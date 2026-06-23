import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Explorer",
    layout="wide"
)

st.title("Dataset Explorer")

# =====================================
# FILE UPLOAD
# =====================================

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

# =====================================
# LOAD DATA
# =====================================

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

else:

    data = pd.read_csv("data/streaming_data.csv")

    st.info("Using default dataset")

# =====================================
# PREVIEW
# =====================================

st.subheader("Dataset Preview")

st.dataframe(
    data,
    use_container_width=True
)

# =====================================
# SHAPE
# =====================================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Rows",
        data.shape[0]
    )

with col2:
    st.metric(
        "Columns",
        data.shape[1]
    )

# =====================================
# COLUMN INFO
# =====================================

st.subheader("Column Information")

column_info = pd.DataFrame({
    "Column": data.columns,
    "Data Type": data.dtypes.astype(str)
})

st.dataframe(
    column_info,
    use_container_width=True
)

# =====================================
# STATISTICS
# =====================================

st.subheader("Statistical Summary")

st.dataframe(
    data.describe(),
    use_container_width=True
)

# =====================================
# MISSING VALUES
# =====================================

st.subheader("Missing Values")

missing = data.isnull().sum()

st.dataframe(
    missing.to_frame("Missing Count"),
    use_container_width=True
)

# =====================================
# DOWNLOAD
# =====================================

csv = data.to_csv(index=False)

st.download_button(
    "Download Dataset",
    csv,
    "dataset.csv",
    "text/csv"
)