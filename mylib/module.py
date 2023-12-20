import streamlit as st
import pandas as pd
import numpy as pd
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

class myfunction():

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
    
    def tambah_parm(parm):
        parms = dict()
        # if parm == 'K Nears Neighbor':
        #     K = st.sidebar.slider('K', 1, 15)
        #     parms['K'] = K
        if parm == 'Support Vector Machine':
            C = st.sidebar.slider('C', 0.01, 10.0)
            parms['C'] = C
        elif parm == 'Neural Network':
            alpha = st.sidebar.slider('alpha', 0.001, 0.9)
            parms['alpha'] = alpha
        else:
            max_depth = st.sidebar.slider('max_depth', 2, 15)
            parms['max_depth'] = max_depth
            n_estimator = st.sidebar.slider('n_estimators', 1, 100)
            parms['n_estimators'] = n_estimator
        return parms
    
    def pilih_class(algorithm, params):
        algo = None
        # if algorithm == 'K Nears Neighbor':
        #     algo = KNeighborsClassifier(n_neighbors=params['K'])
        if algorithm == 'Support Vector Machine':
            algo = SVC(kernel='rbf', C=params['C'])
        elif algorithm == 'Neural Network':
            algo = MLPClassifier(alpha=params['alpha'], random_state=1234)
        else:
            algo = RandomForestClassifier(n_estimators=params['n_estimators'],
                                      max_depth=params['max_depth'], random_state=1234)
        return algo