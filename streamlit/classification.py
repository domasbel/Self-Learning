import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# here we describe the dataset that we want to load as initial one for training
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns = iris.feature_names)

    # adjusting the names for better readability of code 
    df.rename(columns={
        'sepal length (cm)': 'sep_len',
        'sepal width (cm)': 'sep_wid',
        'petal length (cm)': 'pet_len',
        'petal width (cm)': 'pet_wid'
    }, inplace=True)
    df['species'] = iris.target

    return df, iris.target_names

# we load the actual data that we will use for training
df, target_names = load_data()

# initialize the model that we want to use for this classification task
model = RandomForestClassifier()

# train the model on loaded data, excluding the target col and putting it as Y
model.fit(df.iloc[:, :-1], df['species'])

# here we are receiving the data from user that want to classify some instance
# after doing some simple eda we conclude which columns has to be filled in 
# sliders we can create as dynamical ones, since we have training data and anything outside those boarders would be not rational to 'predict'
# so in this case we create limits according to the datasets min and max points
st.sidebar.title('input features of the flower that is in centimeters')
sepal_length = st.sidebar.slider('sepal lenght in centimeters is:', float(df['sep_len'].min()), float(df['sep_len'].max()), float(df['sep_len'].median()))
sepal_width = st.sidebar.slider('sepal width in centimeters is:', float(df['sep_wid'].min()), float(df['sep_wid'].max()), float(df['sep_wid'].median()))
petal_length = st.sidebar.slider('petal lenght in centimeters is:', float(df['pet_len'].min()), float(df['pet_len'].max()), float(df['pet_len'].median()))
petal_witdh = st.sidebar.slider('petal width in centimeters is:', float(df['pet_wid'].min()), float(df['pet_wid'].max()), float(df['pet_wid'].median()))

# then we received data we put into a one line
input_data = [[sepal_length, sepal_width, petal_length, petal_witdh]]

# then we actually do the prediction on the trained model
prediction = model.predict(input_data)

# and then extract the name of the species 
predicted_species = target_names[prediction[0]]

st.write('Prediction')
st.write(f'The predicted species - {predicted_species}')