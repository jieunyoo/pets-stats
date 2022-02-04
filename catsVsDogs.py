import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt


st.title('Cats vs Dogs - Popularity!')

image = Image.open('pet.png')

st.text('Data from 49 states')

st.image(image)

DATA_URL = ('https://raw.githubusercontent.com/jieunyoo/pets-stats/main/catsvdogs.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(50)
data_load_state.text("Done loading data")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


chart = alt.Chart(data).mark_bar().encode(x=alt.X('Location:N'), y=alt.Y('Percentage of Dog Owners:Q'))
st.altair_chart(chart,use_container_width=True)


catChart = alt.Chart(data).mark_bar().encode(x=alt.X('Location:N'), y=alt.Y('Percentage of Cat Owners:Q'))
st.altair_chart(catChart,use_container_width=True)

