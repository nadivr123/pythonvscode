import streamlit as st
import pandas as pd

st.set_page_config(layout= 'wide')

st.title("Data editor app")

upload_csv = st.file_uploader('Upload any file')

if upload_csv:
    csv_file = pd.read_csv(upload_csv)
    edit_csv = st.data_editor(csv_file)

    if st.button("Save the file"):
        pass