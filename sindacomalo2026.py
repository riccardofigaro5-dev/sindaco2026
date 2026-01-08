import streamlit as st

st.set_page_config(page_title="Chi è il tuo candidato ideale?", layout="centered")

st.title("🗳️ Scopri il candidato più vicino alle tue idee")
st.write("Rispondi alle domande scegliendo la posizione che condividi di più.")

questions = [
    {
        "question": "Sicurezza",
        "answers": {
            "Via tutti gli immigrati": "De Zen",
            "Pace e amore": "Marsetti",
            "Serve più polizia": "Dalla Riva",
            "Non è un tema prioritario": "Sette"
        }
    },
    {
        "question": "Ambiente",
        "answers": {
            "Bloccare tutte le grandi opere": "De Zen",
            "Investire solo sulle rinnovabili": "Marsetti",
            "Sviluppo tecnologico e nucleare": "Dalla Riva",
            "Tema secondario": "Sette"
        }
    },
    {
        "question": "Tassazione",
        "answers": {
            "Tassare i più ricchi": "Marsetti",
            "Abbassare le tasse a tutti": "De Zen",
            "Tasse ridotte per le imprese": "Dalla Riva",
            "Nessuna proposta chiara": "Sette"
        }
    }
]

scores = {"Marsetti": 0, "De Zen": 0, "Dalla Riva": 0, "Sette": 0}

for i, q in enumerate(questions):
    choice = st.radio(
        f"**{q['question']}**",
        list(q["answers"].keys()),
        key=i
    )
    scores[q["answers"][choice]] += 1

if st.button("🔍 Scopri il risultato"):
    winner = max(scores, key=scores.get)

    st.success("✅ Risultato calcolato!")
    st.subheader("Il candidato più vicino alle tue idee è:")

    candidate_names = {
        "Marsetti": "Marsetti",
        "De Zen": "De Zen",
        "Dalla Riva": "Dalla Riva",
        "Sette": "Sette"
    }

    st.markdown(f"## 🏆 {candidate_names[winner]}")
    st.write("### Punteggi finali:")
    st.write(scores)
