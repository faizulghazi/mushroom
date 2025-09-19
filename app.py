import streamlit as st
import plotly.express as px
import pandas as pd

mushroom_df = pd.read_csv("mushroom_data.csv")

# Example: assuming mushroom_df is already loaded
fig = px.line(mushroom_df, x="timestamp", y="temperature_C", 
              title="Temperature Over Time")

# Display in Streamlit

st.plotly_chart(fig, use_container_width=True)
