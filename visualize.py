# ==========================================
# Data Visualization
# Team Members: Arjun and Daya
# ==========================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("data/streaming_data.csv")

# Create a histogram
# A histogram shows how values are distributed

plt.figure(figsize=(8,5))

plt.hist(data["views"], bins=20)

plt.title("Distribution of Views")

plt.xlabel("Views")

plt.ylabel("Number of Streams")

plt.show()