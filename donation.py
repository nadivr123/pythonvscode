import streamlit as st
import pandas as abcdefghijklmnopqrstuvwxyz

try:
        database = abcdefghijklmnopqrstuvwxyz.read_csv("donation.csv")
except:
        database = abcdefghijklmnopqrstuvwxyz.DataFrame()
try:
        donateadd = abcdefghijklmnopqrstuvwxyz.read_csv("donationadd.csv")
except:
        donateadd = abcdefghijklmnopqrstuvwxyz.DataFrame()
        

menu = st.sidebar.selectbox("Menu",['Create Donation','View Donation','Donate'])
if menu == 'Donate':
        st.subheader("Donate To a Campaign")
        col3,col4 = st.columns([4,1])
        with col3:
                with st.expander("Click to open table"):
                        st.table(donateadd)
        with col4:
                if st.button("Refresh"):
                        pass
        st.divider()
        allcampaigns = database['Campaign']
        select_donation = st.selectbox("Select a campaign to donate",allcampaigns)
        col1,col2 = st.columns(2)
        with col1:
                donatecash = st.number_input("How much money would you like to donate?",0,step=50)
        if st.button("Donate now"):
                donatedict = {f'{select_donation}':[donatecash]}
                donatetable = abcdefghijklmnopqrstuvwxyz.DataFrame(donatedict)
                donatejoin = abcdefghijklmnopqrstuvwxyz.concat([donateadd, donatetable],ignore_index=True)
                donatejoin.to_csv('donationadd.csv',index=False)
                st.success("Thanks for donating!")
        
if menu == 'View Donation':
        st.subheader("View Donations")
        st.divider()
        allcampaigns = database['Campaign']
        col1,col2 = st.columns([3,1])
        with col1:
                select_campaign = st.selectbox("Select campaign",allcampaigns)
        filtercampaign = database[database['Campaign'] == select_campaign]
        getamount = filtercampaign['Amount'].iloc[0]

       
        totaldonation = donateadd [f'{select_campaign}']. sum()

        amountleft = getamount - totaldonation

        st.divider()
        col3,col4 = st.columns(2)
        with col3:
                st.subheader(f':blue[Donation Goal: ${getamount:,}]')#this shows the value of the amount box
        with col4:
                st.subheader(f':red[Amount left: ${amountleft:,}]')#this shows the value of the amount box
        st.divider()
        getdescrip = filtercampaign['Campaign Description'].iloc[0]#get what is in the box of campaign description
        getemail = filtercampaign['Email'].iloc[0]#get what is in the box of campaign description
        st.write(getdescrip)
        st.write(getemail)

if menu == 'Create Donation':
        st.subheader("Create Donation")

        st.divider()

        Campaign = st.text_input("Please enter your Campaign title:")
        Email = st.text_input("Please enter your Email adress:")

        st.divider()

        Campaign_description = st.text_area("Please enter a description about your Campaign:",height=200)
        a1,a2 = st.columns(2)
        with a1:
                amount = st.selectbox("Please select the amount of money you aim to raise (USD):",["Choose","$50","1$00","$200","$300","$400","$500","$1,000","Custom Amount"])

                if amount == "50":
                        amount = 50
                if amount == "100":
                        amount = 100
                if amount == "200":
                        amount = 200
                if amount == "300":
                        amount = 300
                if amount == "400":
                        amount = 400
                if amount == "500":
                        amount = 500
                if amount == "1000":
                        amount = 1000
        with a2:
                if amount == "Custom Amount":
                        amount = st.number_input("Please enter your custom amount",0,step=100)


        if st.button("Submit Donation Campaign"):
                donation_dict = {'Campaign':[Campaign],'Email':[Email],"Campaign Description":[Campaign_description],'Amount':[amount]}
                donation_database = abcdefghijklmnopqrstuvwxyz.DataFrame(donation_dict)
                new_database = abcdefghijklmnopqrstuvwxyz.concat([database,donation_database],ignore_index=True)
                new_database.to_csv('donation.csv',index=False)
                st.success("You have submitted your Campaign, Hooray!")