
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231 - Art. 24 e 25", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_completo_231_art24_25_COMPLETO.xlsx")

df = load_data()

st.title("📘 Catalogo Reati 231 – Art. 24 & 25")
st.markdown(
    "Consulta e gestisci in modo smart i reati presupposto ai sensi del D.Lgs. 231/2001, "
    "con indicazione completa di articolo del codice penale, stato e modifiche normative."
)

tab1, tab2, tab3 = st.tabs(["📚 Reati Presupposto", "📌 Aggiornamenti Normativi", "🧠 Storico + Note"])

# --- TAB 1 ---
with tab1:
    st.subheader("📋 Filtra i reati per tipologia e stato")

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
        label = f"{row['Articolo 231']} – {row['Articolo c.p.']} – {row['Reato']}"
        with st.expander(f"🔹 {label}"):
            st.markdown(f"**Articolo c.p.:** {row['Articolo c.p.']}")
            st.markdown(f"**Stato:** {'🟢 Vigente' if row['Stato'] == 'Vigente' else '🔴 Abrogato'}")
            st.markdown(f"**Ultimo aggiornamento:** {row['Ultimo aggiornamento']}")
            st.markdown(f"**Modifica recente:** {row['Modifica recente']}")
            st.markdown(f"**Fonte:** [Vai a Normattiva]({row['Fonte Normattiva']})")
            st.text_area("📝 Note OdV", row["Note OdV"], key=row['Articolo c.p.'])

# --- TAB 2 ---
with tab2:
    st.subheader("📌 Reati aggiornati dal 2019")
    df_recent = df[df["Modifica recente"].notnull()]
    df_recent = df_recent[df_recent["Ultimo aggiornamento"] >= "2019-01-01"]
    st.dataframe(df_recent, use_container_width=True)
    st.download_button("⬇️ Scarica aggiornamenti", df_recent.to_excel(index=False), file_name="aggiornamenti_reati_231.xlsx")

# --- TAB 3 ---
with tab3:
    st.subheader("🧠 Riepilogo stato e note OdV")
    st.dataframe(df[["Articolo 231", "Articolo c.p.", "Reato", "Stato", "Ultimo aggiornamento", "Note OdV"]], use_container_width=True)
    st.markdown("✍️ Le note possono essere inserite nei singoli reati sopra. Salvataggio avanzato in arrivo.")
