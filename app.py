import streamlit as st

from apps import file_upload, home_page
from multiapp import MultiApp

app = MultiApp()

st.sidebar.header("Pharmaceutical Sales forcasting")
st.sidebar.write(
    "The aim of this project is to predict the sales six weeks ahead across all the stores of the Rossman Pharmaceutical company using Machine and Deep Learning. The different factors affecting the sales are: promotions, competitions, school-state holiday, seasonality, and locality."
)

# Add all your application here
app.add_app("Home page", home_page.app)
app.add_app("File page", file_upload.app)

# The main app
app.run()
