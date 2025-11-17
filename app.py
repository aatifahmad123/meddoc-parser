import json
from ocr.paddle_ocr_vl import parse_document
from nlp.extract_entities import extract_entities
from nlp.icd_mapper import load_icd10_csv, map_icd_codes


def process_medical_document(path, icd_csv_path="nlp/icd10.csv"):

    print("Step 1: OCR Parsing...")
    text = parse_document(path) or ""

    print("Step 2: Extracting medical entities...")

    try:
        raw_json = extract_entities(text)
        entities = json.loads(raw_json)
    except Exception as e:
        print("NER ERROR:", e)
        entities = {
            "diseases": [],
            "symptoms": [],
            "medications": [],
            "lab_values": [],
            "notes": ""
        }

    if not isinstance(entities, dict):
        entities = {}

    print("Step 3: Mapping ICD codes...")

    icd_data = load_icd10_csv(icd_csv_path)
    icd_results = map_icd_codes(entities, icd_data)

    return {
        "raw_text": text,
        "entities": entities,
        "icd_codes": icd_results
    }


if __name__ == "__main__":
    doc_path = "data/samples/prescription3.png"
    output = process_medical_document(doc_path)
    print(json.dumps(output, indent=4))
