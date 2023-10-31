# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load your time series data
time_series_data = pd.read_csv("Phase_3_Development Part 1/Data/processed_data/cleaned_dataset1.csv")

# Time series visualization
plt.plot(time_series_data['dt'], time_series_data['Timestamp'])
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.title("Time Series Analysis")
plt.show()