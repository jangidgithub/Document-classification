import streamlit as st
from transformers import pipeline
import pandas as pd

def tapas_response(table,query):
    table = table.astype(str)
    tqa = pipeline(task="table-question-answering",model="google/tapas-base-finetuned-wtq")
    inputs = {
    "table": table,
    "query": query
    }
    result = tqa(inputs)
    return result

try:
    table = pd.read_csv(r"D:\Data Science(Ekeeda)\Projects\document_classsification\main_data.csv")
    while True:
        prompt = st.chat_input("Say something")
        if prompt:
            st.write(prompt)
            response = tapas_response(table=table,query=prompt)
        else:
            # st.write("As an tapas model i couldn't fetch the other data which are not in table")
            pass
        
        with st.chat_message("M",avatar="🧑‍💻"):
            st.write(response['answer'])
except Exception as e:
    # st.chat_message("")
    pass
    # st.error(str(e))
    # import traceback
    # st.text(traceback.format_exc())






