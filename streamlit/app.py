import streamlit as st
import pandas as pd 
import numpy as np

# title of the app
st.title('hello streamlit')

# display a simple text
st.write('this is a simple text')

# creating a df 
df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
})

# then display this new df
st.write('here is the dataframe')
st.write(df)

# create a line char

chart_data = pd.DataFrame(
    np.random.randn(20,3), 
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)