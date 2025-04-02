import streamlit as st
import pandas as pd

# Configurazione della pagina
st.set_page_config(page_title="📜 Normativa 231", layout="wide")

# ---- Stile personalizzato (quasi "macOS feel") ----
st.markdown("""
    <style>
    body { font-family: 'San Francisco', -apple-system, BlinkMacSystemFont, sans-serif; }
    .stApp { background-color: #f9f9f9; }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }
    .title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #222;
    }
    .label {
        color: #888;
        font-size: 0.85rem;
        margin-bottom: 0.2rem;
    }
    .button-row button {
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Header ----
st.title("📘 Normativa 231 - Reati presupposto")
st.caption("Versione aggiornata con visualizzazione semplificata delle modifiche dal 2021.")

# ---- Sidebar ----
st.sidebar.header("🧭 Navigazione")
categorie = [
    "Reati contro la Pubblica Amministrazione",
    "Reati societari",
    "Reati tributari",
    "Reati ambientali"
]
categoria_sel = st.sidebar.selectbox("Seleziona una categoria", categorie)

# ---- Simulazione dati ----
reati = pd.DataFrame({
    "Articolo": ["24", "316-bis"],
    "Fattispecie": ["Corruzione", "Malversazione"],
    "Da quando": ["2021", "—"]
})

# ---- Layout a due colonne ----
col1, col2 = st.columns([2, 3])

# ---- Colonna sinistra: elenco articoli ----
with col1:
    st.subheader(f"📚 {categoria_sel}")
    for idx, row in reati.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="card">
                <div class="title">Art. {row['Articolo']} – {row['Fattispecie']}</div>
                <div class="label">Da quando: <strong>{row['Da quando']}</strong></div>
                <div class="button-row">
                    <button>📄 Mostra dettagli</button>
                    <button>⏳ Mostra modifiche</button>
                    <button>⬇️ Esporta</button>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ---- Colonna destra: dettagli dell'articolo selezionato ----
with col2:
    st.subheader("📝 Modifiche del 2021 – Art. 24")
    st.markdown("""
    <div class="card">
        <p><strong>Descrizione:</strong><br>
        L’articolo 24 è stato aggiornato per includere nuove fattispecie di corruzione in ambito amministrativo.</p>

        <p><strong>Modifica introdotta:</strong><br>
        Inserito comma che estende la responsabilità agli enti per reati commessi anche da terzi in funzione amministrativa.</p>

        <button>🔍 Mostra modifiche testuali</button>
    </div>
    """, unsafe_allow_html=True)

# ---- Esportazione dati ----
st.markdown("---")
if st.button("⬇️ Esporta tabella in CSV"):
    reati.to_csv("/mnt/data/reati_catalogo_231.csv", index=False)
    st.success("File esportato!")
    st.markdown("[📥 Scarica il CSV](sandbox:/mnt/data/reati_catalogo_231.csv)", unsafe_allow_html=True)
