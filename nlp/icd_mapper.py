import pandas as pd
from rapidfuzz import process

df = pd.read_csv("nlp/icd10.csv")

def map_to_icd(disease_name):
    choices = df['Disease Name'].tolist()
    best_match, score, idx = process.extractOne(disease_name, choices)
    
    icd_code = df.iloc[idx]['ICD Code']
    return {
        "input": disease_name,
        "match": best_match,
        "icd_code": icd_code,
        "confidence": score
    }
