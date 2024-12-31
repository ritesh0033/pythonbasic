# s = "hello world"
# print(s[5:])


# s = "acdeefghiknfdjaihuiogi"
# print(s[:10])


# s = "hello world"
# modified_string = "H" + s[1:]
# print(modified_string)






# lst = [1,2,3,4,5,6,6,7,8,9]
# print(lst[2:5])

# tup = ("apple","banana","mango")
# print(tup[1:1])
#string into integer
# string = "123"
# try:
#     number = int(string)
#     print(number)
# except ValueError:
#     print("The string cannot be converted to an integer.")

#list into tuple

# list = [1,2,3,4,5,6]
# tup = tuple(list)
# print(tup)

# #tuple into list 
# tuple = ("banana","mango","orange")
# x = list(tuple)
# print(x)

sum = 0
string = "123abc"
for char in string:
    if char.isdigit():
        sum += int(char)
        print(sum)      