import pandas as pd
import numpy as np

# Sample DataFrame (exam_data)
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print("Original DataFrame:\n", df)

# 1. Handling Missing Data
def identify_missing_values(df):
    return df.isnull().sum()

def impute_missing_values(df, column, strategy="mean"):
    if strategy == "mean":
        df[column].fillna(df[column].mean(), inplace=True)
    elif strategy == "median":
        df[column].fillna(df[column].median(), inplace=True)
    elif strategy == "mode":
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df

print("\nMissing Values:\n", identify_missing_values(df))
df = impute_missing_values(df, 'score', strategy="mean")
print("\nDataFrame after imputation:\n", df)

# 2. Data Transformation
def label_encode(df, column):
    df[column] = df[column].astype('category').cat.codes
    return df

def one_hot_encode(df, column):
    return pd.get_dummies(df, columns=[column])

df = label_encode(df, 'qualify')
print("\nDataFrame after Label Encoding:\n", df)
df = one_hot_encode(df, 'qualify')
print("\nDataFrame after One-Hot Encoding:\n", df)

# 3. Removing Duplicates
def remove_duplicates(df):
    return df.drop_duplicates()

def identify_duplicates(df):
    return df.duplicated()

print("\nDuplicate Rows:\n", identify_duplicates(df))
df = remove_duplicates(df)
print("\nDataFrame after Removing Duplicates:\n", df)

# 4. Data Scaling and Normalization
def min_max_scale(df, column):
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df

def z_score_normalize(df, column):
    df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df

df = min_max_scale(df, 'score')
print("\nDataFrame after Min-Max Scaling:\n", df)
df = z_score_normalize(df, 'score')
print("\nDataFrame after Z-score Normalization:\n", df)

# 5. Handling Outliers
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    return df

outliers = detect_outliers_iqr(df, 'score')
print("\nDetected Outliers:\n", outliers)
df = handle_outliers(df, 'score')
print("\nDataFrame after Handling Outliers:\n", df)
