def repair_transcription(client, transcript_text):
    prompt = f"""Data la seguente trascrizione, ripara pezzi di conversazione che secondo te sono stati trascritti in modo sbagliato.
    Annota tutte le modifiche aggiungendo il tag <correzione> prima e dopo <\correzione> la correzione. 
    Se la conversazione non è separata tra interlocutori, aggiungi <terapeuta> e <paziente>.
    Trascrizione: {transcript_text}"""

    gpt_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Se un correttore di trascrizione esperto in sedute psicologiche."},
            {"role": "user", "content": prompt}
        ]
    )

    return gpt_response.choices[0].message.content