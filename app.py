import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reati 231 ↔ Codice Penale", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("Reati_Art24_25_231_PA_POPOLATO.xlsx")

df = load_data()

st.markdown(
    "<h1 style='font-size: 3rem; font-weight: 700; color: #0A84FF;'>📘 Reati 231 ↔ Codice Penale</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='font-size: 1.2rem; color: #555;'>Naviga tra i reati previsti dal D.Lgs. 231/2001 e le corrispondenze con il Codice Penale. Interfaccia ispirata allo stile Apple: semplice, elegante, funzionale.</p><hr>",
    unsafe_allow_html=True
)

for articolo in df["Articolo 231"].unique():
    subset = df[df["Articolo 231"] == articolo]

    st.markdown(f"<h2 style='color:#1d1d1f'>🧩 {articolo} – {subset['Rubrica Articolo 231'].iloc[0]}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#f2f2f7; padding:1rem; border-radius:12px; margin-bottom:1rem; font-family:-apple-system;'>"
                f"<strong>📜 Testo dell'articolo {articolo}:</strong><br>{subset['Testo Articolo 231'].iloc[0].replace(chr(10), '<br>')}</div>",
                unsafe_allow_html=True)

    st.markdown("<h3 style='color:#3c3c43;'>🔗 Reati del Codice Penale collegati</h3>", unsafe_allow_html=True)

    for _, row in subset.iterrows():
        st.markdown(f"""
            <div style='border-radius: 16px; background-color: #ffffff; padding: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 1.5rem;'>
                <h4 style='margin-bottom: 0.5rem; color: #0A84FF;'>🔹 {row['Articolo CP']} – {row['Rubrica Articolo CP']}</h4>
                <details style='margin-top: 0.5rem;'>
                    <summary style='cursor:pointer; color:#555;'>📄 Visualizza testo completo</summary>
                    <p style='margin-top: 0.5rem;'>{row['Testo Articolo CP'].replace(chr(10), '<br>')}</p>
                </details>
            </div>
        """, unsafe_allow_html=True)
