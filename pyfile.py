import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel(io='supermarkt_sales.xlsx', engine='openpyxl', sheet_name='Sales',
                        skiprows=3, usecols='B:R', nrows=1000)

#st.write("""Welcome to Streamlit""")
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

st.dataframe(df)
