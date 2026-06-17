import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Live Streaming Analytics",
    page_icon="",
    layout="wide"
)

data = pd.read_csv("data/streaming_data.csv")

st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(135deg,#1E293B,#0F172A);
text-align:center;
">

<h1 style="color:white;">
AI Live Streaming Analytics Dashboard
</h1>

<h3 style="color:#94A3B8;">
AI-Powered Viewer Engagement Insights
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Total Streams",
        len(data)
    )

with col2:
    st.metric(
        "Average Views",
        int(data["views"].mean())
    )

with col3:
    st.metric(
        "Average Likes",
        int(data["likes"].mean())
    )

with col4:
    st.metric(
        "Average Engagement",
        int(data["engagement_score"].mean())
    )

st.divider()

st.subheader("Project Overview")

st.write("""
This dashboard analyzes streaming performance and predicts viewer engagement using Machine Learning.

### Features

- Streaming Analytics
- Machine Learning Prediction
- Recommendations Engine
- Interactive Charts
- Dataset Explorer
""")