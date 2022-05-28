import pandas as pd
import streamlit as st


def app():
    with st.spinner("Loading Home ..."):
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if st.button("Process"):
            if data_file is not None:
                file_details = {
                    "Filename": data_file.name,
                    "FileType": data_file.type,
                    "FileSize": data_file.size,
                }
                st.write(file_details)

                df = pd.read_csv(data_file)
                st.dataframe(df)
