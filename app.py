
import streamlit as st
import pandas as pd
from fpdf import FPDF

st.set_page_config(page_title="231 Navigator", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_reati_231_unificato.xlsx")

df = load_data()

# Sidebar per filtro e ricerca
st.sidebar.title("🔍 Filtri")
query = st.sidebar.text_input("Cerca reato o articolo...").lower()
famiglie = st.sidebar.multiselect("Filtra per famiglia", df["Famiglia"].unique(), default=list(df["Famiglia"].unique()))
modifiche = st.sidebar.text_input("Filtra per anno o legge (es. 2020, 2024, L. 3/2019)").lower()

df_filtered = df[df["Famiglia"].isin(famiglie)]
if query:
    df_filtered = df_filtered[df_filtered["Reato"].str.lower().str.contains(query) | df_filtered["Art. Cod. Penale"].str.lower().str.contains(query)]
if modifiche:
    df_filtered = df_filtered[df_filtered["Modifiche storiche"].str.lower().str.contains(modifiche)]

st.title("📘 231 Navigator")
st.markdown("Consulta reati presupposto, modifiche normative, sanzioni e versioni storiche. Ora con esportazione PDF!")

if df_filtered.empty:
    st.warning("Nessun reato trovato.")
else:
    for _, row in df_filtered.iterrows():
        with st.expander(f"{row['Art. Cod. Penale']} – {row['Reato']}"):
            st.markdown(f"<div style='font-style: italic; font-size: 18px; line-height: 1.6; color: #333;'>{row['Testo']}</div>", unsafe_allow_html=True)
            st.markdown("💰 **Sanzioni:**")
            st.markdown(f"- Pecuniaria: {row['Sanzione Pecuniaria']}")
            st.markdown(f"- Interdittiva: {row['Sanzione Interdittiva']}")
            st.markdown("📜 **Modifiche storiche:**")
            st.markdown(f"{row['Modifiche storiche']}")
            st.markdown("🧠 **Spiegazione semplificata:**")
            st.markdown(f"{row['Spiegazione semplificata']}")
            st.markdown("📌 **Esempio applicativo:**")
            st.markdown(f"{row['Esempi applicativi']}")

    # Esportazione PDF
    if st.button("📥 Esporta i risultati in PDF"):
        def clean_text(txt):
            return txt.encode('ascii', 'ignore').decode('ascii')

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for _, row in df_filtered.iterrows():
            pdf.set_font("Arial", style='B', size=14)
            pdf.cell(200, 10, txt=clean_text(f"{row['Art. Cod. Penale']} – {row['Reato']}"), ln=True)
            pdf.set_font("Arial", style='', size=12)
            pdf.multi_cell(0, 10, txt=clean_text("Testo: " + row["Testo"]))
            pdf.multi_cell(0, 10, txt=clean_text("Sanzione Pecuniaria: " + row["Sanzione Pecuniaria"]))
            pdf.multi_cell(0, 10, txt=clean_text("Sanzione Interdittiva: " + row["Sanzione Interdittiva"]))
            pdf.multi_cell(0, 10, txt=clean_text("Modifiche storiche: " + row["Modifiche storiche"]))
            pdf.multi_cell(0, 10, txt=clean_text("Spiegazione: " + row["Spiegazione semplificata"]))
            pdf.multi_cell(0, 10, txt=clean_text("Esempio: " + row["Esempi applicativi"]))
            pdf.ln(5)

        export_path = "/mnt/data/reati_filtrati_export.pdf"
        pdf.output(export_path)
        st.success("✅ PDF generato!")
        st.markdown(f"[📂 Scarica il PDF]({export_path})")
