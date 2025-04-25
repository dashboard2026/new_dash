import streamlit as st
import pandas as pd

st.set_page_config(page_title="BASE DE DADOS AVANÇADA", layout="wide")

# Título
st.title("👟⚽🎒👕 PRÉ-VENDA-SS26")

# Caminho do arquivo Excel local
caminho_arquivo = "CARTEIRA_DI_GASPI_24.04.xlsx"
try:
    df = pd.read_excel(caminho_arquivo)

    # Mostrar a tabela
    st.subheader("🖥️ INFORMAÇÕES")
    st.dataframe(df)
except FileNotFoundError:
    st.error("Arquivo não encontrado. Verifique o caminho.")
except Exception as e:
    st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
