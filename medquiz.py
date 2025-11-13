import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF #this is used to generate PDF
import base64 #to write what you have on your computer to the PDF doc
#remember the invoice generator
menu = st.sidebar.selectbox("menu",["Questions","Score",])
score = 0
imagelink = 'cert.png'

try:
  database = pd.read_csv("medquiz.csv") #try to find and read this file

except:
  database = pd.DataFrame() #create an empty table

if menu == "Questions":
   st.title("Medical Awarness quiz for kids")
   name = st.text_input("Please enter your first name(last name also if you have a common name):")
   a1,a2 = st.columns(2)

   with a1:
      st.info('Question 1')
      ques1 = st.selectbox("What is the main job of your heart?",["Choose","Pumping blood","Digesting food","Storing Energy","Beathing Air"])
      st.info('Question 2')
      ques2 = st.selectbox("What do vaccines help protect you from?",["Choose","Common Cold","Deadly diseases","Cuts and bruises","None of the above"])
      st.info('Question 3')
      ques3 = st.selectbox("Why is it important to wash your hands?",["Choose","To smell nice","Prevent sickness","To look clean","All of the above"])
      st.info('Question 4')
      ques4 = st.selectbox("What should you do if you have a fever?",["Choose","Play outside","Tell adult and rest","eat candy","Sleep very late"])
      st.info('Question 5')
      ques5 = st.selectbox("What does a doctor do?",["Choose","Teach math","Fix cars","Help people stay healthy","None of the above"])
      st.info('Question 6')
      ques6 = st.selectbox("What is a healthy snack?",["Choose","Candy","Fruits & Nuts","Chips","Soda"])
      st.info('Question 7')
      ques7 = st.selectbox("What deos allergy mean?",["Choose","You like it a lot","our body reacts badly to it","You can’t eat it","None of the above"])
      
   with a2:
      st.info('Question 8')
      ques8 = st.selectbox("What should you do if you get a cut?",["Choose","Ignore it","Wash it and put a bandage on it","Show it to your friends","None of the above"])
      st.info('Question 9')
      ques9 = st.selectbox("Why is it important to eat breakfast?",["Choose","Best meal of the day","Gives morning energy","Skip it","none of the above"])
      st.info('Question 10')
      que10 = st.selectbox("What is one way to keep your bones strong?",["Choose","Eat Junk","Milk/dairy","Avoid excersise","None of the above"])
      st.info('Question 11')
      que11 = st.selectbox("What is the purpose of first aid?",["Choose","Help with homework","Emergency care","To make food","To be your friend"])
      st.info('Question 12')
      que12 = st.selectbox("What can help your sore throat when you are sick?",["Choose","Drink cold fluids","Drink warm fluids","Drink no fluids","Excersise"])
      st.info('Question 13')
      que13 = st.selectbox("What is a common symptom of a cold?",["Choose","Runny nose","Feeling energetic","Happy thoughts","Depression"])
      st.info('Question 14')
      que14 = st.selectbox("Why should you cover your mouth when you cough?",["Choose","To look funny","Prevent germ spread","To make a sound","none of the above"])

   
   if st.button("Submit Scores"):


       if ques1 == "Pumping blood":
           score +=1
       elif ques1 == 'Choose':
           st.error('Question 1 not answered yet')

       if ques2 == "Deadly diseases":
           score +=1
       elif ques2 == 'Choose':
           st.error('Question 2 not answered yet')

       if ques3 == "Prevent sickness":
           score +=1

       if ques4 == "Tell adult and rest":
           score +=1

       if ques5 == "Help people stay healthy":
           score +=1

       if ques6 == "Fruits & Nuts":
           score +=1

       if ques7 == "our body reacts badly to it":
           score +=1

       if ques8 == "Wash it and put a bandage on it":
           score +=1

       if ques9 == "Gives morning energy":
           score +=1

       if que10 == "Milk/Dairy":
           score +=1

       if que11 == "Emergency care":
           score +=1

       if que12 == "Drink warm fluids":
           score +=1

       if que13 == "Runny nose":
           score +=1
          
       if que14 == "prevent germ spread":
           score +=1

       if (ques1 == 'Choose' or ques2 == 'Choose' or ques3 == 'Choose' or ques4 == 'Choose' or ques5 == 'Choose' ):
          pass
       else:

           st.table(database)
           answers_dict = {'Name':[name],'Score':[score]}
           answers_database = pd.DataFrame(answers_dict)
           new_database = pd.concat([database,answers_database],ignore_index=True)
           new_database.to_csv('medquiz.csv',index=False)
    
           st.success("Thanks for your answers, please check your results on the menu labelled 'Score'")
if menu == "Score":

  st.title ("Results")
  st.table(database)

  chart = st.radio("choose the type of graph/chart you want:",['bar graph','pie chart'],horizontal=True)
  if chart == 'bar graph':
      barchart = px.bar(database, x='Name',y='Score')
      st.plotly_chart(barchart)
  elif chart == 'pie chart':
      piechart = px.pie(database, names='Name',values='Score')
      st.plotly_chart(piechart)

if st.sidebar.toggle('Download certificate'):
  #create function to generate our PDF
  def generate_pdf():
      pdf = FPDF(orientation='L') #this is to create a new PDF page

      #add a new page
      pdf.add_page()

      # set column X and Y
      colx = 20
      coly = 20

      # set column width and height
      colw = 100
      colh = 10

      # add the background certificate
      pdf.image(imagelink,x=0,y=0,w=210,h=300)

      # save the pdf
      pdf_file = 'cert.pdf' #name
      pdf.output(pdf_file)
      return pdf_file
    
  pdf_funct = generate_pdf() #store

  #read the pdf funct as binary data
  with open(pdf_funct, 'rb') as binary:
      pdf_data = binary.read()

  #write the PDF funct
  pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

  dl1, dl2 = st.columns(2)
  with dl1:
      if st.button ("Download Your Certificate"):
          pass

  with dl2:
      if st.button("View Your Certificate"):
          #generate the HTML to embed the PDF on the screen
          pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="70%" height="600px" />'
          #display the embedded pdf
          st.markdown(pdf_embed,unsafe_allow_html=True)