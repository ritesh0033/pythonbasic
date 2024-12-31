# numbers = [1,2,3,4,5]
# squared = list(map(lambda x:x**2,numbers))
# print(squared)

# def sq(x):
#     return x**2
# lst = [1,2,3,4,5]
# squared = map(sq,lst)
# print(squared)


# def check(x):
#    if x%2 == 0:
#     return"Even"
#    else:
#      return"odd"

# num= [1,2,34,5,6,7,8,9]
# type_of = list(map(check,num))
# print(type_of)


from  functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,numbers)
print(sum)

numbers = [3,8,1,6,2]
max_num = reduce(lambda x,y:x if x>y else y,numbers)
print(max_num)

words = ["Hello","","World","!"]
sentence = reduce(lambda x,y:x + y, words)
print(sentence)

numbers = [1,2,3,4,5]
product = reduce(lambda x,y: x*y, numbers,1)
print(product)