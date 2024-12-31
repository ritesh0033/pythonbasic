#print ("chai aur python")


#i = 1
#while i < 6:
 # print(i)
  #i += 1




# value = ("enter a number")
# if value.isdigit():
#   num = int(value)
#   print("f converted integer: {num}")
# elif '.' in value:
#   print("f converted to float: {num}")
# else:
#   print("invalid number input")



# number  =  int(input("Enter a number:"))
# if number > 0:
#  print("positive")
# elif number < 0:
#    print("negative")

# x = 5
# if x > 0:
#   if x < 10:
#      print("x is single positive number")
#   else:
#         print("x is a positive number but not a single digit")
# else:
#    print("x is a negative number")
    
    

# x = 10
# if x > 5:
#   print("x is greater than 5")
#   if x < 15:
#     print("x is less than 15")

#my_str = "My name is Ritesh Kumar Yadav"
#x = len(my_str)
#print(x)


#numbers = [1,2,3,4,5]
# sum = 0
# for num in numbers:
#   sum = sum + num
#   print(num)
#   print("sum",sum)


# x = 0
# while x < 5:
#   print(x)
#   x += 1



# x,y = 10,20
# x,y = y, x
# print(x,y)


# x = 10
# y = 20
# x,y = y,x
# print("before swapping")
# print("x=",x)
# print("y=",y)
# print("after swapping")
# print("x=",y)
# print("y=",x)

# numbers = [1,2,3,4,5]
# for num in numbers:
#   if num == 4:
#     break
#   print(num)


# x = [1,2,3,4,5]
# for num in x:
#   if num == 5:
#     break
# print(num)

# x = 0
# while x < 10:
#   x += 2
#   if x == 5:
#    continue
#   print(x)



# choice = int(input("choice 1 for even choice 2 for odd"))
# start = int(input("enter the start number"))
# end = int(input("enter the end number"))
# if choice == 1:
#   start%2 == 0
#   for x in range(start,end,2):
#     print(x)
# else:
#   for x in range(start+1,end,2):
#     print(x)
#     if choice == 2:
#        start %2 != 0
#        for x in range(start,end,2):
#           print(x)
#   else:
#     for x in range(start+1,end):
#       print(x)





# start = "lets play a game"

# if start == 0:
#     game = start
#     print(game)
# elif start == 1:
#     game = "end"  # Define what 'end' should be
#     print(game)
# else:
#     print("Invalid input")


# x = 10
# y = 20
# x = x + y
# y = x - y
# x = x - y


# s = " Hello , World"
# print(s.replace("World","Python"))
# print(s)


# s = "Hello World"
# print(s.lower())



# s = "Hello , Wprld"
# print(s.upper())




# s = "          Hello, World"
# print(s.lstrip())



# s = "Hello, World          "
# print(s.rstrip())


# s = "            Hello, World          "
# print(s.strip())








# name = "#################################################Hello#Nepal########################"
 
# output = "hellonepal"
# first_part = output[0:5]
 
# second_part =  output[5:]
 
# word = first_part.title()+"#" + second_part.title()
 
 
# length_name = len(name)
# l_length = len(name) - len(name.lstrip('#'))
 
# r_length = len(name) - len(name.rstrip('#'))
 
 
# final_output = "#"*l_length + word + "#"*r_length

# print(final_output)


# s = {"banana","apple","cherry"}
# print(s)


# matrix = [ [1,2,3]
#         [4,5,6]
#         [7,8,9]
#         ]
# sum = 0
# for x in matrix:
#           for y in x:
#             sum += y
#             print(sum)






# thisset = {"banana","mango","apple"}
# thisset.add("orange")
# print(thisset)



# thisset = {"banana","mango","apple"}
# tropical = {"pineapple","orange","papaya"}
# thisset.update(tropical)


# st = {}
# print(type(st))

#tup = (1)
# print(type(tup))


# thisset = {"apple","banana","cherry"}
# thisset.remove("apple")
# print(thisset)

# thisset = {"apple","banana","cherry"}
# thisset.discard("1")
# print(thisset)


# set1 = {"a","b","c"}
# set2 = {"a","b","c"}
# set3 = set1.union(set1)
# print(set3)


# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {"john","elena"}
# set4 = {"apple","banana","orange"}
# myset = set1.union(set2,set3,set4)
# print(myset)



# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {"john","elena"}
# set4 = {"apple","banana","orange"}
# myset = set1|set2|set3|set4
# print(myset)


# set1 = {"apple","banana","orange","mango"}
# set2 = {"apple","mango","cherry"}
# set3 = set1.intersection(set2)
# print(set3)


# lst = [(1,2),(2,3),(3,4),(1,0),(1,1)]
# sums = [a + b for a, b in lst]


# print("sums of tuple",sums)
# max_sum = max(sums)
# print("largest value of sum of the tuple",max_sum)

  

  
lst = [(1,2),(2,3),(3,4),(1,0),(1,1)]
result = []
for x in lst:
  if not result:
    sum_numbers = sum(x)
    result.append([x,sum_numbers])
else:
      sum_numbers = sum(x)
      if result[0][1] < sum_numbers:
        result.clear()
        result.append([x,sum_numbers])
        print(result)
