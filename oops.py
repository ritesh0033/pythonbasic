# class  Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#         def greet(self):
#             return f"hello my name is {self.name} and I am{self.age} years old."
        
#         person1 = Person("Alice",21)
#         person2 = Person("Bob",25)

#         print(person1.name)
#         print(person2.age)


# message  =  person1.greet()
# print(message)



# class car:
#     wheels = 4

# def __init__(self,make,model):
#         self.make = make
#         self.model = model

#         print(car.wheels)
        

# car1 = car("Toyata","Camary")
# car2 = car("Honda","Accord")

# def car(self):
#     return f"carmodel is model.car."

# print(car1.make)
# print(car2.make)

# message = car1.model()
# print(message)



# class car:
#     def __init__(self,name,age):
#      self.name = name
#      self.age = age

#      def fast(self,a,b):
#         print("this car is fast")
#         print(a)
#         print(b)

# car1= car("abc","123")
# value = car1.fast(1,2)
# print(value)

# class Area():
#     pi = 3.14
#     def rectangle(self,len,bre):
#         return(len*bre)
#     def square(self,radius):
#         return self.pi*(radius**2)
    
#     def square(self,len):
#         return len*len
    
# table = Area()
# print("Area of rectangle",table.react(2,2)) 
# print("Area of square",table.square(2)) 
# print("Area of ",table.circle(2)) 




# class Car():
#     def __init__(self,brand,model):
#         self.brand= brand
#         self.model = model

# my_car = Car("Toyata","Suzuki")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("tata","safari")
# print(my_new_car.model)


# class animal:
#     def sound():
#         print("this is a animal")
#     class dog:
#      def bark():
#         print("dogs barks")
        
# a = dog()
# a.sound()    

#single inheritance
# class Animal:
#     def speak(self):
#         return"Animal Speaks"
# class Dog(Animal):
#     def bark(self):
#         return"dogs barks"

# my_dog = Dog()
# print(my_dog.speak())
# print(my_dog.bark())              


# #multilevel inheritance
# class A:
#     def method_A(self):
#         return"MethodA"

# class B:
#         def method_B(self):
#          return"MethodB"  

# class C(A,B):
#     def method_C(self):
#          return"MethodC"

# obj_C = C()
# print(obj_C.method_A())         
# print(obj_C.method_B())   
# print(obj_C.method_C())   


# #multilevel inheritance

# class A:
#     def method_A(self):
#         return"MethodA"

# class B(A):
#         def method_B(self):
#          return"MethodB"  

# class C(B):
#     def method_C(self):
#          return"MethodC"

# obj_C = C()
# print(obj_C.method_A())         
# print(obj_C.method_B())   
# print(obj_C.method_C())   


#super()
class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return  self.length * self.width

class Square(Rectangle):
    def __init__(self,side_length):
        super().__init__(side_length,side_length)           


rectangle = Rectangle(5,3) 
square = Square(4)


print("Area of the rectangle:",rectangle.area())
print("Area of the square:",square.area())