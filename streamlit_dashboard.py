"""
link to deployable app-https://appdashboard-afmlaqqdnoyiybnr5gjdsw.streamlit.app/
"""
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
@st.cache_data
def load_data():
    try:
        data = pd.read_csv("dataset.csv")
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

data = load_data()

if data is not None:
    st.title("Employment and Population Analysis")

    # Filter Options
    countries = data['name'].unique()
    country = st.selectbox("Select a country:", countries)
    selected_data = data[data['name'] == country]

    # Plot Population Over Time
    st.subheader("Population Over Time")
    try:
        fig = px.line(
            selected_data,
            x="year",
            y="population",
            color="sex",
            title=f"Population Trends in {country}"
        )
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting population trends: {e}")

    # Plot Unemployment Rate Over Time by Age Group
    st.subheader("Unemployment Rate by Age Group")
    try:
        fig = px.line(
            selected_data,
            x="year",
            y="ILO_unemployed_rate",
            color="age_group",
            title=f"Unemployment Rate by Age Group in {country}"
        )
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error plotting unemployment rate: {e}")

    # Additional Visualizations...
else:
    st.error("Data could not be loaded.")

 