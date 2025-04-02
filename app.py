
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
            st.markdown(f"## {row['Art. Cod. Penale']} – {row['Reato']}")
            st.markdown("📄 **Testo vigente:**")
            st.markdown(row["Testo"])
            st.markdown("💰 **Sanzioni:**")
            st.markdown(f"- Pecuniaria: {row['Sanzione Pecuniaria']}")
            st.markdown(f"- Interdittiva: {row['Sanzione Interdittiva']}")
            st.markdown("📜 **Modifiche normative storiche:**")
            st.markdown(row["Modifiche storiche"])

            # Visualizzazione diretta versioni storiche con toggle
            if "316-bis" in row["Art. Cod. Penale"]:
                st.markdown("### 📚 Versioni precedenti disponibili")
                if st.toggle("📂 Mostra versioni storiche", key="toggle_" + row["Art. Cod. Penale"]):
                    versioni = df_storico[df_storico["Modifica"] != "Versione attuale"]
                    opzioni = versioni["Data"].tolist()
                    data_scelta = st.selectbox("📅 Seleziona una versione", opzioni, key="select_" + row["Art. Cod. Penale"])
                    versione_storica = versioni[versioni["Data"] == data_scelta].iloc[0]["Testo"]
                    st.markdown("🧾 **Testo della versione selezionata:**")
                    st.markdown(versione_storica)

                    if st.toggle("🔁 Confronta con la versione attuale", key="diff_" + row["Art. Cod. Penale"]):
                        attuale = df_storico[df_storico["Modifica"] == "Versione attuale"].iloc[0]["Testo"]
                        differenze = difflib.unified_diff(
                            versione_storica.split(),
                            attuale.split(),
                            fromfile=f"Versione {data_scelta}",
                            tofile="Attuale",
                            lineterm=""
                        )
                        st.code("\n".join(differenze), language="diff")

elif page == "📜 Modifiche storiche art. 316-bis":
    st.subheader("📜 Storico normativo – Art. 316-bis c.p.")
    versione_attuale = df_storico[df_storico["Modifica"] == "Versione attuale"].iloc[0]["Testo"]

    for _, row in df_storico.iterrows():
        if row["Modifica"] == "Versione attuale":
            continue
        with st.expander(f"{row['Modifica']} ({row['Data']})"):
            st.markdown("**Testo di allora:**")
            st.markdown(row["Testo"])
            if st.toggle("🔍 Mostra confronto con versione attuale", key="main_diff_" + row["Data"]):
                differenze = difflib.unified_diff(
                    row["Testo"].split(),
                    versione_attuale.split(),
                    fromfile="storico",
                    tofile="attuale",
                    lineterm=""
                )
                st.code("\n".join(differenze), language="diff")
