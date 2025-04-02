
import streamlit as st
import pandas as pd
from fpdf import FPDF
import difflib

st.set_page_config(page_title="231 Navigator", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_reati_231_completo_demo.xlsx")

df = load_data()

famiglia_color_map = {
    f: color for f, color in zip(df["Famiglia"].unique(), [
        "#007aff", "#34c759", "#ff3b30", "#af52de", "#5ac8fa",
        "#ffcc00", "#ff9500", "#8e8e93", "#5856d6", "#d63384",
        "#00b894", "#e84393", "#6c5ce7", "#fdcb6e", "#fab1a0",
        "#0984e3", "#e17055", "#dfe6e9", "#636e72", "#a29bfe",
        "#ffeaa7", "#b2bec3", "#81ecec"
    ])
}

st.title("📘 231 Navigator")
st.markdown("Consulta reati presupposto, modifiche normative, sanzioni e versioni storiche — in stile Apple 🍎")

st.sidebar.title("🔍 Filtri")
query = st.sidebar.text_input("Cerca reato o articolo...").lower()
famiglie = st.sidebar.multiselect("Filtra per famiglia", df["Famiglia"].unique(), default=list(df["Famiglia"].unique()))
anno = st.sidebar.text_input("Filtra per anno o legge (es. 2020, L. 137/2023)").lower()

df_filtered = df[df["Famiglia"].isin(famiglie)]
if query:
    df_filtered = df_filtered[df_filtered["Reato"].str.lower().str.contains(query) | df_filtered["Art. Cod. Penale"].str.lower().str.contains(query)]
if anno:
    df_filtered = df_filtered[df_filtered["Modifiche storiche"].str.lower().str.contains(anno)]

if df_filtered.empty:
    st.warning("Nessun reato trovato.")
else:
    for _, row in df_filtered.iterrows():
        colore_famiglia = famiglia_color_map.get(row["Famiglia"], "#f0f0f0")
        st.markdown(f"<div style='background-color: {colore_famiglia}20; padding: 1rem; border-left: 6px solid {colore_famiglia}; border-radius: 0.5rem; margin-bottom: 1rem;'>"
                    f"<strong style='font-size: 1.1rem; color: {colore_famiglia};'>📂 Famiglia: {row['Famiglia']}</strong></div>",
                    unsafe_allow_html=True)

        with st.expander(f"{row['Art. Cod. Penale']} – {row['Reato']}"):
            st.markdown(f"<div style='font-size: 22px; font-weight: 700; margin-bottom: 0.2rem;'>{row['Art. Cod. Penale']} – {row['Reato']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-style: italic; font-size: 17px; line-height: 1.6; color: #333; margin-bottom: 1rem;'>{row['Testo']}</div>", unsafe_allow_html=True)

            st.markdown("💰 **Sanzioni:**")
            st.markdown(f"- **Pecuniaria**: {row['Sanzione Pecuniaria']}")
            st.markdown(f"- **Interdittiva**: {row['Sanzione Interdittiva']}")

            st.markdown("📜 **Modifiche storiche della norma:**")
            st.markdown(f"{row['Modifiche storiche']}")

            st.markdown("🧠 **Spiegazione semplificata:**")
            st.markdown(f"{row['Spiegazione semplificata']}")

            st.markdown("📌 **Esempio applicativo:**")
            st.markdown(f"{row['Esempi applicativi']}")

            st.markdown("<hr style='border: 1px solid #e6e6e6; margin: 2rem 0;' />", unsafe_allow_html=True)

    if st.button("📥 Esporta in PDF"):
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
