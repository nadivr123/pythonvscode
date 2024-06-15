import streamlit as st

st.set_page_config(layout='wide')

furniture = st.sidebar.selectbox("furntiture",['Home funiture','Office furniture','School funtiture',"Mr. Mikes's furniture"])

total = 0

if furniture == "Home furniture":

    a1,a2,a3 = st.columns(3)
    with a1:
        st.image("https://ak1.ostkcdn.com/images/products/is/images/direct/596c3493c573155241b18a43624af6b445fcb52a/Modern-U-Shaped-Sofa-Bed-3-Pieces-Removable-Ottomans-Couch-for-Living-Room.jpg",width=150)
        if st.checkbox("Sofa $4000 HKD, (to expensive for Mr. Mike)"):
            st.success("you have added Sofa, 'congratulations for being richer than Mr. Mike'")
            total += 4000

        st.image("https://images.thdstatic.com/productImages/66a53215-e861-4280-84af-6d5924557e5d/svn/white-golden-coffee-tables-yymd-ca-16-64_600.jpg",width=150)
        if st.checkbox("Coffee Table $1500 HKD, (to expensive for Mr. Mike)"):
            st.success("you have added Coffee table, 'congratulations for being richer than Mr. Mike'")
            total += 1500

    with a2:
        st.image("https://5.imimg.com/data5/SELLER/Default/2021/1/PP/UY/FT/49551708/1610608524710.jpg",width=150)
        if st.checkbox("Bed $5000 HKD, (to expensive for Mr. Mike)"):
            st.success("you have added Bed, 'congratulations for being richer than Mr. Mike'")
            total += 5000

        st.image("https://www.furnitureworld.co.uk/images/products/standard/6872_29331.jpg?t=1658414591",width=150)
        if st.checkbox("Wardrobe $2500 HKD, (to expensive for Mr. Mike)"):
            st.success("you have added Wardrobe, 'congratulations for being richer than Mr. Mike'")
            total += 2500
