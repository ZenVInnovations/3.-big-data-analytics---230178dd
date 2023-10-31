
import matplotlib.pyplot as plt
import pandas as pd

# Example data (replace with your dataset)
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [10, 25, 15, 30, 20]
})

# Example bar chart
def create_bar_chart(data):
    plt.figure(figsize=(8, 6))
    plt.bar(data['Category'], data['Value'])
    plt.title('Example Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.savefig('charts/bar_charts/bar_chart_1.png')  # Save the chart to a specific directory
    plt.show()

# Example line chart
def create_line_chart(data):
    plt.figure(figsize=(8, 6))
    plt.plot(data['Category'], data['Value'], marker='o')
    plt.title('Example Line Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.savefig('charts/line_charts/line_chart_1.png')  # Save the chart to a specific directory
    plt.show()

if __name__ == "__main__":
    create_bar_chart(data)
    create_line_chart(data)
