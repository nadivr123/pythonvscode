#create a app that can generate a CV for students
#by asking a few details
#-name -email (optional) -phone - address
#-prof summary -key skills (text_area) - work exp (text_area) -education (text_area)

#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

import streamlit as st
import requests #interact with other websites/apps

st.set_page_config(layout='wide',page_title="Jop Application A.I CV",page_icon='🧑🏽‍💻')

#--------------------CONFIG-------------------------------

api_key = st.text_input("Enter your API key")  #access key to use their services
api_link = 'https://openrouter.ai/api/v1/chat/completions' #link to connect to openrouter

setup = {'Authorization': f'Bearer {api_key}', 'Content-Type':'application/json'}

#---------------------------------------------------------

#-----------Function to send data to OpenRouter------------
def ask_ai(content):
   data = {'model':'openai/gpt-3.5-turbo','messages':[{'role':'user', 'content':content}]}
   response = requests.post(api_link,headers=setup,json=data) #send the data. post simply mean= send
   return response.json()['choices'][0]['message']['content'] #get the first response from the A.I

#-------------------------------------------------------------

st.sidebar.info(':rainbow[Type your info below]')

if st.sidebar.checkbox('Got a Picture?'):
   picture = st.sidebar.file_uploader('Upload Picture here',type=['jpg','jpeg','png'])

name = st.sidebar.text_input("Please enter your Full name",placeholder='Enter your Full name',label_visibility='collapsed')

address = st.sidebar.text_input("Please enter your Full address",placeholder='Enter your Full address',label_visibility='collapsed')

phone = st.sidebar.text_input("Please enter your phone number",placeholder='Enter your Phone number',label_visibility='collapsed')

if st.sidebar.checkbox('Got an Email?'):
   email = st.sidebar.text_input("Enter your email address",placeholder='Enter your Email address',label_visibility='collapsed')

skills = st.sidebar.text_area("List your key skills",placeholder='List your Key skills',label_visibility='collapsed')

exp = st.sidebar.text_area("List your work experience",placeholder='List enter your Work experience',label_visibility='collapsed')

edu = st.sidebar.text_area("List all the Education you went to",placeholder='List all the Education/Cert you got',label_visibility='collapsed')

#----------Variables to set A.I questions
prof_summary = f"""
Design a professional summary for my CV. Make it 4-5 lines using the information given below
My key skills: {skills}
My work experience: {exp}
My education: {edu}
"""

if st.sidebar.button('Generate My CV'):
   if name and phone and skills and exp and edu and address:
       prof_summary_response = ask_ai(prof_summary)
       st.text_area('You can edit your Professional Summary before downloading',value=prof_summary_response,height=150)

