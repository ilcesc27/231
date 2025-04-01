
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogo Reati 231", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_completo_231_art24_25_COMPLETO.xlsx")

df = load_data()

st.markdown("""<style>
    .card {
        background-color: #1e1e1e;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        border-left: 5px solid #FF4B4B;
    }
    .badge {
        display: inline-block;
        background-color: #2a2a2a;
        padding: 2px 10px;
        border-radius: 20px;
        margin-right: 8px;
        font-size: 0.85em;
    }
</style>""", unsafe_allow_html=True)

st.title("📱 Reati 231 – Art. 24 & 25")
st.markdown("Un’interfaccia elegante, pensata per la compliance moderna. Pulita, chiara, fluida. In stile iPhone 📱.")

tab1, tab2 = st.tabs(["📚 Reati", "📊 Statistiche"])

# --- TAB 1 ---
with tab1:
    articoli_231 = st.multiselect("📂 Famiglia 231", options=df["Articolo 231"].unique(), default=list(df["Articolo 231"].unique()), key="famiglia")
    stato = st.multiselect("🛑 Stato", options=df["Stato"].unique(), default=list(df["Stato"].unique()), key="stato")
    cerca = st.text_input("🔎 Cerca reato...", "", key="search")

    filtered = df[
        df["Articolo 231"].isin(articoli_231) &
        df["Stato"].isin(stato) &
        df["Reato"].str.contains(cerca, case=False, na=False)
    ]

    st.markdown(f"🧠 **{len(filtered)} reati trovati**")

    for art in sorted(filtered["Articolo 231"].unique()):
        st.markdown(f"## 🧩 {art}")
        famiglia_df = filtered[filtered["Articolo 231"] == art]
        for _, row in famiglia_df.iterrows():
            stato_badge = "🟢 Vigente" if row["Stato"] == "Vigente" else "🔴 Abrogato"
            st.markdown(f'''
            <div class="card">
                <div><b>{row['Articolo 231']} – {row['Articolo c.p.']} c.p.</b></div>
                <div style="margin-top: 6px;">📝 <i>{row['Reato']}</i></div>
                <div style="margin-top: 6px;">
                    <span class="badge">{stato_badge}</span>
                    <span class="badge">📅 {row['Ultimo aggiornamento']}</span>
                </div>
                <div style="margin-top: 8px;">🔗 <a href="{row['Fonte Normattiva']}" target="_blank">Vai a Normattiva</a></div>
            </div>
            ''', unsafe_allow_html=True)

# --- TAB 2 ---
with tab2:
    st.subheader("📊 Statistiche generali")
    v = df[df["Stato"] == "Vigente"].shape[0]
    a = df[df["Stato"] == "Abrogato"].shape[0]
    aggiornati = df[df["Ultimo aggiornamento"] >= "2022-01-01"].shape[0]
    st.metric("✅ Reati vigenti", v)
    st.metric("❌ Reati abrogati", a)
    st.metric("🧾 Aggiornati dal 2022", aggiornati)
