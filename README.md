# 231 Navigator

**231 Navigator** è un'app Streamlit progettata per consultare, esplorare ed esportare le informazioni sui reati presupposto previsti dal D.Lgs. 231/2001 in Italia.

## 🔍 Funzionalità
- Ricerca per articolo o parola chiave
- Filtro per famiglia di reato
- Filtro per modifiche normative (es. "2020", "L. 137/2023")
- Visualizzazione Apple-style per ogni reato
- Esportazione in PDF

## 📁 File principali
- `app.py`: codice principale Streamlit
- `catalogo_reati_231_unificato.xlsx`: archivio dei reati
- `requirements.txt`: librerie necessarie

## ▶️ Esecuzione locale
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Requisiti
- Python 3.9+
- Streamlit
- Pandas
- fpdf

## 🔐 Progetto per uso interno (compliance, audit, legal tech)
