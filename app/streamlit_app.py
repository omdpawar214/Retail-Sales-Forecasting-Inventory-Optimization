import streamlit as st
import pandas as pd

st.title("📊 Retail Sales Forecast Dashboard")

try:
    df = pd.read_csv("outputs/predictions.csv")

    st.success("Data loaded successfully!")

    st.subheader("🔍 Predictions Data")
    st.dataframe(df.head())

    st.subheader("📈 Actual vs Predicted Sales")

    # FIXED LINE
    st.line_chart(df[['Actual', 'Predicted']])

    st.subheader("📦 Inventory Status Distribution")
    st.bar_chart(df['Inventory_Status'].value_counts())

except FileNotFoundError:
    st.error("❌ predictions.csv not found. Please run main.py first.")
except Exception as e:
    st.error("⚠️ Something went wrong:")
    st.write(e)