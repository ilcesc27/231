import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reati 231 ↔ Codice Penale", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("Reati_Art24_25_231_PA.xlsx")

df = load_data()

st.title("🔗 Mappatura Reati 231 ↔ Codice Penale")
st.markdown("Visualizzazione interattiva dei collegamenti tra il D.Lgs. 231/2001 (artt. 24 e 25) e i reati del Codice Penale.")

articoli_231 = df["Articolo 231"].unique()

for art in articoli_231:
    st.header(f"📘 {art} – {df[df['Articolo 231'] == art]['Rubrica Articolo 231'].iloc[0]}")
    subset = df[df["Articolo 231"] == art]

    for _, row in subset.iterrows():
        with st.container():
            st.markdown(
                f"""
                <div style='padding: 1rem; margin-bottom: 1rem; border-left: 5px solid #0A84FF; background-color: #f9f9f9; border-radius: 8px;'>
                    <strong>🔹 {row['Articolo CP']}</strong> – {row['Rubrica Articolo CP']}
                </div>
                """, unsafe_allow_html=True
            )
