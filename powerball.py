import streamlit as st
import random
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup

# send a GET request
response = requests.get('https://www.powerball.com/')

# create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# find the tag : <span class='game-jackpot-number text-xxxl lh-1 text-center'
tag = soup.find('span', {'class': 'game-jackpot-number text-xxxl lh-1 text-center'})
date_tag = soup.find('h5', {'class': 'card-title mx-auto mb-3 lh-1 text-center title-date'})
cash_value_tag = soup.find('span', {'class': 'game-jackpot-number text-lg lh-1 text-center'})

# extract the content inside the tag
draw_date = date_tag.text
jackpot = tag.text
cash_tag = cash_value_tag.text

# display the draw date
st.sidebar.markdown(f"# Draw Date")
st.sidebar.write(f"{draw_date}")

# display the jackpot
st.sidebar.write(f"The current Powerball jackpot is {jackpot}")

# display cash value
st.sidebar.write(f"The current cash value is {cash_tag}")

def generate_powerball_numbers():
    numbers = random.sample(range(1, 70), 5)
    numbers.sort()
    powerball = random.randint(1, 26)
    return numbers, powerball


engine = create_engine('sqlite:///powerball_data.db')

st.sidebar.markdown("[Check Your Numbers](https://www.powerball.com/check-your-numbers)")

st.title("PowerBall Number Generator")
if st.button("Generate Numbers"):
    numbers, powerball = generate_powerball_numbers()
    st.write(f"Numbers: {numbers}")
    st.write(f"Powerball: {powerball}")
    date_time = datetime.now()
    numbers_str = ','.join(map(str, numbers))
    df_current = pd.DataFrame({'date_time': [date_time], 'numbers': [numbers_str], 'powerball': [powerball]})
    df_current.to_sql('powerball_numbers', con=engine, if_exists='append', index=False)
    df_updated = pd.read_sql('powerball_numbers', con=engine)
    df_updated['numbers'] = df_updated['numbers'].apply(lambda x: list(map(int, x.split(','))))
    st.session_state.df = df_updated

# Display dataframe and delete buttons for each row
if 'df' in st.session_state:
    st.write(st.session_state.df)
    if not st.session_state.df.empty:
        selected_id = st.sidebar.selectbox('Select an ID to delete:', st.session_state.df.index)
        if st.button('Delete selected ID'):
            st.session_state.df = st.session_state.df.drop(selected_id)
            st.session_state.df = st.session_state.df.reset_index(drop=True)
            st.session_state.df.to_sql('powerball_numbers', con=engine, if_exists='replace', index=False)
            df_updated = pd.read_sql('powerball_numbers', con=engine)
            df_updated['numbers'] = df_updated['numbers'].apply(lambda x: list(map(int, x.split(','))))
            st.session_state.df = df_updated

#  button for deleting all entries
if st.button("Delete all entries"):
    st.session_state.df = st.session_state.df.iloc[0:0]
    st.session_state.df.to_sql('powerball_numbers', con=engine, if_exists='replace', index=False)
    df_updated = pd.read_sql('powerball_numbers', con=engine)
    df_updated['numbers'] = df_updated['numbers'].apply(lambda x: list(map(int, x.split(','))))
    st.session_state.df = df_updated