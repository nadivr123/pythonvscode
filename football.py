# EXAM 100 MARKS

# -CREATE A NEW FILE AND ASK THE COACH TO SUBMIT THE STUDENTS 
# NAME OF PLAYER
# GOALS SCORED
# ASSIST MADE
# TACKLES MADE


# -SAVE IN A CSV FILE - 20 MARKS

# -SHOW THE DICTIONARY OF THE RESPONSE -20 MARKS

# -SHOW THE TABLE OF THE RESPONSE - 5MARKS

# -SHOW THE TABLE FROM THE CSV FILE AT THE TOP (ABOUT 10 SAVED RESPONSES)
# 10 MARKS

# -PLOT A BARCHART OF THE NAMES AGAINST THE GOALS SCORED -20 MARKS

# -PUT A COMMENT IN EVERY LINE TO EXPLAIN WHAT THE CODE DOES -5 MARKS






import streamlit as st
import pandas as pd
import plotly.express as px

database = pd.read_csv("football.csv")# used to read the csv file

menu = st.sidebar.selectbox("menu",["Player information","Player database"])
playerID = 'Player_'+str(len(database)+1)

if menu == 'Player information':

    st.title("Player Information")

    name = st.text_input("Please input the players name")
    goals = st.number_input("Please put the amount of goals this player has scored",1,10000,1)
    assists = st.number_input("Please put the number of assists this player has made",1,10000,1)
    tackles = st.number_input("Please put the number of tackles this player has made",1,10000,1)
    g_a = goals + assists

    st.table(database)
    football_dict = {'PlayerID':[playerID],'Name':[name], 'Goals':[goals], 'assists':[assists], 'Tackles':[tackles], 'G/A':[g_a]}
    football_database = pd.DataFrame(football_dict)
    new_database = pd.concat([database,football_database],ignore_index=True)
    new_database.to_csv('football.csv',index=False)
