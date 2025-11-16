import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI()

def extract_entities(text):
    prompt = f"""
    Extract medical information from this text.
    Return a JSON object with fields:
    - diseases
    - symptoms
    - medications
    - lab_values
    - notes

    Text:
    {text}
    """

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return resp.choices[0].message.content
