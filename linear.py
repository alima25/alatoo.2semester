import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [35, 40, 50, 55, 65, 70, 75, 85, 90, 95]
}
df = pd.DataFrame(data)


X = df['Hours_Studied']
y = df['Score']


X = sm.add_constant(X)


model = sm.OLS(y, X).fit()


print(model.summary())
