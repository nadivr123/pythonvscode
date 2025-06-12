# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))


# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name


# the other page plots the charts of all users who answered and shows their scores

import streamlit as st
import pandas as pd
import plotly.express as px

menu = st.sidebar.selectbox("menu",["Questions","Score"])


try:
    database = pd.read_csv("my.csv") #try to find and read this file

except:
    database = pd.DataFrame() #create an empty table


if menu == "Questions":
    name = st.text_input("Please type your name in the box below")
    Email = st.text_input("Please type your Email adress in the box below")

    st.title("How well do you know me?")

    Ques1 = st.slider("At what age did I start to play football?",min_value=1,max_value=13)
    Ques2 = st.slider("What is the date of my birth? (not month or year)",min_value=1,max_value=31)
    Ques3 = st.text_input( "What is my middle name?")
    Ques4 = st.selectbox("What school house am I in",['Da Vinci','Einstien','Fleming','Nansen','Rutherford','Wilberforce'])
    Ques5 = st.text_input('Which friend of mine left HK to go to Japan in year 4?')
    Ques6 = st.text_input("What was the first proper word i ever spoke")
    Ques7 = st.slider("How old is my dad",min_value=1,max_value=100)
    Ques8 = st.number_input("As of now, How many sports do I play?",1)
    Ques9 = st.selectbox("Who is my favourite coding teacher",['Mr.Tee','Ms. Ope','Mr.Mike'])
    Que10 = st.text_input("As of now, Who is my form tutor in school")
    Que11 = st.number_input("As of now, How long is my longest friendship in years?",1)
    Que12 = st.selectbox("As of now, What is my favourite Subject",['P.E','Music','Science','Expo','Humanities','English','Math','Theatre'])
    Que13 = st.selectbox("Do I wear glassess?",['Yes','No','Sometimes','Rarely'])
    Que14 = st.selectbox("Who is my favourite family member",['Dad','Mum','Sister','None of the above'])
    Que15 = st.slider("As of now, how much do I weigh in KG",min_value=1,max_value=100)

    score = 0
    if st.button("Submit Answers"):
        if Ques1 == 3:
            score += 1
        if Ques2 == 16:
            score += 1
        if Ques3 == 'Teague':
            score += 1
        if Ques4 == 'Rutherford':
            score += 1
        if Ques5 == 'Charlie':
            score += 1
        if Ques6 == 'Hi':
            score += 1
        if Ques7 == 49:
            score += 1
        if Ques8 == 4:
            score += 1
        if Ques9 == 'Mr.Tee':
            score += 1
        if Que10 == 'Ms. Weathington':
            score += 1
        if Que11 == 9:
            score += 1
        if Que12 == 'Music':
            score += 1
        if Que13 == 'Sometimes':
            score += 1
        if Que14 == 'None of the above':
            score += 1
        if Que15 == 51:
            score += 1
        st.success(f"Thank you for answering my quiz, your score is {score} out of 15")
        score_dict = {'Name':[name],'Score':[score]}
        score_database = pd.DataFrame(score_dict)
        new_database = pd.concat([database,score_database],ignore_index=True) # concat means to join database together
        new_database.to_csv('my.csv',index=False) #write/save the new_database to a csv file
        st.success(f"your name is {name}, total score is {score}/15. Congrats, and once again thanks for participating in my quiz")
        

if menu == "Score":

    st.title ("Results")

    chart = st.radio("choose the type of graph/chart you want:",['bar graph','pie chart'],horizontal=True)
    if chart == 'bar graph':
        barchart = px.bar(database, x='Name',y='Score')
        st.plotly_chart(barchart)
    elif chart == 'pie chart':
        piechart = px.pie(database, names='Name',values='Score')
        st.plotly_chart(piechart)
    
    