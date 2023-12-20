import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="| Home",
        page_icon="👋",)
    st.write("# Summary")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        I am a computer science lecturer at Universitas Bunda Mulia (UBM) with 5+ years of
        experience in teaching and research. The research topics I cover include Optimization,
        Image Processing, Expert Systems, Machine Learning, and Artificial Intelligence.
        The conclusions of all of my research are published in internationally accredited
        journals, national journals, or conferences and hope to be feedback for review,
        replicated, or applied in an organization. Some demo systems that have been created
        can be **viewed on the sidebar 👈**
        
        ### Whare you can find me?
        - in my publication [Google scholar](https://scholar.google.com/citations?user=LxbIO5sAAAAJ)
        - in my code documentation [Github](https://github.com/firstime09)
        - in my social media [LinkedIn](https://id.linkedin.com/in/felliks-feiters-tampinongkol-100084174)
        
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """)

if __name__ == "__main__":
    run()