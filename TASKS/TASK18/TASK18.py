import seaborn as sns
import matplotlib.pyplot as plt

# pip install seaborn

data = [10, 20, 30, 40, 50]
x = list(range(1, len(data) + 1))

# Plot without histogram (scatter plot instead).
sns.scatterplot(x=x, y=data, s=70)
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Seaborn Scatter Plot")
plt.show()

