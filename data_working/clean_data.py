# !pip install pandas
# !pip install scikit-learn
# !pip install matplotlib
# !pip install seaborn
# !pip install openpyxl

import pandas as pd
df = pd.read_excel('data/season_three_washing.xlsx')

# Remove unecessary columns

df.columns = df.columns.str.lower()
col_to_remove = ['address', 'date', 'contact info', 
                 'property value', 'customer gender', 
                 'acquired from', 'job id', 'column2', 'column1']
df.drop(columns=col_to_remove, inplace=True)

df.to_csv('data/pressure_washing_cleaned.csv', index=False)