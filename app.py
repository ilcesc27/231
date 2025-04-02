import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reati 231 – Codice Penale", layout="wide")
df = pd.read_csv("catalogo_reati_231_integrato.csv")

st.sidebar.header("🔍 Ricerca")
query = st.sidebar.text_input("Cerca reato, articolo o parola")

articoli = df["Articolo 231"].dropna().unique()
art_sel = st.sidebar.selectbox("📑 Seleziona articolo 231", articoli)

df_filtrato = df[df["Articolo 231"] == art_sel]
if query:
    df_filtrato = df[df.apply(lambda row: query.lower() in row.astype(str).str.lower().to_string(), axis=1)]

st.title("📘 Catalogo Reati D.Lgs. 231/2001 e Articoli Codice Penale")

if df_filtrato.empty:
    st.info("Nessun risultato.")
else:
    for _, row in df_filtrato.iterrows():
        st.markdown(f"""
        <div style="border:1px solid #ddd;padding:1rem;border-radius:10px;margin:1rem 0;background:#fefefe">
        <h4>🧾 {row['Articolo 231']} – {row['Reato']}</h4>
        <p><strong>Art. Codice Penale:</strong> {row['Articolo Codice Penale']}<br>
        <strong>Famiglia:</strong> {row['Famiglia']}</p>

        <p><strong>Fonte:</strong> <a href="{row['Fonte']}" target="_blank">Normattiva</a><br>
        <strong>Data introduzione:</strong> {row['Data introduzione'] or '—'}<br>
        <strong>Data modifiche:</strong> {row['Data modifiche'] or '—'}</p>

        <details><summary>📜 Mostra Fattispecie</summary>
        <p style="margin-top:10px">{row['Fattispecie']}</p></details>
        </div>
        """, unsafe_allow_html=True)
