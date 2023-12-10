import fitz
import json
import requests

def extract_text_from_bbox(pdf_url, json_url):
    json_data = requests.get(json_url).json()
    pdf_data = requests.get(pdf_url).content
    pdf_document = fitz.open("pdf", pdf_data)

    extracted_data = {}

    for entry in json_data:
        field_name, bbox_values = list(entry.items())[0]
        page_number = int(bbox_values[0]) - 1
        page = pdf_document[page_number]
        rect = fitz.Rect(*bbox_values[1:])
        text = page.get_text("text", clip=rect)
        extracted_data[field_name] = text.strip()

    pdf_document.close()
    return extracted_data

pdf_url = 'https://github.com/Dexters-IN/pru/raw/main/sample_invoice.pdf'
json_url = 'https://github.com/Dexters-IN/pru/raw/main/sample_invoice.json'

extracted_data = extract_text_from_bbox(pdf_url, json_url)

if extracted_data is not None:
    for field_name, text in extracted_data.items():
        print(f"{field_name}: {text}")
