# ==========================================
# EDA - Exploratory Data Analysis
# Team Members: Arjun and Daya
# ==========================================

# Import pandas
import pandas as pd

# Read dataset
data = pd.read_csv("data/streaming_data.csv")

# Show first 5 rows
print("\nFIRST 5 ROWS")
print(data.head())

# Show dataset information
print("\nDATASET INFO")
print(data.info())

# Show statistics
print("\nSTATISTICS")
print(data.describe())