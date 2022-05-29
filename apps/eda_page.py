import os

import pandas as pd
import streamlit as st

pwd = os.getcwd()
train_file_path = os.path.join(pwd, "data/train.csv")
store_file_path = os.path.join(pwd, "data/store.csv")


def app():
    st.title("Insights")

    df_train = pd.read_csv(
        train_file_path, dtype={"StateHoliday": object}, parse_dates=["Date"]
    )
    df_store = pd.read_csv(store_file_path)

    df_train_store = pd.merge(df_train, df_store, how="left", on="Store")

    df_train_store_copy = df_train_store.copy()

    st.write(
        f'Rossmann has {df_train_store_copy["Store"].nunique()} stores across 6 different locations'
    )

    st.subheader("Distribution")

    st.image(
        "charts/distributions.png",
        caption="Promotion distribution in the train and test set",
    )

    st.subheader("Promotion")

    st.image(
        "charts/monthly-sales.png",
        caption="Monthly sales across stores with promotions",
    )

    st.subheader("Sales")

    st.image(
        "charts/avg-monthly-sales.png",
        caption="Average monthly sales",
    )

    st.image(
        "charts/avg-weekly-sales.png",
        caption="Average weekly sales",
    )

    st.subheader("Sales and Customers")

    st.image(
        "charts/sale-customer-corr.png",
        caption="Sales and customers relationship",
    )

    st.subheader("Store Type Sales")

    st.image(
        "charts/daily-storetype-sales.png",
        caption="Average sales across different store types",
    )

    st.subheader("Store Assortment Sales")

    st.image(
        "charts/assortment-monthly-sales.png",
        caption="Average sales across different store assortments",
    )
