import streamlit as st
import pandas as pd
import plotly.express as px
#remember the invoice generator
menu = st.sidebar.selectbox("menu",["Questions","Score"])
score = 0

try:
    database = pd.read_csv("medquiz.csv") #try to find and read this file

except:
    database = pd.DataFrame() #create an empty table


if menu == "Questions":
    st.title("Medical Awarness quiz for kids")
    
    name = st.text_input("Please enter your first name(last name also if you have a common name):")
    a1,a2 = st.columns(2)

    with a1:
        ques1 = st.selectbox("What is the main job of your heart?",["Choose","Pumping blood","Digesting food","Storing Energy","Beathing Air"])
        ques2 = st.selectbox("What do vaccines help protect you from?",["Choose","Common Cold","Deadly diseases","Cuts and bruises","None of the above"])
        ques3 = st.selectbox("Why is it important to wash your hands?",["Choose","To smell nice","Prevent sickness","To look clean","All of the above"])
        ques4 = st.selectbox("What should you do if you have a fever?",["Choose","Play outside","Tell adult and rest","eat candy","Sleep very late"])  
        ques5 = st.selectbox("What does a doctor do?",["Choose","Teach math","Fix cars","Help people stay healthy","None of the above"])  
        ques6 = st.selectbox("What is a healthy snack?",["Choose","Candy","Fruits & Nuts","Chips","Soda"])  
        ques7 = st.selectbox("What deos allergy mean?",["Choose","You like it a lot","our body reacts badly to it","You can’t eat it","None of the above"])  
    with a2:
        ques8 = st.selectbox("What should you do if you get a cut?",["Choose","Ignore it","Wash it and put a bandage on it","Show it to your friends","None of the above"])  
        ques9 = st.selectbox("Why is it important to eat breakfast?",["Choose","Best meal of the day","Gives morning energy","Skip it","none of the above"])  
        que10 = st.selectbox("What is one way to keep your bones strong?",["Choose","Eat Junk","Milk/dairy","Avoid excersise","None of the above"])  
        que11 = st.selectbox("What is the purpose of first aid?",["Choose","Help with homework","Emergency care","To make food","To be your friend"])  
        que12 = st.selectbox("What can help your sore throat when you are sick?",["Choose","Drink cold fluids","Drink warm fluids","Drink no fluids","Excersise"])  
        que13 = st.selectbox("What is a common symptom of a cold?",["Choose","Runny nose","Feeling energetic","Happy thoughts","Depression"])  
        que14 = st.selectbox("Why should you cover your mouth when you cough?",["Choose","To look funny","Prevent germ spread","To make a sound","none of the above"])  
    
   
    if st.button("Submit Scores"):
        
        if ques1 == "Pumping blood":
            score +=1
        if ques2 == "Deadly diseases":
            score +=1
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
    