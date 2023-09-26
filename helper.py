from pdf2image.pdf2image import convert_from_path
from nltk.tokenize import word_tokenize,sent_tokenize
import re
import os

def invoice_predicter(text):
    
    condition_1 = text.find('B M Infotrade Private Limited')
    temp = text[condition_1 - 35: condition_1]
    temp_2 = text[condition_1 - 12: condition_1]
    if "Ack Date" in temp or "Tax Invoice" in temp_2:
        return 'Sales'
    else:
        return 'Purchase'

# collecting data

def sales_data_collecting(text):

    try:
        buyer_pattern = r"Ahlicon Parenterals \(India\) Limited|AGM \(ITS\) [a-zA-Z]* [a-zA-Z]* [a-zA-Z]* India|ACC Limited|[a-zA-Z]* [a-zA-Z]* [a-zA-Z]* LIMITED|[a-zA-Z]* BANK|[a-zA-Z]* [a-zA-Z]* Exports|[a-zA-Z]* Solutions|[a-zA-Z]* [a-zA-Z]* [a-zA-Z]*\. LTD|[a-zA-Z]*.[a-zA-Z]*. [a-zA-Z]* \([a-zA-Z]\) Ltd|[a-zA-Z]* [a-zA-Z]* [a-zA-Z]* [a-zA-Z]* LIMITED|[A-Z]*.[A-Z]*. [A-Z]* [A-Z]* LTD|[A-Z]* [A-Z]* [A-Z]* [A-Z]* Ltd|[a-zA-z]*.[a-zA-z]*.[a-zA-z]*. [a-zA-z]*. Ltd"
        buyer = re.findall(buyer_pattern,text)[0]
    except:
        buyer = "Null"
    

    saler = text[text.find('Limited')-22:text.find('Limited')+8]

    # Items 

    item_pattern_1 = r'\d{1,2} [a-zA-Z0-9]* [a-zA-Z0-9]* [a-zA-Z0-9]*|\d \|.*|\d{1,2} \|[a-zA-Z]\-[a-zA-Z0-9]* [a-zA-Z]* \-[a-zA-Z0-9]*-[a-zA-Z0-9], |\d \).*'

    # pattern_2 = r'\d \).*'

    
    date_patern = r"\d{1,2}\-[a-zA-Z]*\-\d{1,2}|\d{1,2}\.\d{1,2}\.\d{2,4}"

    item = re.findall(item_pattern_1, text)
    try:
        pattern_3 = r'\bTotal\b .*'
        matches_3 = re.findall(pattern_3, text)
        
        def amount(matches_3):
            Total_amount = []
            for i in matches_3:
                a = i.split(' = ')
                Total_amount.append(a[1])
                break
            return Total_amount

        Total_amount = amount(matches_3)
    except:
        amount_pattern = r'\bTotal\b .*'
        amount_match = re.findall(amount_pattern,text)
        Total_amount = amount_match[0].split(" ")[-1]
            
    # Total_amount = matches_3
    date = re.findall(date_patern,text)[0]

    return buyer,saler,item,Total_amount,date

def purchase_data_collecting(text):
    
    pu_buyer,new_item,amount_match,pu_saler = "None"

    # items
    purchase_item = r"\d{1,2} \[[a-zA-Z0-9]* [a-zA-Z0-9]*\-[a-zA-Z0-9]*|\d \|.*|.*CGST.*|\bDESCRIPTION\b\n.*\n.*\n.*\n.*|\d{1,2} \|[a-zA-Z]\-[a-zA-Z0-9]* [a-zA-Z]* \-[a-zA-Z0-9]*-[a-zA-Z0-9], "

    amount_pattern = r'\bTotal\b .*'

    saler_pattern = r"[a-zA-Z]* \([a-zA-Z]*\) Limited|[a-zA-Z]* [a-zA-Z]* & Systems|[A-z]* [A-z]* Limited|[A-z]* [A-z]* [A-z]* Ltd|[a-zA-Z]* [a-zA-Z]* SOLUTION|[a-zA-Z]* Electronics"
    
    buyer_pattern =  r"AGM \(ITS\) [a-zA-Z]* [a-zA-Z]* [a-zA-Z]* India|[a-zA-Z]* [a-zA-Z]* [a-zA-Z]* Ltd|[a-zA-Z]* [a-zA-Z]* [a-zA-Z]* [a-zA-Z]* Limited|[a-zA-Z]*.[a-zA-Z]*. [a-zA-Z]* \([a-zA-Z]\) Ltd|[a-zA-Z]* [a-zA-Z]* [a-zA-Z]* [a-zA-Z]* LIMITED|[A-Z]*.[A-Z]*. [A-Z]* [A-Z]* LTD|[A-Z]* [A-Z]* [A-Z]* [A-Z]* Ltd|[a-zA-z]*.[a-zA-z]*.[a-zA-z]*. [a-zA-z]*. Ltd"
    
    date_patern = r"\d{1,2}\-[a-zA-Z]*\-\d{1,2}|\d{1,2}\.\d{1,2}\.\d{2,4}"
        
    new_item = re.findall(purchase_item,text)
        
    amount_match = re.findall(amount_pattern,text)

    pu_saler = re.findall(saler_pattern,text)
    
    pu_buyer = re.findall(buyer_pattern,text)
    
    date = re.findall(date_patern,text)[0]

    return pu_buyer[-1],new_item,amount_match,pu_saler[-1],date

# def save_uploaded_pdf(uploaded_pdf):
#     # Create a unique filename for the uploaded PDF (you might need a more sophisticated naming scheme)
#     pdf_filename = "uploaded_invoice.pdf"

#     # Save the PDF to a temporary directory (you might want to save it to a different location)
#     temp_dir = os.path.join(os.getcwd(), "temp")
#     os.makedirs(temp_dir, exist_ok=True)
    
#     pdf_path = os.path.join(temp_dir, pdf_filename)

#     # with open(pdf_path, "wb") as pdf_file:
#     #     pdf_file.write(uploaded_pdf.read())

#     return pdf_path


def save_uploaded_zip(uploaded_zip):
    # Create a unique folder name for the uploaded zip (you might need a more sophisticated naming scheme)
    zip_folder_name = "uploaded_zip"

    # Save the zip to a temporary directory (you might want to save it to a different location)
    temp_dir = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    # zip_file_path = os.path.join(temp_dir, zip_folder_name + ".zip")
    # os.makedirs(zip_file_path)
    
    zip_file_path = os.path.join(temp_dir,zip_folder_name)
    # os.makedirs(zip_file_path)

    return zip_file_path
