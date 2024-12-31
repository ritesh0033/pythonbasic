
# def divide(x, y):
#     try:
#         result = x / y
#         print("Result:", result)
#     except ZeroDivisionError as e:
#         print("Invalid division: Division by zero is not allowed.")
#     except Exception as e:
#         print(f"General Exception: {e}")


# divide(1, 3)



# def divide():
#     try:
#         x = int(input("enter the number x"))
#         y = int(input("enter the number y"))
#         result = x/y
#         print("result",result)

#     except ZeroDivisionError as e :
#         print("invalid division")
#         x = 1
#         y = 4
#         result = x/y
#         print("result from exception",result)

#     except ValueError as e:
#         print("invalid input from the user please enter the number")
#         x = int(input("enter th number for x"))
#         y  = int(input("enter the number for y "))
#         result = x/y
#         print("result for value error",result)
       
# # divide()
# try:
#    print("x")
# except:
#    print("value not defined")

# lst = [1,2,3]
# try:
#   print(lst[30])
# except IndexError as e:
#    print("value not defined in a range")


#    #3
# a=1 
# b ="xyz"
# try:
#     result = a+b
#     print("sum of number:",result)
# except TypeError:
#     print("sum is not possible")    





# student = {
#      "name":"abc",
#     "roll no":13
#  }
# try:
#     student["class"]
# except KeyError:
#     print('invalid key')

# x = -1
# import traceback
# class class_error(Exception):
#   def__init__(self,message)
# try:
#   if x< 0:
#     raise Exception("sorry,no numbers below zero")
# except Exception as e:
#   traceback.print_exc(e)
#   print(e)
   


# class negative_error(Exception):
#     def __init__(self,message):
#         super().__init__(message)


# class zero_error(Exception):
#     def __init__(self,message):
#         super().__init__(message)


# try:
#     x = -1
#     if x < 0:
#         raise negative_error("sorry,no numbers below zero") 
#     if x == 0:
#         raise zero_error("sorry zero error")
# except negative_error as e:
#     print("x value is negative")

# except zero_error as e:
#     print("x is zero")            


age = int(input("enter the value of the age"))
class negative_error(Exception):
    def __init__(self,message):
        super().__init__(message)

class logic_error(Exception):
    def __init__ (self,message):
        super().__init__(message)

try:
    
    if age > 0:
        raise negative_error("sorry, this age is not valid")
    if age >= 200:
        raise logic_error("sorry , this age exceed the limit")
except negative_error as e:
    print("age value is negative is not possible")
except logic_error as e:
    print("age value has exceed the limit")
