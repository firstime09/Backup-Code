import streamlit as st

st.title("Hello World!")

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
 
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
