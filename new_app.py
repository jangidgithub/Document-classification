import streamlit as st
from pdf2image.pdf2image import convert_from_path
import pytesseract
import helper
import pandas as pd
from PIL import Image
import demo
from transformers import pipeline
import json


import os
import shutil



tesseract_path = r"C:\Users\Rahul\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = tesseract_path

st.sidebar.title("🧾 Invoice data collector")
# create pdf to text generator model function here

def pdf_to_text(pdf_path):
    poppler_path = r"D:\programing software\Release-23.07.0-0\poppler-23.07.0\Library\bin"
    
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    
    extracted_text = ""
    
    for page_num, pdf_image in enumerate(images, start=1):
        page_text = pytesseract.image_to_string(pdf_image)
        extracted_text += f"Page {page_num}:\n{page_text}"
    
    return extracted_text

# empty_list using for containg the sale and purchase data which use for concadinate the sales data or purchase data 
empty_list = []
# function for creating the data frame 

def data_creator(buyer,saler,item,amount=0,type_='NONE',date="None"):
    # buyer = "B M INFOTRADE PRIVATE LIMITED"
    data_dict = {"Date"        : date,
                    "Invoice Type" :   type_,
                    "Buyer"    :   buyer,
                    "Saller"    :   saler,
                     "Products" :   item,
                     "Total_amount" :   amount
                     }    
    data = pd.DataFrame([data_dict])
    return data

    
# folder container which take the uploaded file 

try:
    zip_folder = st.sidebar.file_uploader("",type=['zip'])
    
    folder = demo.zip_data_path(zip_folder)
    if folder:
        if st.sidebar.button('Get Data'):
            for pdf in os.listdir(folder):
                pdf_path = os.path.join(folder,pdf)
                text = pdf_to_text(pdf_path)

                predict = helper.invoice_predicter(text)

                # st.info(f"{predict} Invoice")
                # st.write(pdf_path)
                
                if predict =="Sales":
                    buyer,saler,items,Total_amount,date = helper.sales_data_collecting(text)
                    
                    items_string = "\n\n".join(items)
                    
                    # st.write("Date -->",date)
                    # st.write("Buyer -->",buyer)
                    # st.write("Saler -->",saler)
                    # st.write("Products -->",items_string)
                    # st.write("Total Amount -->",Total_amount[-1])
                    
                    sales_entries = data_creator(buyer=buyer,saler=saler,item=items_string,amount=Total_amount[-1],type_=predict,date=date)
                    empty_list.append(sales_entries)
                    
                elif predict =="Purchase":
                    pu_buyer,new_item,amount_match,pu_saler,date = helper.purchase_data_collecting(text)
                    
                    pu_amount = amount_match[-1].split(" ")[-1]
                    
                    items_string = "\n\n".join(new_item)
                    # st.write("Date -->",date)
                    # st.write("Buyer -->",pu_buyer)
                    # st.write("Saler -->",pu_saler)
                    # st.write("Products -->",items_string)
                    # st.write("Total Amount -->",pu_amount)

                    
                    purchase_entries = data_creator(buyer=pu_buyer,saler=pu_saler,item=items_string,amount=pu_amount,type_=predict,date=date)
                    empty_list.append(purchase_entries)
                    
                else:
                    st.write("Provide the valid Directory")
            for entry in empty_list:
                entry["Products"] = "\n\n".join(entry["Products"])
                
            main_data = pd.concat(empty_list, ignore_index=True)
            st.header("🧾 Invoice data ")
            st.dataframe(main_data)
            main_data.to_csv("Main_data_1.csv")
               
    shutil.rmtree(folder) 
               
  
except Exception as e:
    img_ = Image.open(r"D:\Data Science(Ekeeda)\Projects\document_classsification\Logo with tagline (CMYK)_with Registered (1).png")
    st.image(img_, width=250)

    st.info("Please upload the File above")
    # st.error(str(e))
    # import traceback
    # st.text(traceback.format_exc())