import streamlit as st
import webbrowser
import pandas as pd

menu = st.sidebar._selectbox("Menu",["Video Categories","Video Ratings"])

countlink = "videoratings.csv"

try:
     viewcounts = pd.read_csv(countlink)
except:
     viewcounts = pd.DataFrame()
st.table(viewcounts)

if menu == "Video Categories":
    videocat = st.sidebar.pills("Choose Videos",['All','Educational','Football Quiz','Basketball','Entertainment','Top Movies','Space','Animals'],default = 'All')
    

if videocat == 'All' or videocat == 'Educational':
        st.subheader("Educational Category")

        e1, e2, e3, e4 = st.columns(4)
        
        with e1:
            st.image("https://i.ytimg.com/vi/Twn_4AW0M6U/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAZbYfyCqE5UbWgl1_MJXjEnuhYKQ")
            st.write("My Rock, Paper, Scissors Robot Never Loses (+9 Other Cool Inventions)")
            if st.button("Play Video",key = "1"):
                     webbrowser.open('https://www.youtube.com/watch?v=Twn_4AW0M6U')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,'My Rock, Paper, Scissors Robot Never Loses (+9 Other Cool Inventions)'] +=1
                     except:
                          viewcounts.loc[0,'My Rock, Paper, Scissors Robot Never Loses (+9 Other Cool Inventions)'] =1
                     viewcounts.to_csv(countlink, index=False)
    
            with e2:
                st.image("https://i.ytimg.com/vi/Rsxao9ptdmI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCyngdiLGiInFCVDHZOSCXmpL_wSw")
                st.write("Beating 5 Scam Arcade Games with Science (I Won Them All)")
                if st.button("Play Video",key = "2"):
                     webbrowser.open('https://www.youtube.com/watch?v=Rsxao9ptdmI')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,'Beating 5 Scam Arcade Games with Science (I Won Them All)'] +=1
                     except:
                          viewcounts.loc[0,'Beating 5 Scam Arcade Games with Science (I Won Them All)'] =1
                     viewcounts.to_csv(countlink, index=False)

            with e3:
                st.image("https://i.ytimg.com/vi/Kou7ur5xt_4/maxresdefault.jpg")
                st.write("World's Largest Elephant Toothpaste Experiment")
                if st.button("Play Video",key = "3"):
                     webbrowser.open('https://www.youtube.com/watch?v=Kou7ur5xt_4')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"World's Largest Elephant Toothpaste Experiment"] +=1
                     except:
                          viewcounts.loc[0,"World's Largest Elephant Toothpaste Experiment"] =1
                     viewcounts.to_csv(countlink, index=False)
                     
            with e4:
                st.image("https://i.ytimg.com/vi/3c584TGG7jQ/maxresdefault.jpg`")
                st.write("EXPLODING Glitter Bomb 4.0 vs. Package Thieves")
                if st.button("Play Video",key = "4"):
                     webbrowser.open('https://www.youtube.com/watch?v=3c584TGG7jQ')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"EXPLODING Glitter Bomb 4.0 vs. Package Thieves"] +=1
                     except:
                          viewcounts.loc[0,"EXPLODING Glitter Bomb 4.0 vs. Package Thieves"] =1
                     viewcounts.to_csv(countlink, index=False)


if videocat == 'All' or videocat == 'Football Quiz':
        st.subheader("Football Quiz Category")

        f1, f2, f3, f4 = st.columns(4)
        
        with f1:
            st.image("https://i.ytimg.com/vi/f51pCsDIF0I/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCHUtFCI08NczBELEzN3Vgcad4b4g")
            st.write("GUESS THE NATIONAL TEAM BY PLAYERS CLUB - SEASON 2024/2025 | FOOTBALL QUIZ 2024")
            if st.button("Play Video",key = "5"):
                     webbrowser.open('https://www.youtube.com/watch?v=f51pCsDIF0I')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"GUESS THE NATIONAL TEAM BY PLAYERS CLUB - SEASON 2024/2025 | FOOTBALL QUIZ 2024"] +=1
                     except:
                          viewcounts.loc[0,"GUESS THE NATIONAL TEAM BY PLAYERS CLUB - SEASON 2024/2025 | FOOTBALL QUIZ 2024"] =1
                     viewcounts.to_csv(countlink, index=False)


    
            with f2:
                st.image("https://i.ytimg.com/vi/1vK3n2gKMzM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBQaEPFAHG6_j-8NfILmr9WfWo26w")
                st.write("GUESS THE PLAYER BY COUNTRY + CLUB + JERSEY NUMBER + POSITION")
                if st.button("Play Video",key = "6"):
                     webbrowser.open('https://www.youtube.com/watch?v=1vK3n2gKMzM')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"GUESS THE PLAYER BY COUNTRY + CLUB + JERSEY NUMBER + POSITION"] +=1
                     except:
                          viewcounts.loc[0,"GUESS THE PLAYER BY COUNTRY + CLUB + JERSEY NUMBER + POSITION"] =1
                     viewcounts.to_csv(countlink, index=False)

            with f3:
                st.image("https://i.ytimg.com/vi/YLA1Rb5-f38/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAIxBJ7hqNpAu5ATkC8NLXjp6UOFw")
                st.write("GUESS THE PLAYER BY THEIR TRANSFERS - SEASON 2024/2025 | FOOTBALL QUIZ 2024")
                if st.button("Play Video",key = "7"):
                     webbrowser.open('https://www.youtube.com/watch?v=YLA1Rb5-f38')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"GUESS THE PLAYER BY THEIR TRANSFERS - SEASON 2024/2025 | FOOTBALL QUIZ 2024"] +=1
                     except:
                          viewcounts.loc[0,"GUESS THE PLAYER BY THEIR TRANSFERS - SEASON 2024/2025 | FOOTBALL QUIZ 2024"] =1
                     viewcounts.to_csv(countlink, index=False)
            
            with f4:
                st.image("https://i.ytimg.com/vi/rrbUsY5IAnk/maxresdefault.jpg")
                st.write("I BET YOU CANT GUESS THE TWO FACES OF MERGED PLAYERS | FOOTBALL QUIZ 2024")
                if st.button("Play Video",key = "8"):
                     webbrowser.open('https://www.youtube.com/watch?v=rrbUsY5IAnk')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I BET YOU CANT GUESS THE TWO FACES OF MERGED PLAYERS | FOOTBALL QUIZ 2024"] +=1
                     except:
                          viewcounts.loc[0,"I BET YOU CANT GUESS THE TWO FACES OF MERGED PLAYERS | FOOTBALL QUIZ 2024"] =1
                     viewcounts.to_csv(countlink, index=False)

if videocat == 'All' or videocat == 'Space':
        st.subheader("Space Category")

        s1, s2, s3, s4 = st.columns(4)
        
        with s1:
            st.image("https://i.ytimg.com/vi/pjaN2WHAHVo/maxresdefault.jpg")
            st.write("14 Minutes of Mind-Blowing Space Facts! | With Astrophysicist Brian Cox")
            if st.button("Play Video",key = "9"):
                     webbrowser.open('https://www.youtube.com/watch?v=pjaN2WHAHVo')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"14 Minutes of Mind-Blowing Space Facts! | With Astrophysicist Brian Cox"] +=1
                     except:
                          viewcounts.loc[0,"14 Minutes of Mind-Blowing Space Facts! | With Astrophysicist Brian Cox"] =1
                     viewcounts.to_csv(countlink, index=False)

    
            with s2:
                st.image("https://i.ytimg.com/vi/dSgP3J4fD6U/maxresdefault.jpg")
                st.write("15 Minutes of SUPER Unbelievable and EXTREMELY Fascinating Space Facts")
                if st.button("Play Video",key = "10"):
                     webbrowser.open('https://www.youtube.com/watch?v=dSgP3J4fD6U')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"15 Minutes of SUPER Unbelievable and EXTREMELY Fascinating Space Facts"] +=1
                     except:
                          viewcounts.loc[0,"15 Minutes of SUPER Unbelievable and EXTREMELY Fascinating Space Facts"] =1
                     viewcounts.to_csv(countlink, index=False)

            with s3:
                st.image("https://i.ytimg.com/vi/Vb2ZXRh74WU/maxresdefault.jpg")
                st.write("StoryBots Outer Space | Planets, Sun, Moon, Earth and Stars | Fun Learning")
                if st.button("Play Video",key = "11"):
                     webbrowser.open('https://www.youtube.com/watch?v=Vb2ZXRh74WU')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"StoryBots Outer Space | Planets, Sun, Moon, Earth and Stars | Fun Learning"] +=1
                     except:
                          viewcounts.loc[0,"StoryBots Outer Space | Planets, Sun, Moon, Earth and Stars | Fun Learning"] =1
                     viewcounts.to_csv(countlink, index=False)
            
            with s4:
                st.image("https://i.ytimg.com/vi/uD4izuDMUQA/maxresdefault.jpg")
                st.write("TIMELAPSE INTO THE FUTURE: A Journey going on till the End of Time (4K)")
                if st.button("Play Video",key = "12"):
                     webbrowser.open('https://www.youtube.com/watch?v=uD4izuDMUQA')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"TIMELAPSE INTO THE FUTURE: A Journey going on till the End of Time (4K)"] +=1
                     except:
                          viewcounts.loc[0,"TIMELAPSE INTO THE FUTURE: A Journey going on till the End of Time (4K)"] =1
                     viewcounts.to_csv(countlink, index=False)

if videocat == 'All' or videocat == 'Basketball':
        st.subheader("Basketball Category")

        b1, b2, b3, b4 = st.columns(4)
        
        with b1:
            st.image("https://i.ytimg.com/vi/N8gfmUSHUaw/maxresdefault.jpg")
            st.write("I Hosted a 1v1 Creator Basketball Tournament For $10,000")
            if st.button("Play Video",key = "13"):
                     webbrowser.open('https://www.youtube.com/watch?v=N8gfmUSHUaw&t=1839s')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I Hosted a 1v1 Creator Basketball Tournament For $10,000"] +=1
                     except:
                          viewcounts.loc[0,"I Hosted a 1v1 Creator Basketball Tournament For $10,000"] =1
                     viewcounts.to_csv(countlink, index=False)

    
            with b2:
                st.image("https://i.ytimg.com/vi/7_bIoo3I5q4/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAkYosrKpL1a9Q7mhKEXM5nNTPHrA")
                st.write("I Made My Own AAU Team and This Happened...")
                if st.button("Play Video",key = "14"):
                     webbrowser.open('https://www.youtube.com/watch?v=7_bIoo3I5q4')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I Made My Own AAU Team and This Happened..."] +=1
                     except:
                          viewcounts.loc[0,"I Made My Own AAU Team and This Happened..."] =1
                     viewcounts.to_csv(countlink, index=False)

            with b3:
                st.image("https://i.ytimg.com/vi/2csLZGL4Mg8/maxresdefault.jpg")
                st.write("Creators Coach a 4v4 Basketball Tournament for $1000!")
                if st.button("Play Video",key = "15"):
                     webbrowser.open('https://www.youtube.com/watch?v=2csLZGL4Mg8&t=2425s')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Creators Coach a 4v4 Basketball Tournament for $1000!"] +=1
                     except:
                          viewcounts.loc[0,"Creators Coach a 4v4 Basketball Tournament for $1000!"] =1
                     viewcounts.to_csv(countlink, index=False)
            
            with b4:
                st.image("https://i.ytimg.com/vi/ivBhM8ytGvY/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBOojB-QhI15B1n3Z0txeDPjlv44g")
                st.write("1v1 Tournament for $10,000 GONE WRONG, BACKBOARD SHATTERS")
                if st.button("Play Video",key = "16"):
                     webbrowser.open('https://www.youtube.com/watch?v=Kpg2tM631xQ')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"1v1 Tournament for $10,000 GONE WRONG, BACKBOARD SHATTERS"] +=1
                     except:
                          viewcounts.loc[0,"1v1 Tournament for $10,000 GONE WRONG, BACKBOARD SHATTERS"] =1
                     viewcounts.to_csv(countlink, index=False)

if videocat == 'All' or videocat == 'Entertainment':
        st.subheader("Entertainment Category")

        n1, n2, n3, n4 = st.columns(4)
        
        with n1:
            st.image("https://i.ytimg.com/vi/MHUtv_nKtGU/maxresdefault.jpg")
            st.write("I Bought a $25,000 First Class Ticket to Japan! (Day 1)")
            if st.button("Play Video",key = "17"):
                     webbrowser.open('https://www.youtube.com/watch?v=MHUtv_nKtGU')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I Bought a $25,000 First Class Ticket to Japan! (Day 1)"] +=1
                     except:
                          viewcounts.loc[0,"I Bought a $25,000 First Class Ticket to Japan! (Day 1)"] =1
                     viewcounts.to_csv(countlink, index=False)
            
            st.image("https://i.ytimg.com/vi/8j5Vb3sqpuo/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCbdb3MWnx5uMIW6C1nFh-SH0a1aw")
            st.write("I Tried the Most Exclusive Restaurants in Japan! (Day 5)")
            if st.button("Play Video",key = "18"):
                     webbrowser.open('https://www.youtube.com/watch?v=8j5Vb3sqpuo')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I Tried the Most Exclusive Restaurants in Japan! (Day 5)"] +=1
                     except:
                          viewcounts.loc[0,"I Tried the Most Exclusive Restaurants in Japan! (Day 5)"] =1
                     viewcounts.to_csv(countlink, index=False)

    
            with n2:
                st.image("https://i.ytimg.com/vi/gtu6GhVOjdg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBFZD8KVYu_cLcuMgicPjdT5uz67w")
                st.write("Living Off ONLY Vending Machines in Japan for 24 Hours! (Day 2)")
                if st.button("Play Video",key = "19"):
                     webbrowser.open('https://www.youtube.com/watch?v=gtu6GhVOjdg&t=27s')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Living Off ONLY Vending Machines in Japan for 24 Hours! (Day 2)"] +=1
                     except:
                          viewcounts.loc[0,"Living Off ONLY Vending Machines in Japan for 24 Hours! (Day 2)"] =1
                     viewcounts.to_csv(countlink, index=False)

                st.image("https://i.ytimg.com/vi/doNjutURB08/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBkNV6kCle60s04-P86VIfrW6lMGg")
                st.write("I Went to Disneyland in Tokyo Japan and had SO much fun! (Day 6)")
                if st.button("Play Video",key = "20"):
                     webbrowser.open('https://www.youtube.com/watch?v=doNjutURB08')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I Went to Disneyland in Tokyo Japan and had SO much fun! (Day 6)"] +=1
                     except:
                          viewcounts.loc[0,"I Went to Disneyland in Tokyo Japan and had SO much fun! (Day 6)"] =1
                     viewcounts.to_csv(countlink, index=False)

            with n3:
                st.image("https://i.ytimg.com/vi/Ye9MOdEJUP4/maxresdefault.jpg")
                st.write("I Ate ONLY Convenience Store Food in Japan for 24 Hours! (Day 3)")
                if st.button("Play Video",key = "21"):
                     webbrowser.open('https://www.youtube.com/watch?v=Ye9MOdEJUP4&t=434s')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I Ate ONLY Convenience Store Food in Japan for 24 Hours! (Day 3)"] +=1
                     except:
                          viewcounts.loc[0,"I Ate ONLY Convenience Store Food in Japan for 24 Hours! (Day 3)"] =1
                     viewcounts.to_csv(countlink, index=False)

                st.image("https://i.ytimg.com/vi/et-G4Pq5TNY/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAy7rm_NMe26wu9QRxSyZ___uwG-g")
                st.write("My friends and I just got Kicked Out of Japan. (Day 7)")
                if st.button("Play Video",key = "22"):
                     webbrowser.open('https://www.youtube.com/watch?v=et-G4Pq5TNY')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"My friends and I just got Kicked Out of Japan. (Day 7)"] +=1
                     except:
                          viewcounts.loc[0,"My friends and I just got Kicked Out of Japan. (Day 7)"] =1
                     viewcounts.to_csv(countlink, index=False)
            
            with n4:
                st.image("https://th.bing.com/th?&id=OVF.2xInnRENsLgn%2BuYteBW2Rw&w=580&h=326&c=7&pid=1.7&rs=1")
                st.write("I Stayed at EVERY Weird Hotel in Japan and it was CRAZY! (Day 4)")
                if st.button("Play Video",key = "23"):
                     webbrowser.open('https://www.youtube.com/watch?v=ad_doKl8yWI')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"I Stayed at EVERY Weird Hotel in Japan and it was CRAZY! (Day 4)"] +=1
                     except:
                          viewcounts.loc[0,"I Stayed at EVERY Weird Hotel in Japan and it was CRAZY! (Day 4)"] =1
                     viewcounts.to_csv(countlink, index=False)

if videocat == 'All' or videocat == 'Top Movies':
        st.subheader("Best Movies Category")

        t1, t2, t3, t4 = st.columns(4)
        
        with t1:
            st.image("https://deadline.com/wp-content/uploads/2024/12/sonic3_Cb8f9IP.webp?w=681&h=383&crop=1")
            st.write("Sonic the Hedgehog 3 Movie 2024 ft. Jim Carrey, Keanu Reeves, Idris Elba")
            if st.button("Play Video",key = "24"):
                     webbrowser.open('https://www.youtube.com/watch?v=bvrNZejEWzA')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Sonic the Hedgehog 3 Movie 2024 ft. Jim Carrey, Keanu Reeves, Idris Elba"] +=1
                     except:
                          viewcounts.loc[0,"Sonic the Hedgehog 3 Movie 2024 ft. Jim Carrey, Keanu Reeves, Idris Elba"] =1
                     viewcounts.to_csv(countlink, index=False)
    
            with t2:
                st.image("https://w0.peakpx.com/wallpaper/711/573/HD-wallpaper-avengers-endgame-2019-official-poster-avengers-endgame-avengers-end-game-poster-movies-2019-movies-iron-man-thanos-captain-america-captain-marvel-ant-man-black-widow-rocket-raccoon-hawkeye.jpg")
                st.write("Avengers END GAME Thanos, Thor, Iron Man, Captain America, Black Widow")
                if st.button("Play Video",key = "25"):
                     webbrowser.open('https://www.youtube.com/watch?v=BbvS7H08GIo')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Avengers END GAME Thanos, Thor, Iron Man, Captain America, Black Widow"] +=1
                     except:
                          viewcounts.loc[0,"Avengers END GAME Thanos, Thor, Iron Man, Captain America, Black Widow"] =1
                     viewcounts.to_csv(countlink, index=False)

            with t3:
                st.image("https://www.framerated.co.uk/frwpcontent/uploads/2018/02/blackpanther01.jpg")
                st.write("Black Panther Full Movie 2018 4K HD | Chadwick Boseman, Letitia Wright, Michael B. Jordan")
                if st.button("Play Video",key = "26"):
                     webbrowser.open('https://www.youtube.com/watch?v=uCqUv9rm7-M')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Black Panther Full Movie 2018 4K HD | Chadwick Boseman, Letitia Wright, Michael B. Jordan"] +=1
                     except:
                          viewcounts.loc[0,"Black Panther Full Movie 2018 4K HD | Chadwick Boseman, Letitia Wright, Michael B. Jordan"] =1
                     viewcounts.to_csv(countlink, index=False)
            
            with t4:
                st.image("https://i.ytimg.com/vi/rHik0khkGTw/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCsF6HL2PqBUvMgnLH19P8j6qWZFA")
                st.write("Spider-Man: Far From Home Full Movie In English | New Hollywood Movie")
                if st.button("Play Video",key = "27"):
                     webbrowser.open('https://www.youtube.com/watch?v=rHik0khkGTw')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Spider-Man: Far From Home Full Movie In English | New Hollywood Movie"] +=1
                     except:
                          viewcounts.loc[0,"Spider-Man: Far From Home Full Movie In English | New Hollywood Movie"] =1
                     viewcounts.to_csv(countlink, index=False)

if videocat == 'All' or videocat == 'Animals':
        st.subheader("Animal Category")

        a1, a2, a3, a4 = st.columns(4)
        
        with a1:
            st.image("https://i.ytimg.com/vi/ajkkbAGpj5Q/maxresdefault.jpg")
            st.write("Big Cats for Kids - Animals for Kids - Lion, Tiger, Leopard, Jaguar and more")
            if st.button("Play Video",key = "28"):
                     webbrowser.open('https://www.youtube.com/watch?v=bvrNZejEWzA')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Big Cats for Kids - Animals for Kids - Lion, Tiger, Leopard, Jaguar and more"] +=1
                     except:
                          viewcounts.loc[0,"Big Cats for Kids - Animals for Kids - Lion, Tiger, Leopard, Jaguar and more"] =1
                     viewcounts.to_csv(countlink, index=False)

    
            with a2:
                st.image("https://i.ytimg.com/vi/gN0cpZytGos/maxresdefault.jpg")
                st.write("Amphibians for Kids | What is an amphibian? Learn the characteristics of amphibians")
                if st.button("Play Video",key = "29"):
                     webbrowser.open('https://www.youtube.com/watch?v=BbvS7H08GIo')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Amphibians for Kids | What is an amphibian? Learn the characteristics of amphibians)"] +=1
                     except:
                          viewcounts.loc[0,"Amphibians for Kids | What is an amphibian? Learn the characteristics of amphibians)"] =1
                     viewcounts.to_csv(countlink, index=False)

            with a3:
                st.image("https://i.ytimg.com/vi/zqsK0VhcL8o/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLB_Eb9CCAdOnw5zb3oYqq0uNjafqg")
                st.write("Mammals for Kids | Learn about the characteristics of mammals!")
                if st.button("Play Video",key = "30"):
                     webbrowser.open('https://www.youtube.com/watch?v=zqsK0VhcL8o')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"Mammals for Kids | Learn about the characteristics of mammals!"] +=1
                     except:
                          viewcounts.loc[0,"Mammals for Kids | Learn about the characteristics of mammals!"] =1
                     viewcounts.to_csv(countlink, index=False)
            
            with a4:
                st.image("https://i.ytimg.com/vi/buCrh_Qka9M/maxresdefault.jpg")
                st.write("This is Where Every and I mean EVERY Dog Breed Came From and Originated From")
                if st.button("Play Video",key = "31"):
                     webbrowser.open('https://www.youtube.com/watch?v=buCrh_Qka9M')
                     st.write('Clicked')
                     try:
                          viewcounts.loc[0,"This is Where Every and I mean EVERY Dog Breed Came From and Originated From"] +=1
                     except:
                          viewcounts.loc[0,"This is Where Every and I mean EVERY Dog Breed Came From and Originated From"] =1
                     viewcounts.to_csv(countlink, index=False)

