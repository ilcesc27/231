import streamlit as st
import pandas as pd

# Creazione del layout di base per l'app Streamlit
def app_layout():
    st.set_page_config(page_title="Normativa 231", layout="wide")
    
    # Intestazione principale
    st.title("Normativa 231/2001 - Reati presupposto")
    st.markdown("""
    Benvenuto nella piattaforma per la consultazione dei reati presupposto previsti dal **D.lgs. 231/2001**. 
    Qui puoi esplorare i vari articoli e scoprire le modifiche normative dal 2021.
    """)
    
    # Sidebar per navigazione
    st.sidebar.title("Navigazione")
    categories = ["Reati contro la Pubblica Amministrazione", "Reati societari", "Reati tributari", "Reati ambientali"]
    selected_category = st.sidebar.selectbox("Seleziona una categoria di reati", categories)
    
    # Simuliamo un catalogo dei reati in un dizionario per la demo
    data = {
        "Articolo": [24, 316],
        "Fattispecie": ["Corruzione", "Corruzione"],
        "Da quando": [2021, "—"],
        "Esporta": ["Sì", "No"]
    }
    
    df = pd.DataFrame(data)
    
    # Visualizzazione della tabella dei reati per la categoria selezionata
    st.subheader(f"Reati: {selected_category}")
    st.write(df)
    
    # Dettagli del reato selezionato
    selected_reato = st.selectbox("Seleziona un reato", df["Fattispecie"])
    
    if selected_reato:
        st.markdown(f"**Dettagli su {selected_reato}:**")
        st.markdown("Descrizione del reato, articoli coinvolti, e altre informazioni importanti.")
    
    # Esportazione dei dati
    if st.button("Esporta in CSV"):
        df.to_csv("/mnt/data/reti_presupposto.csv", index=False)
        st.markdown("File CSV esportato! [Scaricalo qui](sandbox:/mnt/data/reti_presupposto.csv)")

# Avviare il layout dell'app
app_layout()
