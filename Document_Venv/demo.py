import streamlit as st
from pdf2image import convert_from_path
import pytesseract

tesseract_path = r"C:\Users\Rahul\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = tesseract_path

def pdf_to_image(pdf_path, page=0):
    poppler_path = r"D:\programing software\Release-23.07.0-0\poppler-23.07.0\Library\bin"
    
    images = convert_from_path(pdf_path, first_page=page, last_page=page + 1,poppler_path=poppler_path)
    pdf_image = images[0]
    
    extracted_text = pytesseract.image_to_string(pdf_image)

    return extracted_text

pdf_path = r"D:\Data Science(Ekeeda)\Projects\document_classsification\Sales_invoice\salesbill8\Dean, Educational Hardware Division, BITS Invoice No. 5228.pdf"

text = pdf_to_image(pdf_path)

# print(text)
st.write(text)

# print(text[text.find('Limited') -22:text.find('Limited')+8])


