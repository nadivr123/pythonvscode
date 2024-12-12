# A group of friends decided to spend a weekend organizing a community sports event. Each friend had $200 saved up, but they also earned extra money by selling tickets and refreshments at the event. Write a Python program to calculate how much each friend has left after organizing the event and earning from ticket sales.

# Start by defining the initial amount saved as saved_amount and set it to 200.

# Ask each friend how much they spent renting the sports venue and store it in venue_rental.
# Ask how much they spent on sports equipment for the event and store it in equipment_cost.

# Ask how much they spent on prizes for the winners and store it in prizes_cost.

# Ask how much they spent on refreshments for the players and spectators and store it in refreshments_cost.

# Ask how much they earned from selling event tickets and store it in ticket_sales.

# Ask how much they earned from selling refreshments during the event and store it in refreshments_sales.

# Calculate the total amount spent by adding up venue_rental, equipment_cost, prizes_cost, and refreshments_cost.

# Calculate the total amount earned by adding ticket_sales and refreshments_sales.

# Subtract the total amount spent from the sum of saved_amount and the total earnings to find the remaining balance.
# Use an if condition to check:

# If the remaining balance is positive, print how much money each friend has left.
# If the remaining balance is zero or negative, print that they spent more than they saved.
# Additionally, if any of the spending exceeds half of the saved_amount, print a warning message indicating they are spending too much on a single activity

import streamlit as st

saved_amount= 200

venue = st.number_input("How much money did you spend on renting the sports venue:")
equipment = st.number_input("How much money did you spend on sports equipment:")
prizes = st.number_input("How much money did you spend on prizes:")
refreshments_cost = st.number_input("How much did you spend on refreshments:")
tickets = st.number_input("How much did you earn from selling tickets:")
refreshments_sales = st.number_input("How much did you earn from selling refreshments:")

total_cost = venue+equipment+prizes+refreshments_cost
total_earned = tickets+refreshments_sales

total = saved_amount+total_earned-total_cost

if total >= 0:
    print("you have earned",total,"dollars")
    st.success("Great Job on making profit")
else:
    print("Sadly, you have spent more money than you saved")
    st.success("Better luck next time")