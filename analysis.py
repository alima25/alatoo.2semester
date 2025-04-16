import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data
data = {
    'Height': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    'Weight': [50, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
}

df = pd.DataFrame(data)

# 1. Percentiles
percentiles_height = np.percentile(df['Height'], [25, 50, 75])
print(f"Percentiles for Height: 25th={percentiles_height[0]}, 50th (Median)={percentiles_height[1]}, 75th={percentiles_height[2]}")

# 2. Variance
# Calculate the variance for the 'Height' column
variance_height = np.var(df['Height'])
print(f"Variance of Height: {variance_height}")

# 3. Standard Deviation

std_dev_height = np.std(df['Height'])
print(f"Standard Deviation of Height: {std_dev_height}")

# 4. Correlation

correlation_hw = np.corrcoef(df['Height'], df['Weight'])[0, 1]
print(f"Correlation between Height and Weight: {correlation_hw}")

# 5. Correlation Matrix
correlation_matrix = df.corr()
print(f"Correlation Matrix:\n{correlation_matrix}")

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix Heatmap")
plt.show()

#6. Correlation vs. Causality

#Correlation: When two variables change together.

#Causality: One variable directly causes the change in another.
