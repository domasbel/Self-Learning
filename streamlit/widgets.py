import streamlit as st
import pandas as pd

# title creating 
st.title('Streamlit headline')

# input variable is possible aswell
name = st.text_input('enter your name:')

if name:
    st.write(f'hello {name}')

# creating a slider
age = st.slider('select your age:', 0, 100, 25)
st.write(f'your age is {age}')

# creating a select box 
options = ['python', 'java', 'c']
choice = st.selectbox('Choose your favourite language:', options)
st.write(f'you have selected {choice}')

# writing and reading a new csv object
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write('This data set is present as a template')
st.write(df)

uploaded_file = st.file_uploader('choose a file to upload:', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)