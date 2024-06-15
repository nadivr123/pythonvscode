# 1.What is streamlit used for? 
# 2.show 8 ways to display text on streamlit
# 3.show how to ask for a text on streamlit
# 4.show how to ask for a number on streamlit
# 5.create a button on the left column but show the output on the right column ????????????????
# 6.create a radio button with a horizontal orientation
# 7.import an image with a 150*150 size
# 8. read and display a CSV file in python
# 9.create a toggle option to display any database/dataframe
# 10.create a dictionary of 5 different cars with 5 attributes (without using a CSV file) and convert it to a dataframe/table

#streamlit is used to code

import streamlit as st
import pandas as pd

database = pd.read_csv("classwork.csv")
st.dataframe(database,use_container_width=True)

print("hi")
st.text_input("hi")
st.write("hi")
st.success("hi")
st.checkbox("hi")
st.number_input("hi")
st.title("hi")
st.subheader("hi")

st.text_input("would you like 1 millon dollars:")

st.number_input("how much money would you like:")

a1,a2 = st.columns(2)
with a1:
   if st.sidebar.button("button"):
      st.sidebar.write("button does nothing")


teachers = st.radio("choose your teacher",['Mr.Mike','Mr.Tee'])
st.write("you selected",teachers)

st.image("https://cdn.jwplayer.com/v2/media/TZ9cm2sk/poster.jpg?width=720",width=150)

