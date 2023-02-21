import streamlit as st
import pandas as pd


st.title("Streamlit Test")
st.write("""Machine Learning Classifier""")

dataSet = st.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine Dataset",
                                          "Supermarket Sales"))

className = st.sidebar.selectbox("Select Classifier", ("K Nears Neighbor", "Support Vector Machine", "Random Forest",
                                                       "Neural Network"))
# st.write(dataSet)
