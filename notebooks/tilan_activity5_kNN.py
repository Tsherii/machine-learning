import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\ASUS\OneDrive\Desktop\Machine Learning\iris.csv"
df = pd.read_csv(file_path)

petal_length = df["petal_length"].values
petal_width = df["petal_width"].values

# New instance to compare
new_instance = [4.5, 2.0]

# Compute Euclidean distances
def euclidean_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.sqrt(np.sum((point1 - point2)**2))
    return distance

# Calculate distances from the new instance to all points in the dataset
distances = [euclidean_distance([petal_l, petal_w], new_instance) for petal_l, petal_w in zip(petal_length, petal_width)]
df["distance"] = distances

# Find the 14 nearest neighbors
k = 14
nearest_neighbors = df.nsmallest(k, "distance")

# Visualization
plt.figure(figsize=(8, 6))
plt.scatter(df["petal_length"], df["petal_width"], label="All Data", color="lightgray")
plt.scatter(nearest_neighbors["petal_length"], nearest_neighbors["petal_width"], color="blue", label="14 Nearest Neighbors")
plt.scatter(new_instance[0], new_instance[1], color="red", label="New Instance (4.5, 2.0)", marker="X", s=100)

# Labels and legend
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("k-Nearest Neighbors Visualization (k=14)")
plt.legend()
plt.grid(True)
plt.show()

# Display nearest neighbors
print(nearest_neighbors)