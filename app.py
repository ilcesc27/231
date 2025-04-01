
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231 - PA", layout="wide")

st.title("📘 Catalogo Reati 231 - Rapporti con la Pubblica Amministrazione")
st.markdown("Consulta i reati presupposto rilevanti ai sensi degli articoli 24 e 25 del D.Lgs. 231/2001. I dati sono aggiornati e collegati a Normattiva.")

# Caricamento dati da entrambi i fogli
excel_file = "Catalogo_231_PA_Art24_25.xlsx"
df_art24 = pd.read_excel(excel_file, sheet_name="Reati Art. 24")
df_art25 = pd.read_excel(excel_file, sheet_name="Reati Art. 25")
df_testi = pd.read_excel(excel_file, sheet_name="Testi Articoli")

# Tabs per articoli
tab1, tab2 = st.tabs(["🧾 Articolo 24", "⚖️ Articolo 25"])

with tab1:
    st.subheader("📄 Testo dell'articolo 24")
    st.markdown(df_testi[df_testi["Articolo"] == "Art. 24"]["Testo"].values[0])

    st.subheader("📌 Reati previsti dall'art. 24")
    st.dataframe(df_art24)

    st.markdown("### 🔗 Link diretti alle norme:")
    for _, row in df_art24.iterrows():
        st.markdown(f"- [{row['Reato']} – {row['Articolo']}]({row['Link Normattiva']})")

with tab2:
    st.subheader("📄 Testo dell'articolo 25")
    st.markdown(df_testi[df_testi["Articolo"] == "Art. 25"]["Testo"].values[0])

    st.subheader("📌 Reati previsti dall'art. 25")
    st.dataframe(df_art25)

    st.markdown("### 🔗 Link diretti alle norme:")
    for _, row in df_art25.iterrows():
        st.markdown(f"- [{row['Reato']} – {row['Articolo']}]({row['Link Normattiva']})")
