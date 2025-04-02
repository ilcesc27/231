import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231", layout="wide")

# Carica il CSV
df = pd.read_csv("catalogo_reati_231_completo.csv")

# Mostra tutto anche se non ci sono Famiglie definite
st.title("Catalogo Reati D.Lgs. 231/2001")

for _, row in df.iterrows():
    st.markdown(f"""
    <div style="border:1px solid #ccc; padding:15px; border-radius:10px; margin-bottom:15px; background:#f9f9f9">
    <h4>🧾 {row['Articolo 231']} – {row['Reato']}</h4>
    <p><strong>Fonte:</strong> <a href="{row['Fonte']}" target="_blank">normattiva.it</a></p>
    <p><strong>Data introduzione:</strong> {row['Data introduzione'] or '—'}<br>
    <strong>Data modifiche:</strong> {row['Data modifiche'] or '—'}</p>
    <details>
        <summary>📜 Mostra fattispecie</summary>
        <p style="margin-top:10px">{row['Fattispecie']}</p>
    </details>
    </div>
    """, unsafe_allow_html=True)

