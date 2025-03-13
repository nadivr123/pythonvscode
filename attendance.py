import streamlit as st
import pandas as abcdefghijklmnopqrstuvwxyz
import pandas as pd

try:
    database = pd.read_csv("attendance.csv")
except:
    database = pd.DataFrame()

st.table (database)

studentname = st.text_input("Please enter the students full name:")
rolenumber = st.text_input("Please enter the students role number:")
tdp = st.text_input("Please enter the students total days present:")
tda = st.text_input("Please enter the students total days absent:")



if st.button ("check attendance"):
    student_dict = {'Student Name':[studentname],'Role Number':[rolenumber], 'Total Days Present':[tdp], 'Total Days Abscent':[tda]}
    student_table = pd.DataFrame (student_dict)
    # st.table (student_dict)
    new_database = pd.concat([database,student_table],ignore_index=True) # concat means to join database together
    new_database.to_csv('attendance.csv',index=False) #write/save the new_database to a csv file
    st.write ("this students full name was",studentname,",their role number was",rolenumber,",their total days present was",tdp,"and their total days abscent was",tda)










































# try:
#         database = abcdefghijklmnopqrstuvwxyz.read_csv("donation.csv")
# except:
#         database = abcdefghijklmnopqrstuvwxyz.DataFrame()
# try:
#         donateadd = abcdefghijklmnopqrstuvwxyz.read_csv("donationadd.csv")
# except:
#         donateadd = abcdefghijklmnopqrstuvwxyz.DataFrame()
        

# menu = st.sidebar.selectbox("Menu",['Create Donation','View Donation','Donate'])
# if menu == 'Donate':
#         st.subheader("Donate To a Campaign")
#         col3,col4 = st.columns([4,1])
#         with col3:
#                 with st.expander("Click to open table"):
#                         st.table(donateadd)
#         with col4:
#                 if st.button("Refresh"):
#                         pass
#         st.divider()
#         allcampaigns = database['Campaign']
#         select_donation = st.selectbox("Select a campaign to donate",allcampaigns)
#         col1,col2 = st.columns(2)
#         with col1:
#                 donatecash = st.number_input("How much money would you like to donate?",0,step=50)
#         if st.button("Donate now"):
#                 donatedict = {f'{select_donation}':[donatecash]}
#                 donatetable = abcdefghijklmnopqrstuvwxyz.DataFrame(donatedict)
#                 donatejoin = abcdefghijklmnopqrstuvwxyz.concat([donateadd, donatetable],ignore_index=True)
#                 donatejoin.to_csv('donationadd.csv',index=False)
#                 st.success("Thanks for donating!")
        
# if menu == 'View Donation':
#         st.subheader("View Donations")
#         st.divider()
#         allcampaigns = database['Campaign']
#         col1,col2 = st.columns([3,1])
#         with col1:
#                 select_campaign = st.selectbox("Select campaign",allcampaigns)
#         filtercampaign = database[database['Campaign'] == select_campaign]
#         getamount = filtercampaign['Amount'].iloc[0]

       
#         totaldonation = donateadd [f'{select_campaign}']. sum()

#         amountleft = getamount - totaldonation

#         st.divider()
#         col3,col4 = st.columns(2)
#         with col3:
#                 st.subheader(f':blue[Donation Goal: ${getamount:,}]')#this shows the value of the amount box
#         with col4:
#                 st.subheader(f':red[Amount left: ${amountleft:,}]')#this shows the value of the amount box
#         st.divider()
#         getdescrip = filtercampaign['Campaign Description'].iloc[0]#get what is in the box of campaign description
#         getemail = filtercampaign['Email'].iloc[0]#get what is in the box of campaign description
#         st.write(getdescrip)
#         st.write(getemail)

# if menu == 'Create Donation':
#         st.subheader("Create Donation")

#         st.divider()

        
        
#         Campaign = st.text_input("Please enter your Campaign title:")
#         Email = st.text_input("Please enter your Email adress:")

#         st.divider()

#         Campaign_description = st.text_area("Please enter a description about your Campaign:",height=200)
#         a1,a2 = st.columns(2)
#         with a1:
#                 amount = st.selectbox("Please select the amount of money you aim to raise (USD):",["Choose","$50","1$00","$200","$300","$400","$500","$1,000","Custom Amount"])

#                 if amount == "50":
#                         amount = 50
#                 if amount == "100":
#                         amount = 100
#                 if amount == "200":
#                         amount = 200
#                 if amount == "300":
#                         amount = 300
#                 if amount == "400":
#                         amount = 400
#                 if amount == "500":
#                         amount = 500
#                 if amount == "1000":
#                         amount = 1000
#         with a2:
#                 if amount == "Custom Amount":
#                         amount = st.number_input("Please enter your custom amount",0,step=100)


#         if st.button("Submit Donation Campaign"):
#                 donation_dict = {'Campaign':[Campaign],'Email':[Email],"Campaign Description":[Campaign_description],'Amount':[amount]}
#                 donation_database = abcdefghijklmnopqrstuvwxyz.DataFrame(donation_dict)
#                 new_database = abcdefghijklmnopqrstuvwxyz.concat([database,donation_database],ignore_index=True)
#                 new_database.to_csv('donation.csv',index=False)
#                 st.success("You have submitted your Campaign, Hooray!")











# database = pd.read_csv("scores.csv") # used to read everything in the csv fine

# menu = st.sidebar.selectbox("menu",["submit score","database/chart","Student File"])
# st.sidebar.image("Tee.png")
# st.sidebar.write("**Made By Nadiv DE ROZARIO**")
# studentID = 'Student_'+str(len(database)+1)

# if menu == "submit score":

#     st.title("Student Grades")

#     name = st.text_input("Enter the students name: ")

#     c1,c2 = st.columns(2)

#     with c1:
#         math = st.number_input("Enter the students math semester grade: ",1,7)
#         english = st.number_input("Enter the students english semester grade; ",1,7)
#         science = st.number_input("Enter the students science semester grade: ",1,7)
#     with c2:
#         hum = st.number_input("Enter the students humanities semester grade:",1,7)
#         art = st.number_input("Enter the students art semester grade: ",1,7)
#         tech = st.number_input("Enter the students tech semester grade: ",1,7)

#     total = hum + art + science + english + math + tech
#     avg = int(total/6)

#     if avg == 7:
#         grade = "A+"
#     elif avg == 6:
#         grade = "A"
#     elif avg == 5:
#         grade = "B+"
#     elif avg == 4:
#         grade = "B"
#     elif avg == 3:
#         grade = "C"
#     elif avg <= 2:
#         grade = "F"
#         #Name,Math,Science,English,Humanities,Art,Total,Average,Grade
#     if st.button("Submit student scores"):
#         student_dict = {'StudentID':[studentID],'Name':[name], 'Math':[math], 'Science':[science], 'English':[english], 'Humanities':[hum], 'Art':[art], 'Tech':[tech],
#                     'Total':[total], 'Average':[avg], 'Grade':[grade]}
#         student_database = pd.DataFrame(student_dict)
#         #i created a dictionary of csv columns:python variable,
#         # then converted it to a dataframe (table)
#         # st.dataframe(student_database)
#         new_database = pd.concat([database,student_database],ignore_index=True) # concat means to join database together
#         new_database.to_csv('scores.csv',index=False) #write/save the new_database to a csv file
#         st.success(f"{name}'s total score is {total}, {name}'s average is {avg}, {name}'s final grade is {grade}")


# #Math,Science,English,Humanities,Art,Tech
# if menu == "database/chart":
#     st.table(database) # to show the data in a table
#     subject = ['Math','English','Humanities','Science','Art','Tech']
#     subjecttable = database[subject].mean().reset_index()
#     subjectrename = subjecttable.rename(columns={'index':'Subject',0:'Grade'})
#     chart = st.radio("choose the type of graph/chart you want:",['bar graph','pie chart'],horizontal=True)
#     if chart == 'bar graph':
#         barchart = px.bar(subjectrename, x='Subject',y='Grade')
#         st.plotly_chart(barchart)
#     elif chart == 'pie chart':
#         piechart = px.pie(subjectrename, names='Subject',values='Grade')
#         st.plotly_chart(piechart)

# if menu == "Student File":
#     header1, header2, header3 = st.columns(3)

#     with header1:
#         st.subheader("Find Student file")
#         findID = st.text_input("Enter Student ID")
#         find = st.button("Find Student")

#     if find:
#         if findID:
#             searchresult = database[database['StudentID'].str.lower() == findID.lower()]
#             st.table(searchresult)
            
#             getname = searchresult['Name'].iloc[0]
#             getmath = searchresult['Math'].iloc[0]
#             geteng = searchresult['English'].iloc[0]
#             gethum = searchresult['Humanities'].iloc[0]
#             getsci = searchresult['Science'].iloc[0]
#             getart = searchresult['Art'].iloc[0]
#             gettech = searchresult['Tech'].iloc[0]
#             getgrade = searchresult['Grade'].iloc[0]

#             h1, h2, h3 = st.columns([1,4,1])
#             with h2:
#                 st.title(":red[TEMITAYO COLLEGE]")
#                 sub1, sub2, sub3 = st.columns([1,4,1])
#                 with sub2:
#                     st.write("INTERNATIONAL SCHOOL")
#             st.divider()