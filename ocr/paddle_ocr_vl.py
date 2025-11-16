# nlp/paddle_ocr_vl.py
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def parse_document(path):
    """
    Parse document using PaddleOCR.
    Returns plain text (joined lines) or empty string on error.
    """
    try:
        result = ocr.ocr(path)
    except Exception as e:
        print("OCR ERROR:", e)
        return ""

    if not result or not isinstance(result, list):
        print("ERROR: Unexpected OCR output format")
        return ""

    text_lines = []

    for page in result:
        if isinstance(page, dict):
            rec_texts = page.get("rec_texts")
            if isinstance(rec_texts, (list, tuple)):
                for t in rec_texts:
                    if isinstance(t, str) and t.strip():
                        text_lines.append(t.strip())
            continue

        if isinstance(page, list):
            for line in page:
                try:
                    if isinstance(line, (list, tuple)) and len(line) >= 2:
                        second = line[1]
                        if isinstance(second, (list, tuple)) and len(second) >= 1:
                            text = second[0]
                        elif isinstance(second, str):
                            text = second
                        else:
                            text = None
                    elif isinstance(line, dict) and "text" in line:
                        text = line.get("text")
                    else:
                        text = None

                    if isinstance(text, str) and text.strip():
                        text_lines.append(text.strip())
                except Exception:
                    continue

    final_text = "\n".join(text_lines).strip()
    print("PARSED TEXT:\n", final_text)
    return final_text
