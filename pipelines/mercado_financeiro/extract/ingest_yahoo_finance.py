import os
import logging
from datetime import date
import pandas as pd
import yfinance as yf

# =========================
# Configurações
# =========================

DATA_LAKE_PATH = os.getenv("DATA_LAKE_PATH")
DOMINIO = "mercado_financeiro"
FONTE = "yahoo_finance"

DT_CARGA = date.today().isoformat()

ATIVOS_PATH = "pipelines/mercado_financeiro/config/ativos.csv"

LOG_DIR = "pipelines/mercado_financeiro/logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "ingest_yahoo_finance.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a"),
        logging.StreamHandler()
    ]
)

# =========================
# Funções auxiliares
# =========================

def carregar_ativos(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def criar_diretorio_raw(tipo: str, ativo: str) -> str:
    path = os.path.join(
        DATA_LAKE_PATH,
        "raw",
        DOMINIO,
        FONTE,
        f"tipo={tipo}",
        f"ativo={ativo}",
        f"dt_carga={DT_CARGA}"
    )
    os.makedirs(path, exist_ok=True)
    return path


def baixar_dados_yahoo(ticker: str, data_inicio: str) -> pd.DataFrame:
    df = yf.download(
        ticker,
        start=data_inicio,
        interval="1d",
        progress=False
    )
    df.reset_index(inplace=True)
    return df

# =========================
# Pipeline principal
# =========================

def main():
    ativos = carregar_ativos(ATIVOS_PATH)

    logging.info(f"### PIPELINE INICIADO ###")

    for _, row in ativos.iterrows():
        ticker = row["ticker"]
        tipo = row["type"]
        data_inicio = row["effective_date"]

        try:
            print(f"Iniciando ingestão do ativo {ticker}")
            logging.info(f"Iniciando ingestão do ativo {ticker}")

            df = baixar_dados_yahoo(ticker, data_inicio)

            if df.empty:
                print(f"Nenhum dado retornado para {ticker}")
                logging.info(f"Nenhum dado retornado para {ticker}")
                continue

            df["ativo"] = ticker
            df["tipo"] = tipo
            df["fonte"] = FONTE
            df["dt_ingestao"] = DT_CARGA

            output_path = criar_diretorio_raw(tipo, ticker)
            file_path = os.path.join(
                output_path,
                f"{ticker.lower()}_diario.parquet"
            )

            df.to_parquet(file_path, index=False)
            print(f"Dados salvos em {file_path}")
            logging.info(f"Dados salvos em {file_path}")

        except Exception as e:
            print(f"Erro ao processar {ticker}: {e}")
            logging.error(f"Erro ao processar {ticker}: {e}")
    
    logging.info(f"### PIPELINE FINALIZADO ###")

if __name__ == "__main__":
    main()