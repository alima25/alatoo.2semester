import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import plotly.express as px

# ======================
# 1. BASIC PLOTS
# ======================

# --- Line Plot ---
plt.figure(figsize=(10, 5))
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]
plt.plot(x, y, marker='o', color='blue')
plt.title("1. Line Plot (Trend Over Time)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()

# --- Bar Chart ---
plt.figure(figsize=(10, 5))
categories = ['A', 'B', 'C', 'D']
values = [15, 20, 12, 25]
plt.bar(categories, values, color='green')
plt.title("2. Bar Chart (Category Comparison)")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# --- Scatter Plot ---
plt.figure(figsize=(10, 5))
x = np.random.rand(50)
y = x + np.random.normal(0, 0.1, 50)
plt.scatter(x, y, color='red', alpha=0.6)
plt.title("3. Scatter Plot (Relationship Between X & Y)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# --- Pie Chart ---
plt.figure(figsize=(10, 5))
sizes = [30, 20, 25, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("4. Pie Chart (Proportions)")
plt.show()

# --- 3D Plot ---
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)
ax.scatter(x, y, z, c='purple', marker='o')
ax.set_title("5. 3D Scatter Plot")
plt.show()

# ======================
# 2. ADVANCED PLOTS
# ======================

# --- Box Plot ---
plt.figure(figsize=(10, 5))
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
sns.boxplot(data=data)
plt.title("6. Box Plot (Distribution Summary)")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()

# --- 2D Heatmap ---
plt.figure(figsize=(10, 5))
matrix = np.random.rand(5, 5)
sns.heatmap(matrix, annot=True, cmap="YlGnBu")
plt.title("7. Heatmap (Matrix Visualization)")
plt.show()

# --- Stacked Bar Chart ---
plt.figure(figsize=(10, 5))
labels = ['A', 'B', 'C']
values1 = [10, 15, 20]
values2 = [5, 10, 15]
plt.bar(labels, values1, label='Group 1')
plt.bar(labels, values2, bottom=values1, label='Group 2')
plt.legend()
plt.title("8. Stacked Bar Chart")
plt.show()

# --- Gantt Chart ---
print("\n(Note: Gantt chart opens in browser if Plotly is installed)")
df = px.data.gantt()
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
fig.update_yaxes(autorange="reversed")
fig.show()

# --- Polar Plot ---
plt.figure(figsize=(10, 5))
theta = np.linspace(0, 2*np.pi, 8)
r = np.random.rand(8)
plt.polar(theta, r, marker='o')
plt.title("10. Polar Plot (Cyclic Data)")
plt.show()