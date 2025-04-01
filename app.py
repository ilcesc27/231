import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reati 231 - Art. 24 e 25", layout="wide")

st.title("📘 Mappatura Reati 231 - Art. 24 e 25")
st.markdown("Consulta i reati rilevanti secondo il D.Lgs. 231/2001 aggiornati con fonti ufficiali.")

# Caricamento dati
df = pd.read_excel("Reati_231_Art24_25_UPDATED.xlsx")

# Filtri
area_filter = st.multiselect("🔍 Filtra per Area 231", options=df["Area 231"].unique(), default=df["Area 231"].unique())
settore_filter = st.multiselect("🏢 Filtra per Settore", options=df["Settore rilevante"].unique(), default=df["Settore rilevante"].unique())
data_filter = st.date_input("📅 Mostra reati modificati dopo:", pd.to_datetime("2020-01-01"))

# Applica filtri
filtered_df = df[
    df["Area 231"].isin(area_filter) &
    df["Settore rilevante"].isin(settore_filter) &
    (pd.to_datetime(df["Data ultima modifica"]) >= pd.to_datetime(data_filter))
]

st.dataframe(filtered_df)

# Link a Normattiva
st.subheader("📎 Link alle norme su Normattiva")
for _, row in filtered_df.iterrows():
    st.markdown(f"**{row['Reato']}** – [Vai alla norma]({row['Fonte']})")
