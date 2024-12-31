with open("file.csv" , "r") as file:
    lines = file.readlines()
    print(lines)

# to_clean_data = [line.strip().split(",") for line in lines if line.strip()]

# for row in to_clean_data:
#     cleaned_data = [data.split() for data in row]
#     #print(cleaned_data)
# i = 0
# with open("file.csv" , "r") as file1:
#     with open('file1.csv' , 'w') as file2:
#         lines = file1.readlines()
#         row = [line.split() for line in lines if line.split()]
#         #print(row)

#         for i , data in enumerate(row):
#             print(data)
#             for j , data1 in enumerate(data):
#                 i = i - 1
#                 k = str(i)
#                 print('i =' , i , 'j =' ,j)
#                 print(data[j])
#                 #print(data1[0].isalnum())
#                 if k  ==  data[0] :
#                     print("remove",j,k,type(k),data[j],type(data[0]))
#                 else:
#                     print("not remove",j,k,type(k),data[j],type(data[0]))
#                     file2.write(data1 + ',')

#             print('\n')
#             file2.write("\n")