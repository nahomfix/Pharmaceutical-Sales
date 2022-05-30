import streamlit as st

from apps import eda_page, file_upload, home_page
from multiapp import MultiApp

app = MultiApp()


st.sidebar.header("Pharmaceutical Sales forcasting")

# Add all your application here
app.add_app("Home page", home_page.app)
app.add_app("EDA page", eda_page.app)
app.add_app("Prediction page", file_upload.app)

# The main app
app.run()
