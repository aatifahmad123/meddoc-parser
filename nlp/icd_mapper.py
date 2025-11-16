# nlp/icd_mapper.py
import csv
import difflib

def load_icd10_csv(csv_path="nlp/icd10.csv"):
    """Load ICD-10 CSV that has columns: ICD Code, Disease Name, Description."""
    icd_list = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            icd_list.append({
                "code": row["ICD Code"].strip(),
                "name": row["Disease Name"].lower().strip(),
                "desc": row["Description"].lower().strip()
            })
    return icd_list


def map_icd_codes(entities, icd_data):
    """Maps diseases/symptoms to ICD codes using exact, substring, and fuzzy matching."""

    diseases = entities.get("diseases", [])
    symptoms = entities.get("symptoms", [])

    terms = diseases + symptoms
    mapped_codes = []

    for term in terms:
        t = term.lower().strip()

        # 1. Exact match with Disease Name
        for item in icd_data:
            if t == item["name"]:
                mapped_codes.append(item["code"])
                continue

        # 2. Substring match with Disease Name or Description
        for item in icd_data:
            if t in item["name"] or item["name"] in t:
                mapped_codes.append(item["code"])
                continue
            if t in item["desc"] or item["desc"] in t:
                mapped_codes.append(item["code"])
                continue

        # 3. Fuzzy match
        names = [item["name"] for item in icd_data]
        best = difflib.get_close_matches(t, names, n=1, cutoff=0.6)
        if best:
            for item in icd_data:
                if item["name"] == best[0]:
                    mapped_codes.append(item["code"])
                    break

    return list(set(mapped_codes))
