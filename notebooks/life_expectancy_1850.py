# Re-importing necessary libraries after reset
import matplotlib.pyplot as plt

# Given data
wine_consumption = [2.5, 3.9, 2.9, 2.4, 2.9, 0.8, 9.1, 2.7, 0.8, 0.7]
heart_disease_deaths = [221, 167, 131, 191, 220, 297, 71, 172, 211, 251]

# Plotting the scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(wine_consumption, heart_disease_deaths, color='b', label='Data Points')
plt.title("Heart Disease Deaths vs. Wine Consumption")
plt.xlabel("Wine Consumption (liters)")
plt.ylabel("Heart Disease Deaths (rate)")
plt.grid(True)
plt.legend()
plt.show()
