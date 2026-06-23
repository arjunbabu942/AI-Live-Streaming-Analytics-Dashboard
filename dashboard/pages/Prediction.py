import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    layout="wide"
)

model = joblib.load("models/engagement_model.pkl")

st.title("Engagement Prediction")

# =====================================
# MANUAL PREDICTION
# =====================================

st.subheader("Manual Prediction")

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

    st.metric(
        "Predicted Engagement Score",
        f"{prediction[0]:.2f}"
    )

st.divider()

# =====================================
# CSV PREDICTION
# =====================================

st.subheader("Batch Prediction Using CSV")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    required_columns = [
        "views",
        "watch_time",
        "likes",
        "comments",
        "shares",
        "retention_rate"
    ]

    if all(col in data.columns for col in required_columns):

        predictions = model.predict(
            data[required_columns]
        )

        data["predicted_engagement_score"] = predictions

        st.success(
            "Predictions generated successfully!"
        )

        st.dataframe(
            data.head(),
            use_container_width=True
        )

        csv = data.to_csv(index=False)

        st.download_button(
            label="Download Prediction Results",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )

    else:

        st.error(
            "CSV must contain: views, watch_time, likes, comments, shares, retention_rate"
        )