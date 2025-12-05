# MedDocParser

### *Automated OCR · Medical NER · ICD-10 Coding Pipeline*

MedDocParser is an end-to-end system that extracts text from medical documents (prescriptions, lab reports), identifies clinical entities such as diseases, symptoms, and medications, and maps them to ICD-10 codes. It also includes a **Streamlit web app** for easy document upload and visualization.

---

## **Key Features**

* **OCR Module** (in `/ocr/`)
  Extracts text from PDFs/images using **PaddleOCR**.

* **Medical NER Module** (in `/nlp/`)
  Uses **GPT-4o-mini** to identify diseases, symptoms, medications, and findings.

* **ICD-10 Mapping**
  Fuzzy + substring + exact matching using an ICD-10 CSV dataset.

* **Interactive Streamlit UI**
  Implemented in `app.py` and `app_ui.py`.

* **Modular Architecture**
  Easy to extend, debug, or replace components.

---

## **Project Structure**

```
MedDocParser/
│
├── ocr/                     # OCR pipeline built on PaddleOCR
├── nlp/                     # GPT-based NER and ICD mapping utilities
├── data/
│   └── samples/             # Sample prescriptions/documents
│
├── app.py                   # Main Streamlit backend
├── app_ui.py                # UI components and layout
├── test_gpt.py              # Quick script to test OpenAI API
│
├── requirements.txt         # Python dependencies
├── packages.txt             # System-level dependencies (optional)
├── .gitignore
├── BTP_report.pdf           # Complete technical report
└── Readme.md                # This README file
```

---

## **System Workflow**

1. **Upload a medical document** via the Streamlit UI (`app.py`).
2. **OCR Processing** using PaddleOCR (`/ocr/`).
3. **Medical NER** using GPT-4o-mini (`/nlp/`).
4. **ICD-10 Mapping** using fuzzy + substring + exact matching.
5. **Results Displayed** using Streamlit UI (`app_ui.py`).

---

## **How to Run Locally**

### **1. Clone the repository**

```bash
git clone https://github.com/yourusername/meddoc-parser.git
cd MedDocParser
```

### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

### **3. Export your OpenAI API key**

```bash
export OPENAI_API_KEY="your_key_here"
```

Windows PowerShell:

```powershell
setx OPENAI_API_KEY "your_key_here"
```

### **4. Run the Streamlit app**

```bash
streamlit run app.py
```

The app will open at **[http://localhost:8501](http://localhost:8501)**.

---

## **Example Output**

| Extracted Entity         | ICD-10 Code |
| ------------------------ | ----------- |
| Hypertension             | I10         |
| Type-2 Diabetes Mellitus | E11         |

---

## **Experimental Findings**

* OCR works well on printed prescriptions.
* GPT-based NER shows strong recall even with noisy text.
* Fuzzy ICD matching improves retrieval accuracy.
* Current challenges:

  * Handwritten text
  * API dependency
  * Document variability

---

## **Future Enhancements**

* Offline biomedical NER using BioBERT/PubMedBERT
* Full hierarchical ICD-10 lookup
* Entity highlighting inside documents
* Support for large-scale hospital datasets
* Fully local processing (no external APIs)

---

## **Author**

**Aatif Ahmad**
B.Tech in Artificial Intelligence and Data Science
Indian Institute of Technology Jodhpur

---

## **License**

This project is intended for academic and research use.
