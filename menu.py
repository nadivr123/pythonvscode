import streamlit as st

st.set_page_config(layout="wide")

menu = st.sidebar.selectbox("menu",["appetizers","drinks","main course","desserts"])

total = 0

if menu == "appetizers":

    a1,a2,a3,a4 = st.columns(4)
    with  a1:
        st.image("https://preventionrd.com/wp-content/uploads/2009/12/frenchfries11.jpg",width=100)
        if st.checkbox("french fries: $15"):
            st.success("You have added french fries")
            total += 15
        st.image("https://www.jessicagavin.com/wp-content/uploads/2023/01/BBQ-chicken-wings-21-1200.jpg",width=130)
        if st.checkbox("Chicken wings: 20"):
            st.success("You have added chicken wings")
            total += 20

    with a2:
        st.image("https://silkroadrecipes.com/wp-content/uploads/2022/02/Naan-Bread-Recipe-square.jpg",width=130)
        if st.checkbox("cheese truffle naan: $25"):
            st.success("You have added cheese truffle naan")
            total += 25
        st.image("https://cfassets.mackenzieltd.com/media/catalog/product/cache/12394f6f0687fad6511d210db21c0192/a/-/a-395-01.png",width=130)
        if st.checkbox("soft shell crab: $30"):
            st.success("you have added soft shell crab")
            total += 30

    with a3:
        st.image("https://iambaker.net/wp-content/uploads/2019/07/chili-cheese-nacho-final.jpg",width=125)
        if st.checkbox("nachos: $15"):
            st.success("You have added nachos")
            total += 15
        st.image("https://spicysouthernkitchen.com/wp-content/uploads/Fried-Jalapeno-Popper-Bites-9.jpg",width=130)
        if st.checkbox("jalapeno poppers: $20"):
            st.success("you have added jalapeno poppers")
            total += 20

    with a4:
        st.image("https://assets.kraftfoods.com/recipe_images/opendeploy/187029_640x428.jpg",width=195)
        if st.checkbox("asparagus: $15"):
            st.success("You have added asparagus")
            total += 15

if menu == "drinks":
   
    b1,b2,b3,b4 = st.columns(4)
    with b1:
       st.image("https://www.unitedsweets.co.nz/cdn/shop/products/Products_2_1080x.png?v=1613011954",width=110)
       if st.checkbox("Fanta: $10"):
           st.success("you have added fanta")
           total += 10
       st.image("https://www.pepsi.com/en-us/refresh082123/images/social/PEPSI_2023_PR_WCPZS_Cans.png",width=110)
       if st.checkbox("Pepsi: $10"):
           st.success("you have added Pepsi")
           total += 10
    with b2:
       st.image("https://previews.agefotostock.com/previewimage/medibigoff/053b8c3cf801e4d2bc7e6b4cd6150a1a/zon-10797227.jpg",width=90)
       if st.checkbox("coca cola: $10"):
           st.success("you have added coca cola")
           total += 10
       st.image("https://corkfinewines.ca/cdn/shop/collections/Red-Wine-category_1346x250.png?v=1611355555",width=110)
       if st.checkbox("red wine: $30"):
           st.success("you have added red wine ")
           total += 30
    with b3:
       st.image("https://www.deliciousmagazine.co.uk/wp-content/uploads/2023/04/2023D100_COCKTAIL_DOUZEPOINTS__-copy.jpg",width=90)
       if st.checkbox("cocktail: $25 "):
           st.success("you have added cocktail")
           total += 25
       st.image("https://image.made-in-china.com/2f0j00YnoVWUcGhKge/Glass-Cup-Beer-Mug-with-Handle-for-Drinking-in-Large-Capacity.jpg",width=110)
       if st.checkbox("beer: $15"):
           st.success("you have added beer")
           total += 15
    with b4:
       st.image("https://www.eatingwell.com/thmb/HYGXDhl0d1uO79Ezfk85rhO9ZRo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8223457-57737d937322479d84c7135c3edd925d.jpg", width=110)
       if st.checkbox("orange juice: $10"):
           st.success("you have added orange juice")
           total = +10
       st.image("https://assets.bonappetit.com/photos/62cdd8cedc3e934b224d8fb5/1:1/w_2560%2Cc_limit/0712-paloma-lede.jpg",width=110)
       if st.checkbox("paloma: $25"):
           st.success("you have added paloma")
           total= +25

if menu == "main course":
    
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        st.image("https://cdn.jwplayer.com/v2/media/TZ9cm2sk/poster.jpg?width=720",width=150)
        if st.checkbox("steak: $80"):
           st.success("you have added steak")
           total= +80
        st.image("https://moorlandseater.com/wp-content/uploads/2018/12/caesar-salad-moorlands-eater-183714.jpg",width=110)
        if st.checkbox("salad: $30"):
            st.success("you have added salad")
            total= +30
    with c2:
        st.image("https://skinnyspatula.com/wp-content/uploads/2022/10/Creamy_Garlic_Chicken_Pasta_0-735x735.jpg",width=110)
        if st.checkbox("pasta: 35"):
            st.success("you have added pasta")
            total= +35
        st.image("https://static.toiimg.com/thumb/53110049.cms?width=1200&height=900",width=150)
        if st.checkbox("pizza: $35"):
            st.success("you have added pizza")
            total= +35