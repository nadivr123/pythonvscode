import streamlit as st

name = st.text_input("what is your name?")
age = st.number_input("what is your age?",1,100)
colour = st.text_input("what is your favourite colour?")
fav_food = st.text_input("what is your favoutie food?")
fav_movie = st.text_input("what is your favoutie movie?")
hobby = st.text_input("what are your hobbies?")

if st.button("SUBMIT"):
    st.write("you are",name,"age is",age,"and you favourite things are",colour,",",fav_food,",",fav_movie,"and",hobby,)