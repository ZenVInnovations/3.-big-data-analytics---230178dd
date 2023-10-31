# model_selection.py
# This script is used for selecting and comparing machine learning models.

# Import necessary libraries
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Load your dataset here
# Example:
# X, y = load_dataset()

# Initialize different models
models = {
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(),
    'Logistic Regression': LogisticRegression()
}

# Evaluate and compare models using cross-validation
for model_name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f'{model_name} Accuracy: {scores.mean():.2f}')
