from ocr.paddle_ocr_vl import parse_document
from nlp.extract_entities import extract_entities
from nlp.icd_mapper import map_to_icd
import json

def process_medical_document(path):
    print("Step 1: OCR Parsing...")
    text = parse_document(path)

    print("Step 2: Extracting medical entities...")
    entities = json.loads(extract_entities(text))

    print("Step 3: Mapping ICD codes...")
    icd_results = []
    for disease in entities.get("diseases", []):
        icd_results.append(map_to_icd(disease))

    return {
        "raw_text": text,
        "entities": entities,
        "icd_codes": icd_results
    }

if __name__ == "__main__":
    doc_path = "data/samples/prescription1.jpg"
    output = process_medical_document(doc_path)
    
    print(json.dumps(output, indent=4))
