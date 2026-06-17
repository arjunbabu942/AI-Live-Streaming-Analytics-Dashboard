import streamlit as st
import joblib

model = joblib.load("models/engagement_model.pkl")
col1, col2 = st.columns(2)

with col1:
    views = st.number_input(
        "Views",
        min_value=0,
        value=5000
    )

    watch_time = st.number_input(
        "Watch Time",
        min_value=0,
        value=15000
    )

    likes = st.number_input(
        "Likes",
        min_value=0,
        value=800
    )

with col2:
    comments = st.number_input(
        "Comments",
        min_value=0,
        value=200
    )

    shares = st.number_input(
        "Shares",
        min_value=0,
        value=100
    )

    retention_rate = st.number_input(
        "Retention Rate",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

if st.button("Predict Engagement Score"):

    prediction = model.predict([[
        views,
        watch_time,
        likes,
        comments,
        shares,
        retention_rate
    ]])

    predicted_score = prediction[0]

    st.success(
        f"Predicted Engagement Score: {predicted_score:.2f}"
    )

    st.subheader("Recommendations")

    if retention_rate < 60:
        st.warning(
            "Retention rate is low. Improve content quality and audience interaction."
        )

    if comments < 100:
        st.warning(
            "Encourage viewers to comment more during the stream."
        )

    if shares < 50:
        st.warning(
            "Promote content sharing to increase reach."
        )

    if likes < 500:
        st.warning(
            "Encourage viewers to like the stream."
        )

    if (
        retention_rate >= 75
        and likes >= 500
        and comments >= 100
    ):
        st.success(
            "Excellent engagement performance."
        )