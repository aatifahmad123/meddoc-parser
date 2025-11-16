# nlp/paddle_ocr_vl.py
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def parse_document(path):
    """
    Parse document using PaddleOCR.
    Handles both possible OCR return formats:
     - list of pages where each page is a list of lines: [points, (text, score)]
     - list of pages where each page is a dict containing 'rec_texts' (and 'rec_scores' etc)

    Returns plain text (joined lines) or empty string on error.
    """
    try:
        result = ocr.ocr(path)
    except Exception as e:
        print("OCR ERROR:", e)
        return ""

    print("RAW RESULT:", result)

    if not result or not isinstance(result, list):
        print("ERROR: Unexpected OCR output format")
        return ""

    text_lines = []

    for page in result:
        # Case A: page is a dict with rec_texts (some Paddle wrappers return this)
        if isinstance(page, dict):
            rec_texts = page.get("rec_texts")
            if isinstance(rec_texts, (list, tuple)):
                for t in rec_texts:
                    if isinstance(t, str) and t.strip():
                        text_lines.append(t.strip())
            # fallback: maybe 'rec_boxes' + 'rec_scores' present, ignore
            continue

        # Case B: page is a list of lines: each line -> [points, (text, score)] or similar
        if isinstance(page, list):
            for line in page:
                # safe extraction for multiple formats
                try:
                    # common Paddle format: [points, (text, score)]
                    if isinstance(line, (list, tuple)) and len(line) >= 2:
                        second = line[1]
                        # second could be tuple (text, score)
                        if isinstance(second, (list, tuple)) and len(second) >= 1:
                            text = second[0]
                        # or it might be directly a string
                        elif isinstance(second, str):
                            text = second
                        else:
                            text = None
                    # sometimes line might be a dict containing 'text' key
                    elif isinstance(line, dict) and "text" in line:
                        text = line.get("text")
                    else:
                        text = None

                    if isinstance(text, str) and text.strip():
                        text_lines.append(text.strip())
                except Exception:
                    # ignore malformed line
                    continue

    final_text = "\n".join(text_lines).strip()
    print("PARSED TEXT:\n", final_text)
    return final_text
