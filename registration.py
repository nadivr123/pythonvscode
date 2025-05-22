import streamlit as st
import pandas as pd

try:
    database = pd.read_csv("registration.csv") #try to find and read this file

except:
    database = pd.DataFrame() #create an empty table

menu = st.sidebar.selectbox("Menu",['Register Student','View Student'])



if menu == 'Register Student':
    
    st.subheader('Student Info')
    uploadimage = st.file_uploader("Please Upload an image of your child (image must be formal)",type=['jpg','jpeg','heic','png','webp'])
    
    a1, a2 = st.columns(2)
    
    name = st.text_input("Please enter your chlid's first and last name:")
    with a1:
        birth = st.date_input("Please enter your child's date of birth:")
        email = st.text_input("Please enter your child's email address:")
    with a2:
        grade = st.selectbox("Please enter what grade your child is in:",['Grade 6','Grade 7','Grade 8','Grade 9','Grade 10','Grade 11','Grade 12'])
        gender = st.radio("Please enter your child's gender:",['Male','Female'],horizontal=True)

    
    st.subheader('Parent Info')
    b1, b2 = st.columns(2)

    with b1:
        Pname = st.text_input("Please enter your first and last name:")
        rela = st.text_input("Please enter how you're related to the student:")
        address = st.text_input("Please enter your address (e.g Country, city, area, house)")
    with b2:
        Pcontact = st.text_input("Please enter your phone number (e.g _ _ _+ _ _ _ _ _ _ _ _)")
        job = st.text_input("Please enter your occupation:")
        Pemail = st.text_input("Please enter your email address:")

    picname = 'studentimage'




    if st.button("Submit Student And Parent Info:"):
        with open(f'{picname}.png','wb') as writepic:
            writepic.write(uploadimage.getbuffer())
            st.success("Image Saved")
        info_dict = {'Birth':[birth],'Student Email':[email],'year':[grade],'Gender':[gender],'Parent Name':[Pname],'Relationship':[rela],'Address':[address],
                  'Parents Contact':[Pcontact],'Parents Job':[job],'Parents Email':[Pemail]}
        info_database = pd.DataFrame(info_dict)
        two_database = pd.concat([database,info_database],ignore_index=True)
        two_database.to_csv('registration.csv',index=False)
        st.success("Your information has been saved into our database, all information can be seen in the View Student section. Thank you for registering to our secondary school.")
     
if menu == 'View Student':

    st.table(database)
    st.image('studentimage.png')