import streamlit as st
import pandas as pd
import plotly.express as px

database = pd.read_csv("scores.csv") # used to read everything in the csv fine

menu = st.sidebar.selectbox("menu",["submit score","database/chart","Student File"])
st.sidebar.write("**Made By Nadiv DE ROZARIO**")
studentID = 'Student_'+str(len(database)+1)

if menu == "submit score":

    st.title("Student Grades")

    name = st.text_input("Enter the students name: ")

    c1,c2 = st.columns(2)

    with c1:
        math = st.number_input("Enter the students math semester grade: ",1,7)
        english = st.number_input("Enter the students english semester grade; ",1,7)
        science = st.number_input("Enter the students science semester grade: ",1,7)
    with c2:
        hum = st.number_input("Enter the students humanities semester grade:",1,7)
        art = st.number_input("Enter the students art semester grade: ",1,7)
        tech = st.number_input("Enter the students tech semester grade: ",1,7)

    total = hum + art + science + english + math + tech
    avg = int(total/6)

    if avg == 7:
        grade = "A+"
    elif avg == 6:
        grade = "A"
    elif avg == 5:
        grade = "B+"
    elif avg == 4:
        grade = "B"
    elif avg == 3:
        grade = "C"
    elif avg <= 2:
        grade = "F"
        #Name,Math,Science,English,Humanities,Art,Total,Average,Grade
    if st.button("Submit student scores"):
        student_dict = {'StudentID':[studentID],'Name':[name], 'Math':[math], 'Science':[science], 'English':[english], 'Humanities':[hum], 'Art':[art], 'Tech':[tech],
                    'Total':[total], 'Average':[avg], 'Grade':[grade]}
        student_database = pd.DataFrame(student_dict)
        #i created a dictionary of csv columns:python variable,
        # then converted it to a dataframe (table)
        # st.dataframe(student_database)
        new_database = pd.concat([database,student_database],ignore_index=True) # concat means to join database together
        new_database.to_csv('scores.csv',index=False) #write/save the new_database to a csv file
        st.success(f"{name}'s total score is {total}, {name}'s average is {avg}, {name}'s final grade is {grade}")


#Math,Science,English,Humanities,Art,Tech
if menu == "database/chart":
    st.table(database) # to show the data in a table
    subject = ['Math','English','Humanities','Science','Art','Tech']
    subjecttable = database[subject].mean().reset_index()
    subjectrename = subjecttable.rename(columns={'index':'Subject',0:'Grade'})
    chart = st.radio("choose the type of graph/chart you want:",['bar graph','pie chart'],horizontal=True)
    if chart == 'bar graph':
        barchart = px.bar(subjectrename, x='Subject',y='Grade')
        st.plotly_chart(barchart)
    elif chart == 'pie chart':
        piechart = px.pie(subjectrename, names='Subject',values='Grade')
        st.plotly_chart(piechart)

if menu == "Student File":
    header1, header2, header3 = st.columns(3)

    with header2:
        st.subheader("Find Student file")
        findID = st.text_input("Enter Student ID")
        find = st.button("Find Student")

    if find:
        if findID:
            pass