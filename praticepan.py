
#to read a file in pandas
# import pandas as pd
# df = pd.read_csv('data1.csv')
# print(df.to_string)

# #to read the fisrt 5 row in a file
# import pandas as pd
# df = pd.read_csv('data1.csv')
# print(df.head())


#to return a data frame with the empty cells
import pandas as pd
df = pd.read_csv('data1.csv')
df.dropna(inplace=True)
new_df = df.dropna()
print(df.to_string())


# import pandas as pd

# # Load the CSV
# df = pd.read_csv('data.csv')

# # Check for missing values
# print("Missing Values Before Cleaning:")
# print(df.isna().sum())

# # Drop rows with missing values
# df.dropna(inplace=True)

# # Check again
# print("\nMissing Values After Cleaning:")
# print(df.isna().sum())

# # Print the cleaned DataFrame
# print(df.to_string(index=False))

# # to clean th wrong format
# import pandas as pd
# df = pd.read_csv('file.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# print(df.to_string())


import pandas as pd
df = pd.read_csv('file.csv')
df.drop_duplicates(inplace=True)
print(df)
