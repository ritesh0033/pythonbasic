# file = open('sample.txt','r')
# a = file.read()
# print(a)
# file.close()


# with open("sample.txt","r") as file:
#     a = file.read()
#     print(a)
#     print(a[6:])

# another method
    # welcome_txt = a .split()
    # for x in welcome_txt:
    #     if"welcome"in x:
    #         print(x) 
  

# with open('data.csv','r')as file:
#     a = file.read()
#     print(a)
#     age_txt = a.split()
#     for x in age_txt():
        
# file_path = 'example.txt'
# with open(file_path,'a') as file:
#     file.write("Apppending new line!\n")


# file_path = 'example.txt'
# with open(file_path,'w') as file
# #     file.write("Hello,world!\n")

# while True:
#     username = input("Enter the name: ")
#     age = int(input("Enter the age: "))
#     address = input("Enter the address: ")
#     try:
#         with open("data.csv",'a') as file:
#             file.write(f"\n{username},{age},{address}")
#             print("Data added successfully")
#     except FileExistsError as e:
#         print("File doesnot exits please check the path of file.")
 

# while True:
#     username = input("Enter the name: ")
#     age = int(input("Enter the age: "))
#     address = input("Enter the address: ")
#     try:
#         with open("data.csv",'a') as file:
#             file.write(f"\n{username},{age},{address}")
#             print("Data added successfully")
#     except FileExistsError as e:
#         print("File doesnot exits please check the path of file.")
 

# information = []
 
# for i in range(3):
#     username = input("Enter username: ")
#     age = int(input("Enter age: "))
#     address = input("Enter address: ")
#     information.append(f"\n{username},{age},{address}")
# try:
#     with open("data.csv",'a') as f:
#         for info in information:
#             f.writelines(info)
# except FileNotFoundError as e:
#     print("file path incorrect. please correct the file path.")
 
 
# print("data added successfully")


# import csv
# file_path = 'data_csv'
# with open(file_path,mode = 'r')as file:
#     csv_reader = csv.reader(file)


# import csv
# data = [
#     ['Alice',30,'london'],
#     ['BOb',25,'paris'],
#     ['charlie',35,'Berlin']
# ]

# file_path = 'output.csv'
# with open(file_path,mode='w',newline ='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name','Age','City'])
#     for row in data:
#         csv_writer.writerow(row)


# import csv
# file_path = 'output.csv'


# with open(file_path,mode='r')as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row['Name'],row['Age'],row['City'])


# import csv
# data = [
#     {'Name':'Alice','Age':30,'City':'London'},
#     {'Name':'Bob','Age':25,'City':'Paris'},
#     {'Name':'Alice','Age':35,'City':'Berlin'},
# ]


# file_path = 'xyz.csv'
# fieldnames = ['Name','Age','City']

# with open(file_path,mode='w',newline='') as file:
#  writer = csv.DictWriter(file,fieldnames=fieldnames)
#  writer.writeheader()
#  for row in data:
#    writer.writerow(row)


import csv
my_dict = {
  " name":"alice",
  "age":27,
  "city":"Newyork",
  "marks":{
      "maths":34,
      "science":67,
      "enlish":23
  }


 }


