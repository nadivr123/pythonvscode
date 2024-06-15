#Create a simple arithmetic calculator that perform addition, subtraction, multiplication and division operation between two numbers.

#Accept user inputs for the two numbers.
# Use an image
# Ensure to add a title

import streamlit as st

st.title("simple arithmetic calculator")
image1,image2,image3=st.columns([1,3,1])
with image2:
    st.image("https://assets-global.website-files.com/61c1a8251c7c762bdbadf2a0/61c1a8251c7c763bc8ae025b_5f2044b0128f70015545e0ba_Calculator%25252520Usage.png")

numberone =  st.number_input("please put a number:",1,10000000000)
numbertwo =  st.number_input("please put another number:",1,100000000000)

add,subtract,multiply,divide = st.columns(4)


with add:
    add = st.button("select for addition")
    if add:
        result = numberone + numbertwo
        st.write(f"your result is {result}")


with subtract:
        subtract = st.button("select for subtraction")
        if subtract:
            result = numberone - numbertwo
            st.write(f"your result is {result}")


with multiply:
        multiply =  st.button("select for multiplication")
        if multiply:
            result = numberone * numbertwo
            st.write(f"your result is {result}")


with divide:
    divide = st.button("select for division")
    if divide:
        result = numberone/numbertwo
        st.write(f"your result is {result}")


  