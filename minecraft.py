import streamlit as st
import os

st.title("Minecraft store")
st.image("https://i.ytimg.com/vi_webp/EfaJ6n64A8g/maxresdefault.webp")

total = 0
download = st.radio("would you like to download minecraft for $200",["yes","no"],horizontal=True)

if download == "yes":
    st.write("thank you for downloading minecraft")
    total += 200
elif download == "no":
    st.write("why you not download mincraft! Are you to broke? Did your parents not allow you?")
    st.image ("https://pngbuy.com/wp-content/uploads/2023/03/WhatsApp-Emoticon-Cryingsad-emoji-.jpg")
    os._exit(0)

world = st.selectbox("choose what mincraft world you would like to play:",["choose","creative($100)","survival($20)"])

if world == "creative($100)":
    st.write("you have chosen creative for 100 dollars")
    total += 100
elif world == "survival($20)":
    st.write("you have chosen survival for 20 dollars")
    total += 20

costumes = st.selectbox("choose what costume you want:",["choose","pink suit($75)","blue suit($75)","red suit($75)","purple suit($75)","black suit($75)"])

if costumes == "pink suit($75)":
    st.write("you have pink suit for 75 dollars")
    total += 75
elif costumes == "blue suit($75)":
    st.write("you have chosen blue suit for 75 dollars")
    total += 75
elif costumes == "red suit($75)":
    st.write("you have chosen red suit for 75 dollars")
    total += 75
elif costumes == "purple suit($75)":
    st.write("you have chosen purple suit for 75 dollars")
    total += 75
elif costumes == "black suits($75)":
    st.write("you have chosen black suit for 75 dollars")
    total += 75

gems = st.selectbox("choose what gems you would like to buy",["diamond($45)","gold($30)","silver($20)"])

if gems == "diamond($45)":
    st.write("you have picked diamonds for 45 dollars")
    total += 45
elif gems == "gold($30)":
    st.write("you have picked gold for 30 dollars")
    total += 30
elif gems == "silver($20)":
    st.write("you have picked silver for 20 dollars")
    total += 20

if st.button("show total"):
    st.write("your total cost for everything is",total)