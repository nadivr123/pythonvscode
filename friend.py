# write a program for a use
# -ask for the name and -age - use a radio to ask for gender
# -use a selectbox to ask to choose best color - use a type to ask best game
# -use a text input to ask to type best movie - use a text input to ask best friend
# create a submit button and show this in a success bar
# Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe

import streamlit as st
import pandas as pd

database = pd.read_csv("friend.csv")
st.dataframe(database,use_container_width=True)

a1,a2,a3= st.columns(3)

with a1:
    name = st.text_input("Please enter your name:")

with a2:
    age = st.text_input("Please enter your age:")

with a3:
    gender = st.radio("choose your gender",['(M)','(F)'],horizontal=True)

b1,b2= st.columns(2)

with b1:
    colour = st.selectbox("whats your favourite colour?",['red','blue','yellow','purple','green','orange','white','black','gold','silver','pink'])
    movie = st.text_input("What is your favourite movie:")

with b2:
    game = st.text_input("what is your favourite game:")
    bff = st.text_input("who is your best friend")

if st.button("submit"):
    friend_dict = {'Name':[name],'Age':[age],'Gender':[gender],'Colour':[colour],'Movie':[movie],'Game':[game],'BFF':[bff]}
    friend_database = pd.DataFrame(friend_dict)
    new_database = pd.concat([database,friend_database],ignore_index=True)
    new_database.to_csv("friend.csv",index=False)
    st.success("information saved")