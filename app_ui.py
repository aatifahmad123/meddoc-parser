import streamlit as st
import json
from app import process_medical_document

st.set_page_config(page_title="Meddoc-Parser", layout="wide")

st.title("Medical Document Parsing + Medical NER + ICD10 Mapping")
st.write("Upload a prescription or medical document to extract diseases, symptoms, medications, and ICD codes.")

uploaded_file = st.file_uploader("Upload Image or PDF", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_path = "temp_upload.jpg"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(file_path, caption="Uploaded Document", use_column_width=True)

    st.info("Processing document...")
    output = process_medical_document(file_path)

    st.subheader("Extracted Text")
    st.text(output["raw_text"])

    st.subheader("Entities")
    st.json(output["entities"])

    st.subheader("ICD Codes")
    st.json(output["icd_codes"])

    st.success("Extraction Complete!")
