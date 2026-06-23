import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
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

    st.info("Using default dataset")

# =====================================
# PAGE TITLE
# =====================================

st.title("Streaming Analytics Dashboard")

st.write(
    "Comprehensive analysis of streaming performance metrics."
)

# =====================================
# KPI OVERVIEW
# =====================================

st.subheader("Performance Overview")

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
        "Average Retention",
        f"{data['retention_rate'].mean():.1f}%"
    )

with col4:
    if "engagement_score" in data.columns:
        st.metric(
            "Average Engagement",
            f"{int(data['engagement_score'].mean()):,}"
        )
    else:
        st.metric(
            "Average Engagement",
            "N/A"
        )

st.divider()

# =====================================
# DISTRIBUTION CHARTS
# =====================================

st.subheader("Distribution Analysis")

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

# =====================================
# ENGAGEMENT DISTRIBUTION
# =====================================

if "engagement_score" in data.columns:

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

# =====================================
# RELATIONSHIP ANALYSIS
# =====================================

if "engagement_score" in data.columns:

    st.subheader("Relationship Analysis")

    fig_scatter = px.scatter(
        data,
        x="views",
        y="engagement_score",
        size="likes",
        color="retention_rate",
        title="Views vs Engagement Score"
    )

    fig_scatter.update_layout(height=500)

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

# =====================================
# CORRELATION HEATMAP
# =====================================

st.subheader("Correlation Analysis")

corr = data.corr(numeric_only=True)

fig_heatmap = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Feature Correlation Heatmap"
)

st.plotly_chart(
    fig_heatmap,
    use_container_width=True
)

# =====================================
# KEY INSIGHTS
# =====================================

st.subheader("Key Insights")

highest_views = int(data["views"].max())

avg_retention = round(
    data["retention_rate"].mean(),
    2
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        f"Highest Views Recorded: {highest_views:,}"
    )

if "engagement_score" in data.columns:

    highest_engagement = int(
        data["engagement_score"].max()
    )

    with col2:
        st.info(
            f"Highest Engagement Score: {highest_engagement:,}"
        )

with col3:
    st.info(
        f"Average Retention Rate: {avg_retention}%"
    )

st.divider()

# =====================================
# ANALYTICS REPORT
# =====================================

st.subheader("Analytics Report")

report_data = {
    "Metric": [
        "Total Streams",
        "Average Views",
        "Average Likes",
        "Average Retention"
    ],
    "Value": [
        len(data),
        round(data["views"].mean(), 2),
        round(data["likes"].mean(), 2),
        round(data["retention_rate"].mean(), 2)
    ]
}

if "engagement_score" in data.columns:

    report_data["Metric"].extend([
        "Average Engagement",
        "Highest Engagement"
    ])

    report_data["Value"].extend([
        round(data["engagement_score"].mean(), 2),
        data["engagement_score"].max()
    ])

report = pd.DataFrame(report_data)

st.dataframe(
    report,
    use_container_width=True
)

csv = report.to_csv(index=False)

st.download_button(
    label="Download Analytics Report",
    data=csv,
    file_name="analytics_report.csv",
    mime="text/csv"
)