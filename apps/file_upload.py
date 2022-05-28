import os

import pandas as pd
import streamlit as st
from joblib import load

pwd = os.getcwd()
random_forest_model = os.path.join(pwd, "models/2022-05-28-17-13-16.pkl")
lstm_model = os.path.join(pwd, "models/LSTM-2022-05-28-19-43-27.pkl")


def app():
    with st.spinner("Loading Home ..."):
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if st.button("Predict"):
            if data_file is not None:
                file_details = {
                    "Filename": data_file.name,
                    "FileType": data_file.type,
                    "FileSize": data_file.size,
                }
                st.write(file_details)

                df = pd.read_csv(data_file)
                st.dataframe(df)

                random_forest = load(random_forest_model)
                lstm = load(lstm_model)

                st.write(random_forest.predict(df))
                # st.write(lstm.predict(df))
