import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def extract_entities(text):
    prompt = f"""
You are a medical information extractor.
Extract ONLY the following fields and return STRICT VALID JSON:

{{
  "diseases": [],
  "symptoms": [],
  "medications": [],
  "lab_values": [],
  "notes": ""
}}

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Return ONLY valid JSON. No explanations."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content

    if not content:
        return '{"diseases":[],"symptoms":[],"medications":[],"lab_values":[],"notes":""}'

    return content
