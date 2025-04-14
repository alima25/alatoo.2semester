
import pandas as pd
import statsmodels.api as sm

# Step 1: Sample dataset (you can replace this with your actual data)
data = {
    'Average_Pulse': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    'Calorie_Burnage': [250, 260, 270, 280, 290, 300, 310, 320, 330, 340]
}
df = pd.DataFrame(data)

# Step 2: Define the independent (X) and dependent (y) variables
X = df['Average_Pulse']
y = df['Calorie_Burnage']

# Step 3: Add a constant term to include the intercept in the model
X = sm.add_constant(X)

# Step 4: Fit the OLS (Ordinary Least Squares) regression model
model = sm.OLS(y, X).fit()

# Step 5: Show the full regression results (includes all required parts)
print(model.summary())

# Step 6 (optional): Print key metrics
print("\n--- Key Metrics ---")
print("Intercept:", model.params['const'])
print("Slope:", model.params['Average_Pulse'])
print("P-value:", model.pvalues['Average_Pulse'])
print("R-squared:", model.rsquared)
