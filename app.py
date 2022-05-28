import streamlit as st

from apps import file_upload, home_page
from multiapp import MultiApp

# from apps import dataset_display, insight, predict_query, prediction_display


app = MultiApp()

st.sidebar.header("Pharmaceutical Sales forcasting")
st.sidebar.write(
    "The aim of this project is to predict the sales six weeks ahead across all the stores of the Rossman Pharmaceutical company using Machine and Deep Learning. The different factors affecting the sales are: promotions, competitions, school-state holiday, seasonality, and locality."
)

# Add all your application here
app.add_app("Home page", home_page.app)
app.add_app("File page", file_upload.app)
# app.add_app("Data sets", dataset_display.app)
# app.add_app("Insights", insight.app)
# app.add_app("Predicting page", predict_query.app)
# app.add_app("Prediction display", prediction_display.app)
# The main app
app.run()
