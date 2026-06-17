import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)

data = pd.read_csv("data/streaming_data.csv")

st.title("Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    fig_views = px.histogram(
        data,
        x="views",
        nbins=20,
        title="Views Distribution"
    )

    fig_views.update_layout(height=350)

    st.plotly_chart(
        fig_views,
        use_container_width=True
    )

with col2:
    fig_likes = px.histogram(
        data,
        x="likes",
        nbins=20,
        title="Likes Distribution"
    )

    fig_likes.update_layout(height=350)

    st.plotly_chart(
        fig_likes,
        use_container_width=True
    )

fig_engagement = px.histogram(
    data,
    x="engagement_score",
    nbins=20,
    title="Engagement Score Distribution"
)

fig_engagement.update_layout(height=400)

st.plotly_chart(
    fig_engagement,
    use_container_width=True
)

st.subheader("Feature Correlation")

corr = data.corr(numeric_only=True)

fig_corr = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig_corr,
    use_container_width=True
)