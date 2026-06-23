import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Live Streaming Analytics Dashboard",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

if "uploaded_data" in st.session_state:

    data = st.session_state["uploaded_data"]

    st.success("Using uploaded dataset")

else:

    data = pd.read_csv("data/streaming_data.csv")

# =====================================
# HERO SECTION
# =====================================

st.markdown("""
<div style="
padding:30px;
border-radius:15px;
background:linear-gradient(135deg,#1E293B,#0F172A);
text-align:center;
">

<h1 style="color:white;">
AI Live Streaming Analytics Dashboard
</h1>

<h3 style="color:#94A3B8;">
Analyze Streaming Performance Using Machine Learning
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# KPI CARDS
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Streams",
        len(data)
    )

with col2:
    st.metric(
        "Average Views",
        f"{int(data['views'].mean()):,}"
    )

with col3:
    st.metric(
        "Average Likes",
        f"{int(data['likes'].mean()):,}"
    )

with col4:

    if "engagement_score" in data.columns:

        st.metric(
            "Average Engagement",
            f"{int(data['engagement_score'].mean()):,}"
        )

    elif "predicted_engagement_score" in data.columns:

        st.metric(
            "Average Engagement",
            f"{int(data['predicted_engagement_score'].mean()):,}"
        )

    else:

        st.metric(
            "Average Engagement",
            "N/A"
        )

st.divider()

# =====================================
# PROJECT OVERVIEW
# =====================================

st.subheader("Project Overview")

st.write("""
This dashboard helps streamers and streaming platforms:

• Analyze audience behavior

• Predict engagement using Machine Learning

• Improve viewer retention

• Increase audience interaction

• Make data-driven decisions
""")

st.divider()

# =====================================
# TECHNOLOGY STACK
# =====================================

st.subheader("Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.info("Python")

with tech2:
    st.info("Pandas")

with tech3:
    st.info("Scikit-Learn")

with tech4:
    st.info("Streamlit")

st.divider()

# =====================================
# DATA SOURCE
# =====================================

st.subheader("Current Data Source")

if "uploaded_data" in st.session_state:

    st.success("Using Uploaded Dataset")

else:

    st.info("Using Default Dataset")