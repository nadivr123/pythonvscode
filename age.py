import streamlit as st
import pandas as pd

database = pd.read_csv('age.csv')
st.dataframe(database,use_container_width=True)

c1,c2 = st.columns(2)

with c1:
    name = st.text_input("Please input your name: ")
with c2:
    age = st.text_input("please inpute your age: ")

if st.button("Submit"):
    age_dict = {'Name':[name],'Age':[age]}
    age_database = pd.DataFrame(age_dict)
    new_database = pd.concat([database,age_database],ignore_index=True)
    new_database.to_csv('age.csv',index=False)
    st.success("new student saved")