from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Mean = 1, Standard Deviation = 2
# pip install seaborn
sns.displot(random.normal(loc=1, scale=2, size=1000), kind="kde")
plt.show()

