import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Sample data: Let's create a dataframe with random data for demonstration
data = {
    'A': np.random.normal(0, 1, 100),
    'B': np.random.normal(0, 1, 100),
    'C': np.random.normal(5, 2, 100),
}

df = pd.DataFrame(data)
#1.Percentiles
