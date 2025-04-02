import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231", layout="wide")

# Carica i dati
df = pd.read_csv("catalogo_reati_231_completo.csv")

# Sidebar - selezione Famiglia
famiglie = df["Famiglia"].dropna().unique()
famiglia_sel = st.sidebar.selectbox("Seleziona Famiglia di reati", famiglie)

# Filtra i reati della famiglia selezionata
df_filtrato = df[df["Famiglia"] == famiglia_sel]

# Mostra ogni reato come card
st.title("Catalogo Reati D.Lgs. 231/2001")
for _, row in df_filtrato.iterrows():
    st.markdown(f"""
    ### 🧾 {row['Articolo 231']} – {row['Reato']}
    **Fonte:** [normattiva.it]({row['Fonte']})  
    **Data introduzione:** {row['Data introduzione']}  
    **Data modifiche:** {row['Data modifiche']}  

    <details>
      <summary>📜 Mostra fattispecie</summary>
      <p>{row['Fattispecie']}</p>
    </details>
    """, unsafe_allow_html=True)
