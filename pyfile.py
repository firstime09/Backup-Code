import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets

st.title("Streamlit Test")
st.write("""Machine Learning Classifier""")

dataSet = st.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine Dataset",
                                          "Supermarket Sales"))

className = st.sidebar.selectbox("Select Classifier", ("K Nears Neighbor", "Support Vector Machine", "Random Forest",
                                                       "Neural Network"))
# st.write(dataSet)

def dtFrame(dataSet):
    if dataSet == "Iris":
        data = datasets.load_iris()
    elif dataSet == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    x = data.data
    y = data.target
    return x, y

x, y = dtFrame(dataSet)
st.write("Shape of data", x.shape)
st.write("Number of class", len(np.unique(y)))