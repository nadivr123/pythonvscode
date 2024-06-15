# """-add a restaurant title
# -Add a restaurant picture
# -Show them the food selections
# -After they choose/select their meals, show them the total amount
# -Ask if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill"""



import streamlit as st
import pandas as pd

database = pd.read_csv('resteraunt.csv')
st.dataframe(database,use_container_width=True)

st.title("No Pay No Eat Restaurant")

st.image("https://img.freepik.com/free-photo/grilled-sirloin-steak-rustic-wood-table-generated-by-ai_188544-22501.jpg?w=2000")

total = 0

st.subheader("We have these meals available. Pick your choice")

if st.checkbox("Spaghetti and Sauce: $50"):
    st.write("You have added Spaghetti and Sauce")
    total += 50

if st.checkbox("sirloin steak: $150"):
    st.write("You have added sirloin steak")
    total += 150

if st.checkbox("salmon: $80"):
    st.write("You have added Salmon")
    total += 80

if st.checkbox("creme brulee: $100"):
    st.write("You have added creme brulee")
    total += 100

if st.checkbox("pepporoni pizza: $70"):
    st.write("You have added pizza")
    total += 70

if st.checkbox("Fanta: $20"):
    st.write("You have added fanta")
    total += 20

if st.checkbox("coca cola: $25"):
    st.write("You have added coca cola")
    total += 25

if st.checkbox("sprite: $20"):
    st.write("You have added sprite")
    total += 20

if st.checkbox("cocktail: $50"):
    st.write("You have added cocktail")
    total += 50

if st.checkbox("french fries: $25"):
    st.write("You have added french fries")
    total += 25

if st.checkbox("egg fried rice: $40"):
    st.write("You have added egg fried rice")
    total += 40

if st.checkbox("butter chicken: $40"):
    st.write("You have added butter chicken")
    total += 40

if st.checkbox("cheese truffle naan: $30"):
    st.write("You have added cheese truffle naan")
    total += 30

if st.checkbox("ice cream cone: $10"):
    st.write("You have added ice cream")
    total += 10

if st.button("cost"):
    resteraunt_dict = {'Total':[total]}
    resteraunt_database = pd.DataFrame(resteraunt_dict)
    new_database = pd.concat([database,resteraunt_database],ignore_index=True)
    new_database.to_csv('resteraunt.csv',index=False)
    st.success(f"your final total is {total}")

if st.checkbox("click to share bill with others"):
    people = st.slider("how many people in total: ",2,20,value = 2)
    person = total/people
    st.write("each person has to pay",person,"dollars")

#Restaurant update test
#Create a csv file with a database that 
#when you click the show bill button, it saves the user total bill

