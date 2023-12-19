# Document-classification
The goal of this project is to develop a data extraction tool that can process both PDF and image files and extract specific data fields, including names, organization names, addresses, and contact numbers. The extracted data will be stored in a CSV (Comma-Separated Values) file, which users can easily download for further use.

Key Components
File Upload: Users can upload PDF and image files containing the data they want to extract.
 
Data Extraction: The system will analyze the uploaded files and extract relevant data fields, including:
 
Name of the person
Organization Name
Address
Contact number
Image Preprocessing: For image files, preprocessing techniques may be applied to enhance text recognition and improve accuracy.
 
Multilingual Support: The system will support multiple languages for data extraction, including English and Hindi.
 
CSV Export: The extracted data will be organized and saved in a CSV file format.
 
User-Friendly Interface: A Streamlit-based graphical user interface (GUI) will be created to make the tool accessible and user-friendly.
 
Technical Stack:
 
Programming Language: Python
Libraries: Pytesseract (for text extraction from images), PyPDF2 (for PDF processing), Pillow (for image preprocessing), Streamlit (for GUI), Pandas (for data handling), and OpenCV (for image manipulation).
Workflow:
 
The user uploads a PDF or image file through the GUI.
The system preprocesses the image (if applicable) and extracts the specified data fields using Tesseract OCR (Optical Character Recognition) and PDF parsing.
Extracted data is organized and stored in a CSV file.
The user can download the CSV file containing the extracted data.
Usage Guidelines:
 
Users should upload PDF or image files with clear and legible text to improve extraction accuracy.
For best results, ensure that the uploaded documents are well-scanned or have good image quality.
Verify the extracted data for accuracy, as the system's performance may vary depending on the document's quality and complexity.
Future Improvements:
 
Implementing advanced data validation and verification techniques to enhance data accuracy.
Adding support for additional data fields and languages.
We are enhancing image preprocessing algorithms for improved text extraction from noisy images.
Conclusion:
The "Data Extraction from PDF and Image Files with CSV Export" project aims to provide users with a convenient tool for extracting specific data fields from a variety of document types. It offers a user-friendly interface and the flexibility to process documents in multiple languages. Users can easily download the extracted data in a CSV format for further analysis and use.
