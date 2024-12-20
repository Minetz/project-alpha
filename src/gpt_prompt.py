def repair_transcription(client, transcript_text):
    prompt = """Data la seguente trascrizione, ripara pezzi di conversazione che secondo te sono stati trascritti in modo sbagliato.
    Annota tutte le modifiche aggiungendo ** prima e dopo ** la correzione. 
    Se la conversazione non è separata tra interlocutori, aggiungi <terapeuta> e <paziente>. Associa al terapueta allo psicologo giudicando dal contenuto della conversazione.
    Tutta la conversazione deve essere riportata, non perdere messaggi iniziali o finali. Puo iniziare sia il paziente che il terapeuta."""
    gpt_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": transcript_text}
        ]
    )

    response = gpt_response.choices[0].message.content
    return response