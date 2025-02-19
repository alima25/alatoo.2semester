#1
#When creating a Series object in pandas, you can use various types of data(integers, strings, floating point numbers, Python objects, etc.). 


#2
import pandas as pd

months = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
                  index=["January", "February", "March", "April", "May", "June", 
                         "July", "August", "September", "October", "November", "December"])
print(months)


#3 
import pandas as pd

batch_students = {
    "MatMIE": 30,
    "Mat DAIS": 25,
    "COMIE": 40,
    "COMEC": 35
}

student_series = pd.Series(batch_students)

print(student_series)

#4
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print(df)

#5
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data, index=labels)

filtered_df = df[df['attempts'] > 2]

print(filtered_df)


