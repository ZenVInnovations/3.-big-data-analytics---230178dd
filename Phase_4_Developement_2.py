import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import PCA
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# -------------------------------
# Rainfall in India: Analysis & Forecast
# Author: Dasari Ushodaya
# -------------------------------

# Load dataset
df = pd.read_csv('rainfall_india_1901-2015.csv')

# Select features and target
features = df[['Year', 'Month']]
target = df['Rainfall']

# Train-test split
X_tr, X_te, y_tr, y_te = train_test_split(features, target, test_size=0.2, random_state=1)

# Model training
rf = RandomForestRegressor(n_estimators=100, random_state=1)
rf.fit(X_tr, y_tr)

# Predictions
y_hat = rf.predict(X_te)

# Evaluation
mse_val = mean_squared_error(y_te, y_hat)
print(f"MSE: {mse_val:.2f}")

# Plot: Actual vs Predicted
plt.figure(figsize=(10, 6))
plt.scatter(X_te['Year'], y_te, alpha=0.7, label='Actual')
plt.scatter(X_te['Year'], y_hat, color='crimson', alpha=0.6, label='Predicted')
plt.title('Rainfall Prediction: Actual vs Predicted')
plt.xlabel('Year')
plt.ylabel('Rainfall')
plt.legend()
plt.tight_layout()
plt.show()

# PCA for Feature Reduction
pca_model = PCA(n_components=2)
features_pca = pca_model.fit_transform(features)

# PCA Visualization
plt.figure(figsize=(8, 6))
plt.scatter(features_pca[:, 0], features_pca[:, 1], c='teal', alpha=0.6)
plt.title('PCA Projection of Year-Month')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.tight_layout()
plt.show()

# Time Series Analysis with ARIMA
arima = sm.tsa.ARIMA(target, order=(2, 1, 2))
arima_fit = arima.fit()

# ACF and PACF
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
plot_acf(arima_fit.resid, ax=axes[0])
plot_pacf(arima_fit.resid, ax=axes[1])
axes[0].set_title("ACF of Residuals")
axes[1].set_title("PACF of Residuals")
plt.tight_layout()
plt.show()

# Advanced Visualization: Pairplot (Modify features accordingly)
# Ensure features like 'feature1', 'feature2', 'target_category' exist or update accordingly
if {'feature1', 'feature2', 'target_category'}.issubset(df.columns):
    sns.pairplot(df, vars=['feature1', 'feature2'], hue='target_category')
    plt.suptitle('Feature Relationships', y=1.02)
    plt.tight_layout()
    plt.show()
else:
    print("Update feature names in pairplot to match actual columns.")
