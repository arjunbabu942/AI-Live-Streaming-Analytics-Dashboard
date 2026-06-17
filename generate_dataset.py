# ==========================================
# Generate Streaming Dataset
# Team Members: Arjun and Daya
# ==========================================

# Import libraries
import pandas as pd
import numpy as np

# Fix random seed
# This ensures the same random numbers are generated every time
np.random.seed(42)

# Number of streams we want
num_rows = 500

# Create realistic streaming metrics
views = np.random.randint(500, 10000, num_rows)

watch_time = views * np.random.uniform(1.5, 4.0, num_rows)

likes = views * np.random.uniform(0.05, 0.30, num_rows)

comments = views * np.random.uniform(0.01, 0.10, num_rows)

shares = views * np.random.uniform(0.005, 0.05, num_rows)

retention_rate = np.random.uniform(40, 95, num_rows)

# Engagement Score
# Higher likes/comments/shares = higher engagement
engagement_score = (
    likes * 0.4 +
    comments * 0.3 +
    shares * 0.3
)

# Create table
data = pd.DataFrame({
    "views": views,
    "watch_time": watch_time.astype(int),
    "likes": likes.astype(int),
    "comments": comments.astype(int),
    "shares": shares.astype(int),
    "retention_rate": retention_rate.round(2),
    "engagement_score": engagement_score.astype(int)
})

# Save dataset
data.to_csv("data/streaming_data.csv", index=False)

print("Dataset created successfully!")
print("Rows:", len(data))