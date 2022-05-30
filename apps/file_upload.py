import os

import pandas as pd
import streamlit as st
from joblib import load

pwd = os.getcwd()
random_forest_model = os.path.join(pwd, "models/2022-05-30-19-29-52.pkl")
lstm_model = os.path.join(pwd, "models/LSTM-2022-05-28-19-43-27.pkl")


def app():
    data_file = st.file_uploader("Upload CSV", type=["csv"])
    if data_file is not None:
        file_details = {
            "File Name": data_file.name,
            "File Type": data_file.type,
            "File Size": data_file.size,
        }

        st.write(file_details)

        df = pd.read_csv(data_file)
        st.dataframe(df)

        if st.button("Predict"):
            random_forest = load(random_forest_model)
            # lstm = load(lstm_model)

            predicted = random_forest.predict(df)

            pd.DataFrame({"Sales": predicted})

            st.dataframe(predicted)
            # st.write(lstm.predict(df))
