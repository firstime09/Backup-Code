import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets

st.title("Streamlit Test")
st.write("""Machine Learning Classifier""")

dataSet = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine Dataset",
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

def tambah_parm(parm):
    parms = dict()
    if parm == 'K Nears Neighbor':
        K = st.sidebar.slider('K', 1, 15)
        parms['K'] = K
    elif parm == 'Support Vector Machine':
        C = st.sidebar.slider('C', 0.01, 10.0)
        parms['C'] = C
    elif parm == 'Neural Network':
        epoch = st.sidebar.slider('epoch', 100, 300)
        parms['epoch'] = epoch
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        parms['max_depth'] = max_depth
        n_estimator = st.sidebar.slider('n_estimators', 1, 100)
        parms['n_estimators'] = n_estimator
    return parms

params = tambah_parm(className)

# def pilih_class(algorithm, params):
