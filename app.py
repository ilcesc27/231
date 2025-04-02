
import streamlit as st
import pandas as pd

st.set_page_config(page_title="231 Navigator", layout="centered")

# SELEZIONE PAGINA
page = st.radio("Scegli cosa esplorare", [
    "🏠 Home",
    "🧩 Esplora reati",
    "📜 Modifiche storiche art. 316-bis",
    "🍏 Reato Apple-style"
], horizontal=True)

# === HOME ===
if page == "🏠 Home":
    st.title("📘 231 Navigator")
    st.markdown("Benvenuto in una nuova esperienza di compliance. Scopri, esplora e resta aggiornato sul D.Lgs. 231/2001 in stile Apple.")
    st.markdown("### Cosa puoi fare:")
    st.markdown("- 🧩 Naviga le famiglie di reato")
    st.markdown("- 📜 Consulta le modifiche normative")
    st.markdown("- 📑 Prepara verbali e documentazione OdV")

# === DEMO APPLE-STYLE CON ESPORTAZIONE ===
elif page == "🍏 Reato Apple-style":
    st.markdown("<h1 style='font-size: 36px;'>Art. 316-bis c.p. – Malversazione di erogazioni pubbliche</h1>", unsafe_allow_html=True)

    # Testo in corsivo
    testo_reato = """
Chiunque, estraneo alla pubblica Amministrazione, avendo ottenuto dallo Stato o da altro ente pubblico o dalle Comunità europee contributi, finanziamenti, mutui agevolati o altre erogazioni dello stesso tipo, comunque denominate, destinati alla realizzazione di una o più finalità, non li destina alle finalità previste, è punito con la reclusione da sei mesi a quattro anni.
"""
    st.markdown("📄 **Testo vigente:**")
    st.markdown(f"<div style='font-style: italic; font-size: 18px; line-height: 1.6; color: #333;'>{testo_reato}</div>", unsafe_allow_html=True)

    st.markdown("💰 **Sanzioni:**")
    st.markdown("- Pecuniaria: da 100 a 500 quote; nei casi di rilevante profitto o danni di particolare gravità da 200 a 600 quote.")
    st.markdown("- Interdittiva: divieto di contrattare con la pubblica amministrazione; esclusione da agevolazioni, finanziamenti, contributi o sussidi ed eventuale revoca di quelli già concessi; divieto di pubblicizzare beni e servizi; da tre mesi a due anni.")

    st.markdown("📜 **Modifiche normative storiche:**")
    modifiche = [
        ("L. 86/1990", "Introdotto con "),
        ("L. 181/1992", "Modificato da "),
        ("L. 3/2019", "Modificato da "),
        ("D.Lgs 75/2020", "Modificato da "),
        ("L. 137/2023", "Modificato da ")
    ]
    for legge, label in modifiche:
        st.markdown(f"- <a href='#' style='color: #007aff; text-decoration: none;'>{label}{legge}</a>", unsafe_allow_html=True)

    # Esportazione (simulazione)
    if st.button("📥 Esporta in formato Excel"):
        data = {
            "Articolo": ["Art. 316-bis c.p."],
            "Testo": [testo_reato],
            "Sanzioni": ["Pecuniaria e Interdittiva"],
            "Modifiche": [", ".join([x[0] for x in modifiche])]
        }
        df = pd.DataFrame(data)
        export_path = "/mnt/data/316bis_esportazione.xlsx"
        df.to_excel(export_path, index=False)
        st.success("✅ File generato!")
        st.markdown(f"[📂 Scarica il file Excel]({export_path})")

# === ALTRE PAGINE (placeholder) ===
elif page == "🧩 Esplora reati":
    st.info("🔍 Sezione Esplora reati in aggiornamento Apple-style...")

elif page == "📜 Modifiche storiche art. 316-bis":
    st.info("🕰 Integrazione modifiche storiche in corso...")
