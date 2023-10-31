import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset and set low_memory to False to suppress the warning
data = pd.read_csv('Phase_3_Development Part 1/Data/processed_data/cleaned_dataset1.csv', low_memory=False)

# Replace the sample data with your dataset
categories = data['AverageTemperature'] 
values = data['dt'] 

# Create a bar chart
plt.bar(categories, values)
plt.xlabel('AverageTemperature')
plt.ylabel('data')
plt.title('visualizations')

# Display the chart
plt.show()
