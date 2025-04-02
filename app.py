
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Art. 316-bis – Apple Style", layout="centered")

# Icone: da sostituire con immagini locali reali nella cartella /images/
ICON_TESTO = "📄"
ICON_SANZIONI = "💰"
ICON_STORICO = "📜"

# Testo formattato del reato
testo_reato = """
Chiunque, estraneo alla pubblica Amministrazione, avendo ottenuto dallo Stato o da altro ente pubblico o dalle Comunità europee contributi, finanziamenti, mutui agevolati o altre erogazioni dello stesso tipo, comunque denominate, destinati alla realizzazione di una o più finalità, non li destina alle finalità previste, è punito con la reclusione da sei mesi a quattro anni.
"""

# HTML per il testo reato (corsivo + spacing Apple-style)
testo_html = f"""
<div style='font-style: italic; font-size: 18px; line-height: 1.6; color: #333; margin-bottom: 20px;'>
{testo_reato}
</div>
"""

# Sanzioni dettagliate
sanzioni = [
    "Pecuniaria: da 100 a 500 quote; nei casi di rilevante profitto o danni di particolare gravità da 200 a 600 quote.",
    "Interdittiva: divieto di contrattare con la pubblica amministrazione; esclusione da agevolazioni, finanziamenti, contributi o sussidi ed eventuale revoca di quelli già concessi; divieto di pubblicizzare beni e servizi; da tre mesi a due anni."
]

# Modifiche storiche
modifiche = [
    ("L. 86/1990", "Introdotto con "),
    ("L. 181/1992", "Modificato da "),
    ("L. 3/2019", "Modificato da "),
    ("D.Lgs 75/2020", "Modificato da "),
    ("L. 137/2023", "Modificato da ")
]

# Layout
st.markdown("<h1 style='font-size: 36px;'>Art. 316-bis c.p. – Malversazione di erogazioni pubbliche</h1>", unsafe_allow_html=True)

st.markdown(f"<h3 style='margin-top: 20px;'>{ICON_TESTO} Testo vigente:</h3>", unsafe_allow_html=True)
st.markdown(testo_html, unsafe_allow_html=True)

st.markdown(f"<h3 style='margin-top: 30px;'>{ICON_SANZIONI} Sanzioni:</h3>", unsafe_allow_html=True)
for s in sanzioni:
    st.markdown(f"- {s}")

st.markdown(f"<h3 style='margin-top: 30px;'>{ICON_STORICO} Modifiche normative storiche:</h3>", unsafe_allow_html=True)
for legge, label in modifiche:
    link_legge = f"<a href='#' style='color: #007aff; text-decoration: none;'>{label}{legge}</a>"
    st.markdown(f"- {link_legge}", unsafe_allow_html=True)

st.markdown("<br><hr style='margin-top: 40px;'><br>", unsafe_allow_html=True)
st.caption("💡 Tocca una modifica per consultare la versione storica. Prossimamente: link diretti ai testi PDF e timeline animata.")
