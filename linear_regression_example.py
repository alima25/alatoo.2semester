
import pandas as pd
import statsmodels.api as sm


data = {
    'Average_Pulse': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    'Calorie_Burnage': [250, 260, 270, 280, 290, 300, 310, 320, 330, 340]
}
df = pd.DataFrame(data)


X = df['Average_Pulse']
y = df['Calorie_Burnage']


X = sm.add_constant(X)


model = sm.OLS(y, X).fit()


print(model.summary())


print("\n--- Key Metrics ---")
print("Intercept:", model.params['const'])
print("Slope:", model.params['Average_Pulse'])
print("P-value:", model.pvalues['Average_Pulse'])
print("R-squared:", model.rsquared)
