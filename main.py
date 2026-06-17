# ==========================================
# AI Live Streaming Analytics Dashboard
# Team Members: Arjun and Daya
# ==========================================

# Import pandas library
# Pandas helps us work with CSV files
import pandas as pd

# Read the dataset from the data folder
data = pd.read_csv("data/streaming_data.csv")

# Print a title
print("Streaming Dataset")

# Print the complete table
print(data)