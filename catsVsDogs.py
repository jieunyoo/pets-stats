import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt


st.title('Cats vs Dogs - Popularity!')

#image = Image.open('pet.png')

st.text('Data from 49 states')

#st.image(image)

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

#use slider values to populate data shown
st.text('Adjust the slider to show data for states that fall within your range of values')
values = st.slider(
     'Select a range of values for dogs',
     0.0, 100.0, (0.0, 50.0))
#st.write('Values:', values)

filtered_data = data[data['Percentage of Dog Owners'].between(values[0], values[1], inclusive=True)]

bottom = alt.Chart(filtered_data).mark_bar().encode(x=alt.X('Location:N'), y=alt.Y('Percentage of Dog Owners:Q'))
st.altair_chart(bottom,use_container_width=True)

#choose cat percentage values
st.text('Adjust the slider to show data for states that fall within your range of values')
valuesCat = st.slider(
     'Select a range of values for cats',
     0.0, 100.0, (0.0, 50.0))

filtered_dataCat = data[data['Percentage of Cat Owners'].between(valuesCat[0], valuesCat[1], inclusive=True)]

catChart = alt.Chart(filtered_dataCat).mark_bar().encode(x=alt.X('Location:N'), y=alt.Y('Percentage of Cat Owners:Q'))
st.altair_chart(catChart,use_container_width=True)

