def repair_transcription(client, transcript_text):
    prompt = """Given the following transcription, repair any parts of the conversation that you think were transcribed incorrectly.
    Mark all modifications by adding ** before and after ** the correction.
    If the conversation is not separated between speakers, add <therapist> and <patient>. There might be multiple people in the conversation, but only one therapist. Identify the therapist's lines by analyzing the conversation content.
    The entire conversation must be included, do not lose any messages from the beginning or end. Either the patient or the therapist can start the conversation.
    Do not change the language of the transcription."""
    gpt_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": transcript_text}
        ]
    )

    response = gpt_response.choices[0].message.content
    return response