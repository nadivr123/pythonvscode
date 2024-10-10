import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox("Choose an option",['Upload CSV','Upload images','Upload audio','Upload Videos'])

if menu == 'Upload CSV':
    st.subheader("Upload CSV & View Database")
    uploadcsv = st.file_uploader("Upload your CSV file here",type='csv')
    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)

        with st.expander("View CSV Table"):
            st.table(readcsv)

if menu == 'Upload images':
    st.subheader("Upload Images To View")
    uploadimage = st.file_uploader("Upload your image file here",type=['jpg','jpeg','heic','png','webp'])
    if uploadimage:
        st.image(uploadimage)

if menu == 'Upload audio':
    st.subheader("Upload Audio To Play")
    uploadaudio = st.file_uploader("Upload your audio file here",type=['mp3','wav'])
    if uploadaudio:
        st.audio(uploadaudio, format='audio/mp3')

if menu == 'Upload Videos':
    st.subheader("Upload Video link To Play")
    uploadvideo = st.text_input("Paste In your Video Link")
    if uploadvideo:
        try:
            if st.button("Play Video"):
                st.video(uploadvideo)
        except:
            st.error("That is not a valid video link")