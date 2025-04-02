
import streamlit as st
import pandas as pd

st.set_page_config(page_title="231 Akoma Ntoso Viewer", layout="centered")

@st.cache_data
def load_data():
    return pd.read_excel("Articoli_231_Art24_25_AkomaNtoso.xlsx")

df = load_data()

st.title("📘 D.Lgs. 231/2001 – Art. 24 & 25 (Akoma Ntoso Edition)")
st.markdown("Text extracted from Normattiva XML export – structured for legal clarity and version control.")

for _, row in df.iterrows():
    with st.expander(f"{row['Articolo']} – {row['Titolo']}"):
        st.markdown(f"### {row['Articolo']} – {row['Titolo']}")
        st.markdown(f"<div style='font-size: 17px; line-height: 1.7; font-style: italic; color: #333;'>{row['Testo']}</div>", unsafe_allow_html=True)

        st.markdown("#### 🕰️ Modifiche Normative")
        st.markdown("_To be added_")

        st.markdown("#### 🔍 Versioni Precedenti")
        st.markdown("_To be linked_")

        st.markdown("#### 📌 Esempio Normativo")
        st.markdown("_To be completed_")
