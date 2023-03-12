# Python program to show pyplot module
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")

# This will plot a simple bar chart
plt.bar(df['Species'], df['SepalLengthCm'])

# Title to the plot
plt.title("Iris Dataset")

# Adding the legends
plt.legend(["bar"])
plt.show()
