import streamlit as st

st.title("Using Selectbox and Radion button")

name = st.text_input("Enter your name")

gender = st.radio('Choose your gender',['Male','Female'])

game = st.selectbox('Choose your favorite game',['Minecraft','Roblox','FC Mobile'])




a1,a2,a3= st.columns(3)

with a1:
    st.write('hello')


with a2:
    st.write('hello')


with a3:
    st.write('hello')

b1,b2= st.columns(2)

with b1:
    st.write('hello')


with b2:
    st.write('hello')

