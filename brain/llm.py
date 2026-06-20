from openai import OpenAI

client = OpenAI()

def ask_llm(prompt, memory=""):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are LEO OS, a voice-controlled AI system. Convert user instructions into structured JSON actions ONLY when needed."
            },
            {"role": "user", "content": memory + "\nUser: " + prompt}
        ]
    )

    return response.choices[0].message.content