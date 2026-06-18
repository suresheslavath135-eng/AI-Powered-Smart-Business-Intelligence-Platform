
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

df = pd.read_csv("sales_data_sample.csv")

model = joblib.load("model.pkl")
st.set_page_config(
    page_title="Smart Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Business Intelligence Platform")

st.markdown(
"""
### AI-Powered Business Analytics Dashboard
"""
)

st.sidebar.title(
    "Navigation"
)

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Business Insights",
        "Sales Prediction",
        "AI Assistant"
    ]
)

if page == "Dashboard":

    st.header(
        "Executive KPI Dashboard"
    )



    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Revenue",
        "$10.03M"
    )

    col2.metric(
        "Orders",
        "307"
    )

    col3.metric(
        "Customers",
        "92"
    )

    col4.metric(
        "Countries",
        "19"
    )

    st.subheader("Monthly Revenue Trend")

    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

    monthly_sales = (
        df.groupby(
            df["ORDERDATE"].dt.to_period("M")
        )["SALES"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(10,5))

    monthly_sales.plot(ax=ax)

    ax.set_title("Monthly Revenue Trend")

    st.pyplot(fig)

        st.subheader("Revenue by Product Line")

    product_revenue = (
        df.groupby("PRODUCTLINE")["SALES"]
        .sum()
        .sort_values(ascending=False)
    )

    fig2, ax2 = plt.subplots(figsize=(10,5))

    product_revenue.plot(
        kind="bar",
        ax=ax2
    )

    ax2.set_title(
        "Revenue by Product Line"
    )

    st.pyplot(fig2)

        st.subheader("Top Countries by Revenue")

    country_revenue = (
        df.groupby("COUNTRY")["SALES"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig3, ax3 = plt.subplots(figsize=(10,5))

    country_revenue.plot(
        kind="bar",
        ax=ax3
    )

    ax3.set_title(
        "Top Countries by Revenue"
    )

    st.pyplot(fig3)

    elif page == "Business Insights":

    st.header("Business Insights")

    country_revenue = (
        df.groupby("COUNTRY")["SALES"]
        .sum()
        .sort_values(ascending=False)
    )

    product_revenue = (
        df.groupby("PRODUCTLINE")["SALES"]
        .sum()
        .sort_values(ascending=False)
    )

    customer_revenue = (
        df.groupby("CUSTOMERNAME")["SALES"]
        .sum()
        .sort_values(ascending=False)
    )

    st.subheader("Top Market")
    st.write(country_revenue.head(5))

    st.subheader("Top Product Lines")
    st.write(product_revenue.head(5))

    st.subheader("Top Customers")
    st.write(customer_revenue.head(5))

    elif page == "Sales Prediction":

    st.header("Sales Prediction")

    st.write("Sales Prediction Module Coming Soon")

    elif page == "AI Assistant":

    st.header("🤖 AI Business Assistant")

    question = st.text_input(
        "Ask a Business Question"
    )

    if question:

        q = question.lower()

        total_revenue = df["SALES"].sum()

        top_country = (
            df.groupby("COUNTRY")["SALES"]
            .sum()
            .idxmax()
        )

        top_customer = (
            df.groupby("CUSTOMERNAME")["SALES"]
            .sum()
            .idxmax()
        )

        top_product = (
            df.groupby("PRODUCTLINE")["SALES"]
            .sum()
            .idxmax()
        )

        if "revenue" in q:

            st.success(
                f"Total Revenue is ${total_revenue:,.2f}"
            )

        elif "country" in q:

            st.success(
                f"{top_country} is the highest revenue-generating country."
            )

        elif "customer" in q:

            st.success(
                f"{top_customer} is the top customer."
            )

        elif "product" in q:

            st.success(
                f"{top_product} is the best-performing product line."
            )

        elif "recommend" in q:

            st.success(
                "Focus on USA market and Classic Cars product line."
            )

        else:

            st.warning(
                "Try asking about revenue, country, customer, product, or recommendations."
            )
