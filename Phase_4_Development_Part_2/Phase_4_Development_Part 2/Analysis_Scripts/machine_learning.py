# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load your dataset
data = pd.read_csv("Phase_4_Development Part 1\Data\processed_data\cleaned_data.csv")

# Split the dataset into training and testing sets
X = data.drop(columns=["AverageTemperature"])
y = data["Longitude"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Machine Learning Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Machine Learning Model Accuracy:", accuracy)

