# Lista di domande e risposte con relative posizioni dei candidati
questions = [
    {
        "question": "Qual è la tua posizione sulla sicurezza?",
        "answers": [
            {"text": "Via tutti gli immigrati", "candidate": "Candidato B"},
            {"text": "Pace e amore", "candidate": "Candidato A"},
            {"text": "Serve più polizia", "candidate": "Candidato C"},
            {"text": "Non menziona", "candidate": "Candidato D"}
        ]
    },
    {
        "question": "Qual è la tua posizione sull'ambiente?",
        "answers": [
            {"text": "No agli inceneritori", "candidate": "Candidato B"},
            {"text": "Sostegno all'energia rinnovabile", "candidate": "Candidato A"},
            {"text": "Sviluppo delle centrali nucleari", "candidate": "Candidato C"},
            {"text": "Non menziona", "candidate": "Candidato D"}
        ]
    },
    {
        "question": "Qual è la tua posizione sulla tassazione?",
        "answers": [
            {"text": "Tassare le grandi ricchezze", "candidate": "Candidato A"},
            {"text": "Abbassare le tasse per tutti", "candidate": "Candidato B"},
            {"text": "Tassare solo le multinazionali", "candidate": "Candidato C"},
            {"text": "Non menziona", "candidate": "Candidato D"}
        ]
    }
]

# Funzione principale per raccogliere le risposte dell'utente
def ask_questions():
    scores = {
        "Candidato A": 0,
        "Candidato B": 0,
        "Candidato C": 0,
        "Candidato D": 0
    }

    # Iteriamo attraverso le domande
    for q in questions:
        print(q["question"])
        # Mostriamo le risposte
        for idx, answer in enumerate(q["answers"]):
            print(f"{idx + 1}. {answer['text']}")
        
        # Raccogliamo la risposta dell'utente
        while True:
            try:
                answer_idx = int(input("Scegli una risposta (1-4): ")) - 1
                if 0 <= answer_idx < 4:
                    break
                else:
                    print("Per favore, scegli un numero tra 1 e 4.")
            except ValueError:
                print("Input non valido. Per favore, scegli un numero tra 1 e 4.")
        
        # Incrementiamo il punteggio per il candidato corrispondente
        selected_answer = q["answers"][answer_idx]
        scores[selected_answer["candidate"]] += 1
    
    return scores

# Funzione per determinare il candidato più vicino
def determine_candidate(scores):
    # Troviamo il candidato con il punteggio più alto
    most_suitable_candidate = max(scores, key=scores.get)
    return most_suitable_candidate

# Funzione principale del programma
def main():
    print("Benvenuto al quiz sui candidati sindaco!")
    
    # Raccogliamo le risposte
    scores = ask_questions()
    
    # Determiniamo il candidato più vicino
    winner = determine_candidate(scores)
    
    # Stampa il risultato
    print(f"\nIl tuo candidato sindaco più vicino alle tue opinioni è: {winner}!")
    print(f"Dettagli punteggi: {scores}")

if __name__ == "__main__":
    main()
