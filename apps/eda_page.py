import streamlit as st


def app():
    st.title("Insights")

    st.write(f"Rossmann has 1115 stores across 6 different locations")

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
