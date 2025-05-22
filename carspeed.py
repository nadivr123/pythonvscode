import streamlit as st

name = st.text_input("what is the name of your car")
meter = st.text_input("what is the total distance traveled of your car")
time = st.text_input("What is the time of your car")

speed = meter/time

if speed > 30:
    st.error("Warning your car is going at a speed of",speed,"Which is too fast!")
elif speed > 20 and speed < 30:
    st.warning("Caution,, your car speed is",speed,"be careful when driving!")
elif speed < 20:
    st.success("Your car speed is",speed,"and you are driving safely ")