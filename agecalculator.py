import streamlit as st

name = st.text_input("Please enter the students name: ")
age = st.number_input("Please enter the students age: ",0)

if st.button("show me"):
    st.success(f"your student is {name} and they are {age}")