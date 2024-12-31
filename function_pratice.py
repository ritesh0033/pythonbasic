#withouth return function
# def calculate_sum(x,y):
#     x = 10
#     y = 20
#     sum = x + y
#     print("the sum of two numbers:",sum)

# # calculate_sum(0,0)

# def sub(x,y):
#     print(x)
#     print(y)
#     difference = x - y
#     return difference
# value = sub(30,20)
# print('the subtractio of the two number:',value)

# to print the fictorail of the number

# def fact(n):
#     if n == 0 or n == 1:
#       return n
#     else:
#      return n*fact(n-1)
# result = fact(5)
# print(result)
    
# to create a list and findout even numbers and to display it in new list

# def fun(numbers):
#     even_numbers =[]
#     numbers = [1,2,3,4,5,6,7,8,9,10]
#     for number in numbers:
#         if number % 2 == 0:
#          even_numbers.append(number)
#     return even_numbers
# thislist = fun([])
# print("even number in a list:",thislist)     


# y = lambda x,y: x/y
# print(y(10,2))


# x = lambda x,y : x + y
# print(x(40,50))

# factor = 10
# result = lambda x: x*factor
# print(result(5))

#default argument and keyword argument

def greet_message(name,message):
    print("hello",name)
    print("messsage",message)
greet_message("jack","how is going on")  
greet_message(message="how are you",name = "ritesh") 
    