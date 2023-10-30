import matplotlib.pyplot as plt

# Example: Function for creating a histogram
def create_histogram(data, title, x_label, y_label):
    plt.hist(data, bins=20)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Example: Function for creating a scatter plot
def create_scatter_plot(x, y, title, x_label, y_label):
    plt.scatter(x, y, c='blue', marker='o')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
