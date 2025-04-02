
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_excel("reati231.xlsx")

st.set_page_config(page_title="231 Navigator", layout="wide")

df = load_data()

st.title("📘 D.Lgs. 231/2001 – Reati Art. 24 e 25")
st.write("Naviga tra i reati presupposto 231 con stile Apple. Filtra, consulta e scarica le informazioni principali.")

articoli = df["Famiglia di Reato"].unique()

selected = st.selectbox("📂 Seleziona una famiglia di reati", articoli)

filtered = df[df["Famiglia di Reato"] == selected]

for _, row in filtered.iterrows():
    with st.expander(f"{row['Articolo CP']} – {row['Rubrica Articolo CP']}"):
        st.markdown(f"### 📜 Testo dell'articolo\n{row['Testo Articolo 231']}")
        st.markdown(f"**📌 Normativa:** {row['Norma di riferimento']}")
