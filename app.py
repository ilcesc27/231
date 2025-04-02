
import streamlit as st
import pandas as pd
from fpdf import FPDF

st.set_page_config(page_title="231 Navigator", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("Catalogo_Reati_231_Art24_25_TAG_PA.xlsx")

df = load_data()

st.title("📘 231 Navigator – Art. 24 & 25 (Tag: PA)")
st.markdown("Explore offenses related to the Public Administration under D.Lgs. 231/2001. You can filter, view details, and export data.")

st.sidebar.title("🔍 Filters")
query = st.sidebar.text_input("Search by keyword...").lower()
tags = st.sidebar.multiselect("Filter by Tag", df["Tag"].unique(), default=list(df["Tag"].unique()))
famiglie = st.sidebar.multiselect("Filter by Famiglia", df["Famiglia di Reato"].unique(), default=list(df["Famiglia di Reato"].unique()))

filtered = df[df["Tag"].isin(tags) & df["Famiglia di Reato"].isin(famiglie)]
if query:
    filtered = filtered[filtered["Titolo Reato"].str.lower().str.contains(query) | filtered["Sotto-articolo"].str.lower().str.contains(query)]

if filtered.empty:
    st.warning("No results found.")
else:
    for _, row in filtered.iterrows():
        with st.expander(f"{row['Sotto-articolo']} – {row['Titolo Reato']}"):
            st.markdown(f"### 📚 {row['Sotto-articolo']} – {row['Titolo Reato']}")
            st.markdown(f"**Famiglia:** {row['Famiglia di Reato']} &nbsp;&nbsp; | &nbsp;&nbsp; **Tag:** {row['Tag']}")

            st.markdown("#### 📜 Article Text")
            st.markdown(row["Testo Articolo"] or "_To be completed_")

            st.markdown("#### 💥 Consequences")
            st.markdown(row["Conseguenze"] or "_To be completed_")

            st.markdown("#### 🕰 Normative Changes")
            st.markdown(row["Modifiche Normative"] or "_To be completed_")

            if row["Versioni Precedenti Link"]:
                st.markdown(f"[🔍 View Previous Versions]({row['Versioni Precedenti Link']})")

            if row["Esempio Normativo"]:
                st.markdown("#### 📌 Example")
                st.markdown(row["Esempio Normativo"])

    if st.button("📥 Export to PDF"):
        def clean(txt): return txt.encode("ascii", "ignore").decode("ascii")
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for _, row in filtered.iterrows():
            pdf.set_font("Arial", style='B', size=14)
            pdf.cell(200, 10, txt=clean(f"{row['Sotto-articolo']} – {row['Titolo Reato']}"), ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, clean("Text: " + str(row["Testo Articolo"] or "")))
            pdf.multi_cell(0, 10, clean("Consequences: " + str(row["Conseguenze"] or "")))
            pdf.multi_cell(0, 10, clean("Normative Changes: " + str(row["Modifiche Normative"] or "")))
            if row["Esempio Normativo"]:
                pdf.multi_cell(0, 10, clean("Example: " + str(row["Esempio Normativo"])))
            pdf.ln(5)

        export_file = "/mnt/data/reati_art24_25_export.pdf"
        pdf.output(export_file)
        st.success("✅ PDF generated.")
        st.markdown(f"[📥 Download PDF]({export_file})")
