import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231", layout="wide")

# Carica dati
df = pd.read_csv("catalogo_reati_231_completo_v2.csv")

# Ricerca globale
st.sidebar.header("🔎 Ricerca")
search = st.sidebar.text_input("Cerca per parola chiave")

# Elenco articoli
articoli_unici = df["Articolo 231"].unique()
articolo_selezionato = st.sidebar.selectbox("📑 Seleziona articolo", articoli_unici)

# Filtro per ricerca e articolo
df_filtrato = df[df["Articolo 231"] == articolo_selezionato]

if search:
    df_filtrato = df_filtrato[df_filtrato.apply(lambda row: search.lower() in row.astype(str).str.lower().to_string(), axis=1)]

# Titolo principale
st.title("📘 Catalogo Reati D.Lgs. 231/2001")

# Mostra risultati
if df_filtrato.empty:
    st.warning("Nessun risultato trovato.")
else:
    for _, row in df_filtrato.iterrows():
        st.markdown(f"""
        <div style="border:1px solid #ccc; padding:15px; border-radius:10px; margin-bottom:15px; background:#f9f9f9">
        <h4>🧾 {row['Articolo 231']} – {row['Reato']}</h4>
        <p><strong>Fonte:</strong> <a href="{row['Fonte']}" target="_blank">normattiva.it</a></p>
        <p><strong>Data introduzione:</strong> {row['Data introduzione'] or '—'}<br>
        <strong>Data modifiche:</strong> {row['Data modifiche'] or '—'}</p>

        <p><strong>💰 Sanzione pecuniaria:</strong> {row['Sanzione pecuniaria']}<br>
        <strong>⛔ Sanzioni interdittive:</strong> {row['Sanzione interdittiva']}</p>

        <details>
            <summary>📜 Mostra fattispecie</summary>
            <p style="margin-top:10px">{row['Fattispecie']}</p>
        </details>
        </div>
        """, unsafe_allow_html=True)
