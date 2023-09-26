import streamlit as st
from pdf2image.pdf2image import convert_from_path
import pytesseract
import helper
import pandas as pd
from PIL import Image
import demo
from transformers import pipeline


import os
import shutil
import base64



tesseract_path = r"C:\Users\Rahul\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = tesseract_path

img_ = Image.open(r"D:\Data Science(Ekeeda)\Projects\document_classsification\Logo with tagline (CMYK)_with Registered (1).png")
st.sidebar.image(img_, width=200)
st.sidebar.title("Data Collerctor from invoices")

# create tapas model function here

def tapas_response(table):
    tqa = pipeline(task="table-question-answering",model="google/tapas-base-finetuned-wtq")
    inputs = {
    "table": table,
    "query": "what flight did Anshul took to DEL?"
    }
    result = tqa(inputs)
    return result

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

def data_creator(buyer,saler,item,amount=0,type_='NONE'):
    # buyer = "B M INFOTRADE PRIVATE LIMITED"
    data_dict = {"Buyer"    :   buyer,
                     "Saler"    :   saler,
                     "Products" :   item,
                     "Total_amount" :   amount,
                     "Invoice Type" :   type_
                     }    
    data = pd.DataFrame([data_dict])
    return data

    
# folder container which take the uploaded file 

zip_folder = st.sidebar.file_uploader("Enter path of PDF",type=['zip'])


try:
    
    folder = demo.zip_data_path(zip_folder)
    if folder:
        if st.sidebar.button('Generate'):
            
            for pdf in os.listdir(folder):
                pdf_path = os.path.join(folder,pdf)


                text = pdf_to_text(pdf_path)

                predict = helper.invoice_predicter(text)

                # st.info(f"{predict} Invoice")
                
                if predict =="Sales":
                    buyer,saler,item,Total_amount = helper.sales_data_collecting(text)
                    
                    sales_entries = data_creator(buyer,saler,item,Total_amount[0],predict)
                    # # st.write(Total_amount[0])
                    empty_list.append(sales_entries)
                    
                elif predict =="Purchase":
                    pu_buyer,items,pu_amount,pu_saler = helper.purchase_data_collecting(text)
                    
                    pu_amount = pu_amount[-1].split(" ")[-1]
                    
                    item = ""
                    for i in items:
                        item += i
                        item +="\n\n"
                        
                    # st.write("Saler",pu_saler)
                    # st.write("Buyer",pu_buyer)
                    # st.write("AMount",pu_amount)
                    # st.write("Product",item)
                    

                    purchase_entries = data_creator(buyer=pu_buyer,saler=pu_saler,item=item,amount=pu_amount,type_=predict)
                    empty_list.append(purchase_entries)
                    
                else:
                    # st.write("Provide the valid Directory")
                    pass
                
            main_data = pd.concat(empty_list, ignore_index=True)
            st.dataframe(main_data)
            
            # if st.button("Download"):
            #     os.chdir(f"{os.path.expanduser('~')}\\Downloads")
            #     main_data.to_csv("Downloads.csv")
            #     st.info("Download Succesfully")

    shutil.rmtree(folder)            
  
except Exception as e:
    st.info("Please upload the File above")
    # st.error(str(e))
    # import traceback
    # st.text(traceback.format_exc())

        