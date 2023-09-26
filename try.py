import streamlit as st
from pdf2image.pdf2image import convert_from_path
import pytesseract
import helper
import pandas as pd
from PIL import Image


tesseract_path = r"C:\Users\Rahul\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = tesseract_path

img_ = Image.open("Logo with tagline (CMYK)_with Registered (1).png")
st.sidebar.image(img_, width=250)
st.sidebar.title("Data Collerctor from invoices")


def pdf_to_text(pdf_path):
    poppler_path = r"D:\programing software\Release-23.07.0-0\poppler-23.07.0\Library\bin"
    
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    
    extracted_text = ""
    
    for page_num, pdf_image in enumerate(images, start=1):
        page_text = pytesseract.image_to_string(pdf_image)
        extracted_text += f"Page {page_num}:\n{page_text}"
    
    return extracted_text

def data_creator(buyer="B.M Inofotrade Private Limited",saler='None',item='None',amount='0',Invoice_type = 'None'):
    data_dict = {"Buyer"    :   buyer,
                     "Saler"    :   saler,
                     "Products" :   item,
                     "Total_amount" :   amount,
                     "Invoice Type" :   Invoice_type
                     }    
    data = pd.DataFrame(data_dict)
    return data

folder = st.file_uploader("Enter path of PDF",type=['zip'])
