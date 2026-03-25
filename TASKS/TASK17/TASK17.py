import seaborn as sns
import matplotlib.pyplot as plt

# pip install seaborn

data = [10, 20, 30, 40, 50]
x = list(range(1, len(data) + 1))

sns.lineplot(x=x, y=data, marker="o")
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Seaborn Line Plot")
plt.show()

