from paddleocr import PaddleOCR

# Initialize model
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def parse_document(path):
    result = ocr.ocr(path, cls=True)
    
    text_out = []
    for line in result:
        for word in line:
            text_out.append(word[1][0])  # Extract text content
    
    return "\n".join(text_out)
