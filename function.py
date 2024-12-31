# def addition(x,y):
#  result = x+y
# print("sum is",result)
# sum1 = addition(1,9)
# print("sum1",sum1)



    
# def subtraction(x,y):
#     result = x-y
#     print("subtraction is ",result)
#     return result
#     sub1 = subtraction(10,5)
#     print("sub1",sub1)




# def addition(x):
#     print("x",x)
    
#     sum_value = sum(x)
#     max_value = max(x)
#     min_value = min(x)

#     return sum_value,max_value,min_value
# lst = [1,2,3,4,5]  
# value= addition(lst)
# print(f"sum is {value[0]}, max is {value[1]},min is {value[2]}")



# def addition(x,y=1):
#     print("x",x)
#     print("y",y)
#     add1 = x+y
#     return add1

# val = addition(5,10)
# print("addition",val)

# def sub(x,y=10):
#     print("x",x)
#     print("y",y)
#     sub1= x-y
#     return sub1

# val = sub(5,9)
# print("addition",val)




#global variable and local variable
# def add():
#     x = 5
#     print("inside the funxtion",x)
#     add()
#     print("outside the function",x)
# y = 20
# def my_function():
#     print("inside the function:", y)

# # my_function()
# print("outside the function:", y)


# z = 30
# def update_global():
#     global z
#     z = z+5
#     print("inside the function:", z)

# my_function()
# print("outside the function:", z)



# def add(*args):
#     print("args",type(args))
# result = args[0] + agrs[1]
# print(f"the sum two numbers:",result)
# print("inside the function")
# add(1,2,3,4,5,7,8)


# #my adding a loop
# def add (*args):
#     sum = 0
#     print("args",type(args))
#     for x in args:
#         if x==1 or x ==5:
#             sum += sum
#             print("sum,sum")
#             add(1,2,3,4,5,7,8)


# def my_fuction(**kid):
#  print("his last name" +kid["name"])
# print("kid",type(kid))
# my_fuction(fname = "Tobias", lname = "refsnes")



# def my_function (*score,**kid):
#     print("His last name" +kid["lname"])
#     kid["marks"] = list(score)
#     print("kids",kid)
    



# my_function(40,50,60,fname = 'abc',lname = 'xyz')


# #recursive function
# def fact(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n *fact(n-1)
# result = fact(5)
# print(result)


#fibonacci series assignment

def fibonacci_recursive(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = 10  
print([fibonacci_recursive(i) for i in range(n)])
