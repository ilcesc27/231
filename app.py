
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reati PA – Art. 24", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_reati_pubblica_amministrazione.xlsx")

df = load_data()

st.title("📘 Reati contro la Pubblica Amministrazione – Art. 24 D.Lgs. 231/2001")
st.markdown("Consulta i reati presupposto principali connessi ai rapporti con la Pubblica Amministrazione. Versione demo con due reati mappati manualmente.")

for _, row in df.iterrows():
    with st.expander(f"{row['Art. Cod. Penale']} – {row['Reato']}"):
        st.markdown(f"**Art. 231:** {row['Art. 231']}")
        st.markdown(f"**Famiglia:** {row['Famiglia']}")
        st.markdown(f"**Stato:** {row['Stato']} | **Ultimo aggiornamento:** {row['Ultimo aggiornamento']}")
        st.markdown("---")
        st.markdown(f"### 📝 Testo integrale del reato
{row['Testo']}")
        st.markdown("### 💰 Sanzioni")
        st.markdown(f"- **Pecuniaria:** {row['Sanzione Pecuniaria']}")
        st.markdown(f"- **Interdittiva:** {row['Sanzione Interdittiva']}")
        st.markdown(f"**Fonte:** {row['Fonte']}")
