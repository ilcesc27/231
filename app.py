
import streamlit as st
import pandas as pd

st.set_page_config(page_title="231 Navigator – Famiglie Complete", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_reati_con_tutte_famiglie.xlsx", sheet_name="Reati")

df = load_data()

st.title("📘 231 Navigator – Tutte le Famiglie di Reato")

famiglie_disponibili = sorted(df["Famiglia"].unique())
famiglia_scelta = st.selectbox("🧩 Seleziona una Famiglia di Reato", famiglie_disponibili)

reati_famiglia = df[df["Famiglia"] == famiglia_scelta]

if reati_famiglia.empty:
    st.info("🔍 Nessun reato trovato per questa famiglia.")
else:
    for _, row in reati_famiglia.iterrows():
        with st.expander(f"{row['Art. Cod. Penale']} – {row['Reato']}"):
            st.markdown(f"🧾 **Testo**")
            st.markdown(row["Testo"])
            st.markdown("💰 **Sanzioni**")
            st.markdown(f"- Pecuniaria: {row['Sanzione Pecuniaria']}")
            st.markdown(f"- Interdittiva: {row['Sanzione Interdittiva']}")
            st.markdown(f"📜 **Modifiche normative storiche:**")
            st.markdown(row["Modifiche storiche"])
            st.markdown(f"📅 Ultimo aggiornamento: {row['Ultimo aggiornamento']} | Stato: {row['Stato']}")
            st.markdown(f"🔗 Fonte: {row['Fonte']}")
