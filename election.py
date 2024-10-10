import streamlit as st
import pandas as pd
import plotly.express as px

#Freshman
jackM = 0
CharM = 0
AvaW = 0
JeffA = 0

#Junior high school
JackL = 0
LeckS = 0
TyE = 0
RagB = 0

st.subheader("")
name = st.text_input("Please type your first and last name")


selectcampaign = st.radio("Select a campaign",['Freshman','Junior School','High School'])



if selectcampaign == 'Freshman':
    st.image("https://s3.amazonaws.com/org.kellenberg.www-media/wp-content/uploads/2020/03/09101244/20191213-Boys-Freshman-Track-Rodriguez.jpg")
    if st.checkbox("Jack Miller"):
        st.success("Thank you for voting for Jack Miller")
        jackM = +1
    st.image("https://s3.amazonaws.com/org.kellenberg.www-media/wp-content/uploads/2020/03/05102146/20191213-Girls-Freshman-Track-12-ORegan.jpg")
    if st.checkbox("Charlotte Smith"):
        st.success("Thank you for voting for Charlotte Smith")
        CharM = +1
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoEW4GBDAXjREv-bjjgWDL5UVuJ0KtwMAeRQ&s")
    if st.checkbox("Ava Wilson"):
        st.success("Thank you for voting for Ava Wilson")
        AvaW = +1
    st.image("https://s3.amazonaws.com/org.kellenberg.www-media/wp-content/uploads/2019/11/18192319/20191009-Boys-Freshman-Cross-Country-Ronan-scaled.jpg")
    if st.checkbox("Jeff Anderson"):
        st.success("Thank you for voting for Jeff Anderson")
        JeffA= +1

if selectcampaign == 'Junior School':
    st.image("https://s3.amazonaws.com/org.kellenberg.www-media/wp-content/uploads/2019/11/18192322/20191009-Boys-Freshman-Cross-Country-Jackson-scaled.jpg")
    if st.checkbox("Jackson Lopez"):
        st.success("Thank you for voting for Jackson Lopez")
        JackL= +1
    st.image("https://s3.amazonaws.com/org.kellenberg.www-media/wp-content/uploads/2019/11/14091746/20191025-JV-B-Football-Leckler-scaled.jpg")
    if st.checkbox("Leckler Smith"):
        st.success("Thank you for voting for Leckler Smith")
        LeckS= +1
    st.image("https://s3.amazonaws.com/org.kellenberg.www-media/wp-content/uploads/2018/11/04113631/Tyler-Evert.jpg")
    if st.checkbox("Tyler Evert"):
        st.success("Thank you for voting for Tyler Evert")
        TyE= +1
    st.image("https://s3.amazonaws.com/org.kellenberg.www-media/wp-content/uploads/2019/11/14091748/20191025-JV-B-Football-Ragusa-scaled.jpg")
    if st.checkbox("Ragusa Brown"):
        st.success("Thank you for voting for Ragusa Brown")
        RagB= +1