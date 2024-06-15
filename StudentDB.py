import streamlit as st
import pandas as pd

database = pd.read_csv("scores.csv") # used to read everything in the csv fine
st.dataframe(database,use_container_width=True) # to show the data in a table

st.title("Student Grades")

name = st.text_input("Enter the students name: ")

c1,c2 = st.columns(2)

with c1:
    math = st.number_input("Enter the students math results: ",0,8)
    english = st.number_input("Enter the students english results; ",0,8)
    science = st.number_input("Enter the students science results: ",0,8)
with c2:
    hum = st.number_input("Enter the students humanities results:",0,8)
    art = st.number_input("Enter the students art results: ",0,8)

total = hum + art + science + english + math
avg = int(total/5)

if avg == 8:
    grade = "A+"
elif avg == 7:
    grade = "A"
elif avg == 6:
    grade = "B+"
elif avg == 5:
    grade = "B"
elif avg == 4:
    grade = "C"
elif avg <= 3:
    grade = "F"


#Name,Math,Science,English,Humanities,Art,Total,Average,Grade
if st.button("Submit student scores"):
    student_dict = {'Name':[name], 'Math':[math], 'Science':[science], 'English':[english], 'Humanities':[hum], 'Art':[art],
                    'Total':[total], 'Average':[avg], 'Grade':[grade]}
    student_database = pd.DataFrame(student_dict)
    #i created a dictionary of csv columns:python variable,
    # then converted it to a dataframe (table)
    # st.dataframe(student_database)
    new_database = pd.concat([database,student_database],ignore_index=True) # concat means to join database together
    new_database.to_csv('scores.csv',index=False) #write/save the new_database to a csv file
    st.success(f"{name}'s total score is {total}, {name}'s average is {avg}, {name}'s final grade is {grade}")