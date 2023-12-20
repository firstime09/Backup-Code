import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO
from mylib.module import myfunction
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mf = myfunction()
st.title("Streamlit Test")
st.write("""Machine Learning Classifier""")

# uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=True,)
uploaded_file = st.sidebar.file_uploader("Choose a xlsx file")
if uploaded_file is not None:
    df0 = pd.ExcelFile(uploaded_file)
    df1 = pd.read_excel(df0)
    st.dataframe(df1)

dataSet = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine Dataset",
                                          "Supermarket Sales"))

className = st.sidebar.selectbox("Select Classifier", ("K Nears Neighbor", "Support Vector Machine", "Random Forest",
                                                       "Neural Network"))

x, y = mf.dtFrame(dataSet)
st.write("Shape of data", x.shape)
st.write("Number of class", len(np.unique(y)))

params = mf.tambah_parm(className)
algo = mf.pilih_class(className, params)

X_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)

algo = algo.fit(X_train, y_train)
y_pred = algo.predict(x_test)

acc = accuracy_score(y_test, y_pred)
st.write(f'Algoritma = {algo}')
st.write(f'Akurasi = ', acc)