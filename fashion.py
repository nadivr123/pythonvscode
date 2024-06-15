import streamlit as st
st.set_page_config(layout = "wide")
bill= 0
st.title("Clothing store")

st.image("https://cdn.pixabay.com/photo/2016/11/22/19/08/hangers-1850082_1280.jpg")


st.header("mens categories") 

men1,men2,men3,men4 = st.columns(4)

with men1:
    st.subheader("legwear")
    if st.checkbox("pants: $35"):
     bill = +35
     st.success("added to list")
    if st.checkbox("shorts: $30"):
     bill = +30
     st.success("added to list")
    if st.checkbox("jeans: $30"):
     bill = +30
     st.success("added to list")
    if st.checkbox("track pants: $40"):
      bill = + 40


with men2:
    st.subheader("Winter Wear")
    if st.checkbox("hoodie: $40"):
     bill = +40
     st.success("added to list")
    if st.checkbox("jacket: $35"):
     bill = +35
     st.success("added to list")
    if st.checkbox("scarf: $30"):
      bill = +30
      st.success("added to list")
    if st.checkbox("mittens: $25"):
      bill = +25
      st.success("added to list")

with men3:
    st.subheader("summer wear")
    if st.checkbox("T - shirt: $35"):
     bill = +35
     st.success("added to list")
    if st.checkbox("swimwear = $50"):
     bill = +50
     st.success("added to list")
    if st.checkbox("sandals: $30"):
      bill = +30
      st.success("added to list")
    if st.checkbox("flip flops: $25"):
      bill = +25
      st.success("added to list")

with men4:
    st.subheader("watches")
    if st.checkbox("rolex = $300"):
        bill = + 300
        st.success("added to list")
    if st.checkbox(''):
      pass


if st.button("cost"):
    st.subheader(f'Your total bill is {bill}') #explain f-string next class
