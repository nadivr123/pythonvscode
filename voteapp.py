import streamlit as st

age = st.number_input("please put your age",1)

if age >= 18:
    st.write("your are eligable for voting in the elections")
    elections = st.text_input("please say who you would like to vote to be presedent")
    if st.button("vote"):
        st.success("thank you for voting")
else:
    st.write("you are still to young to vote for the elections")



#ST.WRITE('YES'?)