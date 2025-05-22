# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))


# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name


# the other page plots the charts of all users who answered and shows their scores

import streamlit as st

name = st.text_input("Please type your name in the box below")
Email = st.text_input("Please type your Email adress in the box below")


Ques1 = st.slider("What year was the only year england won the world cup?",min_value=1900,max_value=2022)
Ques2 = st.selectbox("Who won the 2024 Ballon d'or?",['Haaland','Lamine Yamal','Rodri','Jude Bellingham'])
Ques3 = st.selectbox("Where is the 2026 world cup going to be held at?",['Canada','USA','Mexico','All of the above'])
Ques4 = st.selectbox("Who is the all time premier league scorer?",['Thierry Henry','Alan Shearer','Cristiano Ronaldo','Micheal Owen'])
Ques5 = st.selectbox('Who is known as the "Black Spider"',['Didier Drogba','JJ Okocha','Lev Yashin','Antonio Rudiger'])
Ques6 = st.slider('When was the red card first introduced?',min_value=1900,max_value=2020)
Ques7 = st.selectbox("Who has more goal crontributions between MS10 and CR7?",['Messi','Ronaldo'])
Ques8 = st.selectbox("Who is the only person to have won the Super Ballon d'or?",['Ronaldo','Messi','Di Stefano','Ruud Gullit'])
Ques9 = st.slider("How many years has messi been in barelona (including his academy years)",min_value=1,max_value=30)
Que10 = st.slider("When did the only goal keeper to win a Ballon d'or win it?",min_value=1920,max_value=2024)
