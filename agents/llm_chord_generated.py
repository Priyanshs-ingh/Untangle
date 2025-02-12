import requests
import json

# Replace with your actual Groq API Key
GROQ_API_KEY = "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"

def get_chords_from_llm(song_lyrics):
    """Uses Groq API (Mixtral/Llama2/Gemma) to generate guitar chords."""

    prompt = f"""
You are an expert guitar teacher. Given the lyrics of a song, generate a **complete and structured chord progression**.

Follow this format:

[Intro]  
Chords

[Verse 1]  
Chords

[Chorus]  
Chords

Make sure to provide all missing chords and **ensure accuracy**.

Lyrics:
{song_lyrics}
"""


    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",  # ✅ Use "mixtral-8x7b", "llama2-70b-chat", or "gemma-7b-it"
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        chords = response.json()["choices"][0]["message"]["content"]
        return {"chords": chords}
    else:
        return {"error": f"Failed to fetch chords. Status Code: {response.status_code}, Response: {response.text}"}

if __name__ == "__main__":
    # ✅ Example: Lyrics of "Perfect" by Ed Sheeran
    song_lyrics = """
    I found a love for me
    Darling, just dive right in
    And follow my lead
    Well, I found a girl, beautiful and sweet
    I never knew you were the someone waiting for me
    """

    result = get_chords_from_llm(song_lyrics)

    # Save to JSON file
    with open("predicted_chords.json", "w") as f:
        json.dump(result, f, indent=4)

    print("✅ Chords Saved to predicted_chords.json")
