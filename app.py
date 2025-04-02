
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_excel("Catalogo_Art24_25_231_TAG_PA_updated.xlsx")

st.set_page_config(page_title="231 Navigator", layout="wide")

st.title("📘 D.Lgs. 231/2001 – Art. 24 & 25")
st.subheader("Esplora articoli aggiornati con struttura Akoma Ntoso e visualizzazione migliorata")

df = load_data()

for _, row in df.iterrows():
    with st.expander(f"{row['Sub-articolo']}"):
        st.markdown(f"### 🧾 Articolo")
        st.markdown(f"<div style='font-size: 16px; font-style: italic; padding: 10px; background-color: #f9f9f9; border-radius: 8px'>{row['Testo articolo'].replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

        st.markdown("### 💥 Conseguenze")
        st.write(row["Conseguenze"] or "Da compilare")

        st.markdown("### 📜 Modifiche normative")
        st.write(row["Modifiche normative"] or "Da compilare")

        st.markdown("### 🕰️ Vedi modifiche precedenti")
        st.button("Apri versione precedente")

        st.markdown("### 📌 Esempio normativo")
        st.write(row["Esempio normativo"] or "Da compilare")
