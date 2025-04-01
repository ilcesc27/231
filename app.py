
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231 - Art. 24 e 25", layout="wide")

st.title("📘 Catalogo Reati 231 - Art. 24 e 25")
st.markdown("Visualizza e filtra tutti i reati presupposto connessi agli articoli 24 e 25 del D.Lgs. 231/2001. Dati aggiornati con stato normativo, modifiche recenti e note OdV.")

# Caricamento dati
df = pd.read_excel("catalogo_completo_231_art24_25_COMPLETO.xlsx")

# Sidebar con filtri
with st.sidebar:
    st.header("🔍 Filtra i reati")
    articoli_231 = st.multiselect("Articolo 231", options=sorted(df["Articolo 231"].unique()), default=list(df["Articolo 231"].unique()))
    stato = st.multiselect("Stato", options=sorted(df["Stato"].unique()), default=list(df["Stato"].unique()))
    parola_chiave = st.text_input("Parola chiave nel reato", "")

# Filtro dati
filtered_df = df[
    df["Articolo 231"].isin(articoli_231) &
    df["Stato"].isin(stato) &
    df["Reato"].str.contains(parola_chiave, case=False, na=False)
]

# Visualizzazione tabella
st.subheader(f"📋 Reati trovati: {len(filtered_df)}")
st.dataframe(filtered_df, use_container_width=True)

# Riepilogo stato
st.markdown("### 📌 Stato normativo")
st.write(filtered_df["Stato"].value_counts())

# Download del file filtrato
st.download_button("⬇️ Scarica tabella filtrata in Excel", data=filtered_df.to_excel(index=False), file_name="reati_filtrati_231.xlsx")

# Dettagli singoli reati
st.markdown("### 🔗 Dettagli e fonti")
for _, row in filtered_df.iterrows():
    st.markdown(f"**{row['Reato']}** – [{row['Articolo c.p.']}]({row['Fonte Normattiva']})")
