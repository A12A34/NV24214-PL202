import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

kmeans = KMeans(n_clusters=4, random_state=0, n_init=10)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_, cmap="viridis")
plt.title("KMeans Clustering with 4 Clusters")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
