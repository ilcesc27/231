
import streamlit as st
import pandas as pd

st.set_page_config(page_title="231 Navigator", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel("catalogo_reati_e_famiglie_aggiornato.xlsx", sheet_name="Reati PA")

df = load_data()

st.markdown("""
    <style>
    .big-title {
        font-size: 40px;
        font-weight: 600;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .sub {
        font-size: 20px;
        color: #888;
        margin-bottom: 30px;
    }
    .card {
        background-color: #f9f9f9;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .pill {
        display: inline-block;
        background-color: #eee;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.85em;
        margin-right: 8px;
        color: #444;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">📘 Reati 231 - Navigator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Un’interfaccia pensata per esplorare, capire e documentare i reati presupposto in modo elegante e immediato.</div>', unsafe_allow_html=True)

view = st.radio("Scegli una vista", ["📚 Tutti i reati", "🧩 Famiglia: Reati PA", "📜 Modifiche normative"], horizontal=True)

if view == "📚 Tutti i reati":
    for _, row in df.iterrows():
        with st.expander(f"{row['Art. Cod. Penale']} – {row['Reato']}"):
            st.markdown(f"<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"🧩 <b>Famiglia:</b> {row['Famiglia']}", unsafe_allow_html=True)
            st.markdown(f"🧾 <b>Testo:</b><br>{row['Testo']}", unsafe_allow_html=True)
            st.markdown("💰 <b>Sanzioni</b>", unsafe_allow_html=True)
            st.markdown(f"- Pecuniaria: {row['Sanzione Pecuniaria']}")
            st.markdown(f"- Interdittiva: {row['Sanzione Interdittiva']}")
            st.markdown(f"<span class='pill'>📅 {row['Ultimo aggiornamento']}</span><span class='pill'>Stato: {row['Stato']}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

elif view == "🧩 Famiglia: Reati PA":
    pa_reati = df[df["Famiglia"].str.contains("Pubblica Amministrazione")]
    for _, row in pa_reati.iterrows():
        st.markdown(f"### {row['Art. Cod. Penale']} – {row['Reato']}")
        st.markdown(f"🧾 **Testo:** {row['Testo'][:250]}...")
        st.markdown(f"📅 Ultimo agg.: {row['Ultimo aggiornamento']} | Stato: {row['Stato']}")

elif view == "📜 Modifiche normative":
    for _, row in df.iterrows():
        st.markdown(f"### 🧾 {row['Art. Cod. Penale']} – {row['Reato']}")
        st.markdown("**Modifiche storiche rilevanti:**")
        st.markdown(f"{row['Modifiche storiche']}")
        st.markdown("---")
