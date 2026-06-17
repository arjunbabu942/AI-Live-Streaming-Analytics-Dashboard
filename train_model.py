# ==========================================
# Machine Learning Model
# Team Members: Arjun and Daya
# ==========================================

# Import pandas for working with data
import pandas as pd

# Import train_test_split
# Used to divide data into training and testing sets
from sklearn.model_selection import train_test_split

# Import Linear Regression model
from sklearn.linear_model import LinearRegression

# Import function to measure accuracy
from sklearn.metrics import r2_score


# ------------------------------------------
# Step 1: Read Dataset
# ------------------------------------------

data = pd.read_csv("data/streaming_data.csv")


# ------------------------------------------
# Step 2: Select Input Features
# ------------------------------------------

X = data[
    [
        "views",
        "watch_time",
        "likes",
        "comments",
        "shares",
        "retention_rate"
    ]
]


# ------------------------------------------
# Step 3: Select Target Column
# ------------------------------------------

y = data["engagement_score"]


# ------------------------------------------
# Step 4: Split Dataset
# ------------------------------------------
# 80% Training
# 20% Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------
# Step 5: Create Model
# ------------------------------------------

model = LinearRegression()


# ------------------------------------------
# Step 6: Train Model
# ------------------------------------------

model.fit(X_train, y_train)


# ------------------------------------------
# Step 7: Make Predictions
# ------------------------------------------

predictions = model.predict(X_test)


# ------------------------------------------
# Step 8: Measure Accuracy
# ------------------------------------------

score = r2_score(y_test, predictions)

print("Model Accuracy (R² Score):")
print(score)
# Import joblib
import joblib

# Save trained model
joblib.dump(model, "models/engagement_model.pkl")

print("Model saved successfully!")