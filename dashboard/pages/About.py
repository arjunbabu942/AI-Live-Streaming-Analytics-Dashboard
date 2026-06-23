import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide"
)

st.title("About Project")

st.markdown("""
## AI-Powered Live Streaming Analytics Dashboard

The AI-Powered Live Streaming Analytics Dashboard is a machine learning-based system designed to analyze streaming performance and predict audience engagement.

The platform helps content creators, streamers, and analysts understand key performance metrics and make data-driven decisions to improve audience interaction and stream effectiveness.
""")

st.divider()

# =====================================
# PROJECT OBJECTIVES
# =====================================

st.subheader("Project Objectives")

st.write("""
- Analyze streaming performance metrics
- Predict viewer engagement using Machine Learning
- Visualize streaming statistics through interactive dashboards
- Identify patterns affecting stream performance
- Provide actionable recommendations for improvement
""")

st.divider()

# =====================================
# KEY FEATURES
# =====================================

st.subheader("Key Features")

st.write("""
- Interactive Analytics Dashboard
- Engagement Score Prediction
- Data Visualization and Insights
- Correlation Analysis
- Dataset Exploration
- Recommendation System
""")

st.divider()

# =====================================
# TECHNOLOGY STACK
# =====================================

st.subheader("Technology Stack")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("Python")

with col2:
    st.success("Pandas")

with col3:
    st.success("Scikit-Learn")

with col4:
    st.success("Streamlit")

st.write("")

col5, col6 = st.columns(2)

with col5:
    st.success("Plotly")

with col6:
    st.success("NumPy")

st.divider()

# =====================================
# MACHINE LEARNING MODEL
# =====================================

st.subheader("Machine Learning")

st.write("""
### Learning Type

Supervised Learning

### Algorithm

Linear Regression

### Input Features

- Views
- Watch Time
- Likes
- Comments
- Shares
- Retention Rate

### Predicted Output

- Engagement Score
""")

st.divider()

# =====================================
# BENEFITS
# =====================================

st.subheader("Benefits")

st.write("""
This system enables:

- Better understanding of audience behavior
- Improved content strategy
- Higher viewer retention
- Increased audience engagement
- Data-driven decision making
""")

st.divider()

st.success("AI-Powered Live Streaming Analytics Dashboard")