# Page1: REGISTER OF USERS INFO
# (profile pic, all other info (name, age,email, grade,,favsubj, sports & hobbies(multiselect),  etc)

import streamlit as st

pfp = st.file_uploader("Upload your Account Profile Picture here",type=['jpg','jpeg','heic','png','webp'])

a1,a2 = st.columns(2)

with a1:
    name = st.text_input("Please type your full name:")
with a2:
    age = st.text_input("Please type your age:")

email = st.text_input("Please type your email address:")


b1,b2 = st.columns([1,2])

with b2:
    subject = st.selectbox("Please select your favourite subject:",['Math','Science','P.E','Explorations','English','Humanities','Language','Art','Music','Theatre','Technology'])
    Hobbies = st.multiselect("Please select your favourite hobby:",['Playing sports','Reading','Playing Video Games','Hanging out with friends','Hiking','Painting','Dancing','Traveling'])
with b1:
    year = st.selectbox("Please select your year:",['Year 7','Year 8','Year 9','Year 10','Year 11','Year 12','Year 13'])
    sport = st.multiselect("Please select your favourite sport:",['Football','Basketball','Tennis','Swimming','Badminton','Hockey/Ice Hockey','Baseball','Cricket','American Football'])

if st.button("Submit results"):
    st.success("Thank you for making an account, your account details have been saved")


# if menu == 'Upload images':
#     st.subheader("Upload Images To View")
#     if uploadimage:
#         st.image(uploadimage)