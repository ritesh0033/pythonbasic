# import pandas as pd
# data = {
#     'Name':['Alice','Bob','Charlie'],
#     'Age':[25,30,35],
#     'City':['New York','Chicago','Los Angeles']

# }
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd

# df = pd.read_csv('data.csv')
# df.fillna(130,inplace= True)


# import pandas as pd
# df = pd.read_csv('file.csv')
# df.dropna(inplace=True)


# df['Date'] == pd.to_datetime(df['Date'])
# print(df.to_string)
# print(df)

# import pandas as pd
# df = pd.read_csv('file.csv',)
# for x in df.index:
#     if df.loc[x,"Duration"]>120:
#         df.loc[x,"Duration"]=120


import pandas as pd
data  = {'Name':['abc','bob','charlie'],
         'age':[25,None,27]
         'Data'
         }