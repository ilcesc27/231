import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231", layout="wide")

# Caricamento dati
@st.cache_data
def load_data():
    return pd.read_excel("catalogo_completo_231_art24_25_COMPLETO.xlsx")

df = load_data()

# Titolo e introduzione
st.title("📘 Catalogo Reati 231 – Art. 24 & 25")
st.markdown(
    "Una piattaforma smart per esplorare, filtrare e gestire i reati presupposto del D.Lgs. 231/2001. "
    "Versione aggiornata con stato normativo, modifiche recenti, e spazio note OdV."
)

# Tabs principali
tab1, tab2, tab3 = st.tabs(["📚 Reati Presupposto", "📌 Aggiornamenti Normativi", "🧠 Storico + Note"])

# --- TAB 1: Catalogo Reati ---
with tab1:
    st.subheader("📋 Filtra e consulta i reati ex Art. 24 e 25")

    col1, col2, col3 = st.columns(3)
    with col1:
        articoli_231 = st.multiselect("Articolo 231", options=df["Articolo 231"].unique(), default=list(df["Articolo 231"].unique()))
    with col2:
        stato = st.multiselect("Stato", options=df["Stato"].unique(), default=list(df["Stato"].unique()))
    with col3:
        parola = st.text_input("🔎 Cerca nel reato", "")

    filtered_df = df[
        df["Articolo 231"].isin(articoli_231) &
        df["Stato"].isin(stato) &
        df["Reato"].str.contains(parola, case=False, na=False)
    ]

    st.success(f"💡 {len(filtered_df)} reati trovati")

    for _, row in filtered_df.iterrows():
        with st.expander(f"🔹 {row['Articolo 231']} – {row['Reato']}"):
            st.markdown(f"**Articolo c.p.:** {row['Articolo c.p.']}")
            st.markdown(f"**Stato:** {'🟢 Vigente' if row['Stato'] == 'Vigente' else '🔴 Abrogato'}")
            st.markdown(f"**Ultimo aggiornamento:** {row['Ultimo aggiornamento']}")
            st.markdown(f"**Modifica recente:** {row['Modifica recente']}")
            st.markdown(f"**Fonte:** [Vai a Normattiva]({row['Fonte Normattiva']})")
            st.text_area("📝 Note OdV", row["Note OdV"], key=row['Articolo c.p.'])

# --- TAB 2: Aggiornamenti Normativi ---
with tab2:
    st.subheader("🗓️ Reati modificati negli ultimi anni")
    df_recent = df[df["Modifica recente"].notnull()]
    df_recent = df_recent[df_recent["Ultimo aggiornamento"] >= "2019-01-01"]
    st.dataframe(df_recent, use_container_width=True)
    st.download_button("⬇️ Scarica aggiornamenti", df_recent.to_excel(index=False), file_name="aggiornamenti_reati_231.xlsx")

# --- TAB 3: Storico e Note OdV ---
with tab3:
    st.subheader("📑 Storico, stato e annotazioni")
