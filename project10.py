#Liam is an enthusiastic football fan and wants to enhance his game-day experience by purchasing various items. He plans to buy match tickets, a season pass, team merchandise, snacks, and even subscribe to a premium sports channel. Write a Python program to help Liam calculate the total cost of his football adventure.

#Liam’s journey through the football shopping spree involves several steps:

#Match Ticket Purchase:

#Liam needs to purchase match tickets, which cost $100 each.
# Account Login:

# Liam will log in to his account using his username and password.
# Season Pass Selection:

# Liam can choose one of the following season passes:
# Standard Pass for $200
# VIP Pass for $500
# Team Merchandise:

# Liam can browse through various team merchandise:
# Jersey for $60
# Scarf for $30
# Hat for $20
# Snacks Purchase:

# Liam can buy snacks for the match:
# Popcorn for $10
# Hotdog for $15
# Soda for $5
# Premium Sports Channel Subscription:

# Liam can subscribe to a premium sports channel:
# Monthly subscription for $20
# Annual subscription for $200
# Total Calculation:

# After making his selections, Liam wants to see the total cost of his football adventure.
import streamlit as st

st.title("Manchester Derby match")
st.image("https://i.pinimg.com/originals/b5/09/71/b509716b7517f890dc248bcd63294de1.jpg")

total = 0

username = st.text_input("Please enter your username")
password = st.text_input("Please enter your password")

if username and password:
    ticket = st.radio("How many football tickets would you like to buy, each one is $100",["1","2","3","4","5","6"],horizontal=True)

    if ticket == "1":
        st.success("Thank you for purchasing 1 ticket")
        total += 100
    elif ticket == "2":
        st.success("Thank you for purchasing 2 tickets")
        total += 200
    elif ticket == "3":
        st.success("Thank you for purchasing 3 tickets")
        total += 300
    elif ticket == "4":
        st.success("Thank you for purchasing 4 tickets")
        total += 400
    elif ticket == "5":
        st.success("Thank you for purchasing 5 tickets")
        total += 500
    elif ticket == "6":
        st.success("Thank you for purchasing 6 tickets")
        total += 600

    member = st.radio("Whould you like to buy a membership",["yes","no"],horizontal=True)

    if member == "yes":
        membership = st.radio("Which membership would you like to buy",["Standard: $200","VIP: $500"],horizontal=False)
        if membership == "Standard: $200":
            st.success("Thank you for buying the standard membership")
            total += 200
        elif membership == "VIP: $500":
            st.success("Thank you for buying the VIP membership")
            total += 500

    elif member == "no":
        st.write("Its okay if you dont want to buy a membership")


    merchandise = st.radio("Whould you like to buy some merchandise, options are",["Jersey: $60","Hat: $20"],horizontal=False)

    if merchandise == "Jersey: $60":
        st.success("Thank you for buying a jersey")
        total += 60
    elif merchandise == "Hat: $20":
        st.success("Thank you for buying a hat")
        total += 20

    snacks = st.radio("Whould you like to buy some snacks, options are",["Popcorn: $10","Hotdog: $15","Soda: $10"],horizontal=False)

    if snacks == "Popcorn: $10":
        st.success("Thank you for buying popcorn")
        total += 10
    elif snacks == "Hotdog: $15":
        st.success("Thank you for buying a hotdog")
        total += 15
    elif snacks == "Soda: $10":
        st.success("Thank you for buying soda")
        total += 10

    tv = st.radio("Whould you like to subscribe to a sports channel?",["yes","no"])

    if tv == "yes":
        subscribe = st.radio("Which channel whould you like to subscribe to",["Sky Sports: $200","Fly Sports: $50"],horizontal=True)
        if subscribe == "Sky Sports: $200":
            st.write("Thank you for subscribing to Sky Sports")
            total += 200
        elif subscribe == "Fly Sports: $50":
            st.write("Thank you for subscribing to Fly Sports")
            total += 50
    elif tv == "no":
        st.write("Its okay if you dont want to subbscribe to a channel")

    if st.button("show total"):
        st.write("your total cost for everything is",total)