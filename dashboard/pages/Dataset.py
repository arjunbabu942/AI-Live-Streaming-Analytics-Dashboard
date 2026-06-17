import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset",
    layout="wide"
)

data = pd.read_csv("data/streaming_data.csv")

st.title("Dataset Explorer")

st.subheader("Dataset Preview")

st.dataframe(
    data,
    use_container_width=True
)

st.subheader("Dataset Statistics")

st.dataframe(
    data.describe(),
    use_container_width=True
)

csv = data.to_csv(index=False)

st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="streaming_data.csv",
    mime="text/csv"
)