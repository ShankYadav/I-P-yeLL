import streamlit as st
import pandas as pd
import random
import os

st.set_page_config(page_title='iIi.pPp.eL')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

if 'count' not in st.session_state:
    st.session_state.count = 0
    
def increment_counter():
    st.session_state.count += 1

player_db = pd.read_csv('IPL_Data.csv')
cols = ['Name','Team','Type','Born','National Side','Batting Style','Bowling','MatchPlayed']

df = pd.DataFrame(player_db,columns = cols)
df = df.sort_values(by=['Name'])
df = df.fillna(0)

tmp = [[0, 'nan'], ['West Indies', 'WI'], ['India', 'IND'], ['Afghanistan', 'AFG'], ['Bangladesh', 'BAN'], ['England', 'ENG'], ['Australia', 'AUS'], ['Sri Lanka', 'SL'], ['New Zealand', 'NZ'], ['South Africa', 'SA'], ['Singapore', 'SIN']]
for i in tmp:
    df.loc[df["National Side"] == i[0], "National Side"] = i[1]

p_name = random.choice(df['Name'])

f = open("rand_player.txt","a")
f.write(p_name)
f.write(',')
f.close()

f = open("rand_player.txt", "r")
data = f.read()
data = data.split(',')
data = data[0]
f.close()

player_name = data

def details(cols,player_name):
    player_arr = []
    for i in cols:
        if i == 'Born':
            data = df.loc[df['Name'] == player_name, i].iloc[0]
            if data != 0:
                data = data.split(' ')
                data = data[2] 
            player_arr.append(data)
        else:
            player_arr.append(df.loc[df['Name'] == player_name, i].iloc[0])
    player_arr[7] = int(player_arr[7])
    return player_arr

player_arr = details(cols,player_name)


def add_data(data):
    f = open("playerdb.txt", "a")
    f.write(data) 
    f.write(',')
    f.close()

def fetch_players():
    f = open("playerdb.txt", "r")
    data = f.read()
    data = data.split(',')
    data = data[:-1]
    f.close()
    return data

def fetch_data():
    players = fetch_players()
    player_details = []
    for i in players:
        player_details.append(details(cols, i))
    return player_details

st.title('I.P.eL \U0001F3CF')

st.subheader('Rules : ')
st.write('1) The matches indicate the number of IPL matches played prior to 2023 IPL.')
st.write('2) The green color indicates a correct guess.')
st.write('3) The red color indicates a wrong guess.')
st.write('4) The color blue indicates that the number is lesser than the expected guess.')
st.write('5) The color orange indicates that the number is greater than the expected guess.')
st.write('6) You will have 6 guesses to guess.')
st.write('7) Good luck :smile:')
option = st.selectbox('Enter your guess: ',(df['Name'].values))

count = st.session_state.count 

c = st.columns([6,1.1,3.75,1,1.2,4,6,0.5])

flag = 0

ws = "<div><span class='highlight red'>"
cs = "<div><span class='highlight green'>"
ls = "<div><span class='highlight orange'>"
gs = "<div><span class='highlight blue'>"
be = "</span></div>"

if st.button('Enter',on_click = increment_counter) and count <= 6 :
    add_data(option)
    data = fetch_data()
    with c[0]:
        st.write('Name')
        st.subheader('---------------')
    with c[1]:
        st.write('Team')
        st.subheader('-')
    with c[2]:
        st.write('Role')
        st.subheader('-------')
    with c[3]:
        st.write('DOB')
        st.subheader('-')
    with c[4]:
        st.write('From')
        st.subheader('-')
    with c[5]:
        st.write('Bat')
        st.subheader('-----------')
    with c[6]:
        st.write('Bowl')
        st.subheader('---------------')
    with c[7]:
        st.write('Matches')
        st.subheader('-')
    for i in data:
        name,team,role,year,coun,batt,bowl,mchs = [i[x] for x in range(8)]
        arr = [i[x] for x in range(8)]
        
        with c[0]:
            if player_arr[0]==name:
                flag=1
                st.markdown(cs+name+be, unsafe_allow_html=True)
            else:
                st.markdown(ws+name+be, unsafe_allow_html=True)
            st.write('--------')
            
        with c[1]:
            if player_arr[1]==team:
                team = str(team)
                st.markdown(cs+team+be, unsafe_allow_html=True)
            else:
                st.markdown(ws+team+be, unsafe_allow_html=True)
            st.write('--------')
        with c[2]:
            if player_arr[2]==role:
                role = str(role)
                st.markdown(cs+role+be, unsafe_allow_html=True)
            else:
                st.markdown(ws+role+be, unsafe_allow_html=True)
            st.write('--------')
        with c[3]:
            year = int(year)
            player_arr[3] = int(player_arr[3])
            if (year - player_arr[3]) > 0:
                st.markdown(gs+str(year)+be, unsafe_allow_html=True)
            elif (year - player_arr[3]) < 0:
                st.markdown(ls+str(year)+be, unsafe_allow_html=True)
            else:
                st.markdown(cs+str(year)+be, unsafe_allow_html=True)
            st.write('--------')
        with c[4]:
            if player_arr[4]==coun:
                coun = str(coun)
                st.markdown(cs+coun+be, unsafe_allow_html=True)
            else:
                st.markdown(ws+coun+be, unsafe_allow_html=True)
            st.write('--------')
        with c[5]:
            if player_arr[5]==batt:
                batt = str(batt)
                st.markdown(cs+batt+be, unsafe_allow_html=True)
            else:
                st.markdown(ws+batt+be, unsafe_allow_html=True)
            st.write('--------')
        with c[6]:
            if player_arr[6]==bowl:
                bowl = str(bowl)
                st.markdown(cs+bowl+be, unsafe_allow_html=True)
            else:
                st.markdown(ws+bowl+be, unsafe_allow_html=True)
            st.write('--------')
        with c[7]:
            if (mchs - player_arr[7]) > 0:
                st.markdown(gs+str(mchs)+be, unsafe_allow_html=True)
            elif (mchs - player_arr[7]) < 0:
                st.markdown(ls+str(mchs)+be, unsafe_allow_html=True)
            else:
                st.markdown(cs+str(mchs)+be, unsafe_allow_html=True)
            st.write('--------')           
            
if count > 6:
    st.markdown(cs+'The Correct Player was '+player_arr[0]+be, unsafe_allow_html=True)
    st.markdown(ws+'Maximum tries done :('+be, unsafe_allow_html=True)
    st.markdown(ws+'Reset for a new game'+be, unsafe_allow_html=True)
 
if st.button('Reset'):
    st.session_state.count = 0
    st.write('Reset Done')
    st.write('Press enter your new guess')
    os.remove('playerdb.txt')
    os.remove("rand_player.txt")
    
if flag==1:
    st.markdown(cs+'You are correct!!! Kudos!!!'+be, unsafe_allow_html=True)
    st.write('Reset to play again :smile:')

