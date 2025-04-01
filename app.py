import streamlit as st
import pandas as pd
import difflib

st.set_page_config(page_title="231 Navigator", layout="centered")

@st.cache_data
def load_dati_reati():
    return pd.read_excel("catalogo_reati_con_tutte_famiglie.xlsx", sheet_name="Reati")

@st.cache_data
def load_storico():
    return pd.read_excel("storico_316bis.xlsx")

df_reati = load_dati_reati()
df_storico = load_storico()

st.markdown("""
<style>
h1 {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    margin-top: 1rem;
}
.big-button {
    display: flex;
    justify-content: center;
    margin-top: 2rem;
}
button.css-1x8cf1d.edgvbvh3 {
    font-size: 22px;
    padding: 1rem 2rem;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# 📘 231 Navigator")

page = st.radio("Scegli cosa esplorare", ["🏠 Home", "🧩 Esplora reati", "📜 Modifiche storiche art. 316-bis"], horizontal=True)

if page == "🏠 Home":
    st.markdown("Benvenuto in una nuova esperienza di compliance. Scopri, esplora e resta aggiornato sul D.Lgs. 231/2001 in stile Apple.")
    st.markdown("### Cosa puoi fare:")
    st.markdown("- 🧩 Naviga le famiglie di reato")
    st.markdown("- 📜 Consulta le modifiche normative")
    st.markdown("- 🧾 Prepara verbali e documentazione OdV")

elif page == "🧩 Esplora reati":
    famiglie = sorted(df_reati["Famiglia"].unique())
    scelta = st.selectbox("🔍 Seleziona una Famiglia", famiglie)
    subset = df_reati[df_reati["Famiglia"] == scelta]

    if subset.empty:
        st.warning("⛔ Nessun reato ancora caricato per questa famiglia.")
    else:
        for _, row in subset.iterrows():
            with st.expander(f"{row['Art. Cod. Penale']} – {row['Reato']}"):
                st.markdown("📄 **Testo vigente:**")
                st.markdown(row["Testo"])
                st.markdown("💰 **Sanzioni:**")
                st.markdown(f"- Pecuniaria: {row['Sanzione Pecuniaria']}")
                st.markdown(f"- Interdittiva: {row['Sanzione Interdittiva']}")
                st.markdown("📜 **Modifiche normative storiche:**")
                st.markdown(row["Modifiche storiche"])

elif page == "📜 Modifiche storiche art. 316-bis":
    st.subheader("📜 Storico normativo – Art. 316-bis c.p.")
    versione_attuale = df_storico[df_storico["Modifica"] == "Versione attuale"].iloc[0]["Testo"]

    for _, row in df_storico.iterrows():
        if row["Modifica"] == "Versione attuale":
            continue
        with st.expander(f"{row['Modifica']} ({row['Data']})"):
            st.markdown("**Testo di allora:**")
            st.markdown(row["Testo"])
            if st.toggle("🔍 Mostra confronto con versione attuale", key=row["Data"]):
                differenze = difflib.unified_diff(
                    row["Testo"].split(),
                    versione_attuale.split(),
                    fromfile="storico",
                    tofile="attuale",
                    lineterm=""
                )
                st.code("\n".join(differenze), language="diff")
