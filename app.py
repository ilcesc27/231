import streamlit as st
import pandas as pd

st.set_page_config(page_title="Reati 231 – Art. 24 & 25", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_reati_231_art24_25_mappato.xlsx")

df = load_data()

st.markdown("""<style>
.card {
    background-color: #1e1e1e;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    border-left: 5px solid #FF4B4B;
}
.badge {
    display: inline-block;
    background-color: #444;
    padding: 4px 10px;
    border-radius: 20px;
    margin: 4px 4px 4px 0;
    font-size: 0.85em;
}
</style>""", unsafe_allow_html=True)

st.title("📱 Reati 231 – Art. 24 & 25 (Versione Avanzata)")
st.markdown("Consulta il testo coordinato aggiornato dei reati presupposto in formato smart, completo di sanzioni e struttura per la compliance OdV.")

tab1, tab2 = st.tabs(["📚 Catalogo reati", "📊 Statistiche"])

with tab1:
    famiglie = st.multiselect("🧩 Filtra per Famiglia", options=df["Famiglia"].unique(), default=list(df["Famiglia"].unique()))
    stato = st.multiselect("🛑 Stato", options=df["Stato"].unique(), default=list(df["Stato"].unique()))
    cerca = st.text_input("🔎 Cerca nel reato o testo coordinato...", "")

    filtered = df[
        df["Famiglia"].isin(famiglie) &
        df["Stato"].isin(stato) &
        (df["Reato (rubrica)"].str.contains(cerca, case=False, na=False) |
         df["Testo coordinato"].str.contains(cerca, case=False, na=False))
    ]

    st.markdown(f"🔎 **{len(filtered)} reati trovati**")

    for _, row in filtered.iterrows():
        st.markdown(f'''
        <div class="card">
            <b>{row['Art. 231']} – {row['Art. Cod. Penale']} c.p. – {row['Reato (rubrica)']}</b><br><br>
            <span class="badge">{row['Stato']}</span>
            <span class="badge">📅 {row['Ultimo aggiornamento']}</span>
            <span class="badge">📁 {row['Famiglia']}</span><br><br>
            <div style="font-size: 0.95em; line-height: 1.5;">{row['Testo coordinato']}</div><br>
            <b>💰 Sanzione Pecuniaria:</b> {row['Sanz. pec.']}<br>
            <b>🚫 Sanzione Interdittiva:</b> {row['Sanz. interd.']}
        </div>
        ''', unsafe_allow_html=True)

with tab2:
    st.subheader("📊 Statistiche complessive")
    st.metric("✅ Reati vigenti", df[df["Stato"] == "Vigente"].shape[0])
    st.metric("❌ Reati abrogati", df[df["Stato"] == "Abrogato"].shape[0])
    st.metric("🧾 Totale reati catalogati", df.shape[0])
