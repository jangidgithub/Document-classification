import os
import zipfile
import helper

import streamlit as st


def zip_data_path(folder):
    pdf_path_list = []
    root_ = []
    if folder is not None:
        # Specify the path to the uploaded zip file
        zip_file_path = os.path.join(os.getcwd(),folder.name)
        
        extracted_folder = 'extracted_data'
        # Create a directory to extract the zip contents
        os.makedirs(extracted_folder, exist_ok=True)
        

        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)

        # Process the extracted PDF files
        
        for root, _, files in os.walk(extracted_folder):
            return root
