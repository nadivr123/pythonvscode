import streamlit as st

name = 'Nadiv'

score = 90

#QUESTION??
#What if I want to store my favorite colors? I want many data stored in one variable

#I need a data collection

#Types of data collection
#-List -Dictionary

colours = st.selectbox("choose your favourite colour",['orange','grey','pink','green','purple'])
Pcolours = st.radio("Choose your favourite primary colour"['red','blue','yellow'])
menu = st.sidebar.selectbox('menu',['Home','contact']) 
