# class Empolyee:
#         def __init__(self,first,last,pay,email):
#             self.fisrt= first
#             self.last= last
#             self.pay= pay
#             self.email = email

#         def  fullname(self):
#                 return '{}{}'.format(self.fisrt,self.last)


# emp_1 = Empolyee('ritesh','yadav',5000,'ry0323535@gmail.com')
# emp_2 = Empolyee('bibek','yadav',6000,'bibeyadav@gmail.com')





# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())



# class Empolyee:
#     num_employee = 0
#     raise_amount = 1.04
#     def __init__(self,first,last,pay,email):
#         self.fisrt= first
#         self.last = last
#         self.pay = pay
#         self.email = email

#         Empolyee.num_employee += 1

#     def fullname(self):
#       return '{} {}'.format(self.fist,self.last)

#     def apply_raise(self):
#        self.pay = int(self.pay*1.04)

# emp_1 = Empolyee('ritesh','yadav',5000,'ry0323535@gmail.com')
# emp_2 = Empolyee('bibek','yadav',6000,'bibeyadav@gmail.com')

# print(Empolyee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Empolyee.num_employee)
# print(emp_1. __dict__)



# class Employee:
#     num_employee = 0
#     raise_amt = 1.04

#     def __init__(self, first, last, pay, email):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = email

#         Employee.num_employee += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
#     @classmethod
#     def from_string(cls,emp_str):
#      first, last , pay,email = emp_str_1.split('-')
#      return cls(first,last,pay,email)



# emp_1 = Employee('ritesh', 'yadav', 5000, 'ry0323535@gmail.com')
# emp_2 = Employee('bibek', 'yadav', 6000, 'bibeyadav@gmail.com')

# emp_str_1 = 'john-xyz-7000-john@gmail.com'
# emp_str_2 = 'xyz-stvev-8000'
# emp_str_3 = 'steve-yadav-9000'

# new_emp_1 = Employee.from_string(emp_str_1)

# #first, last , pay,email = emp_str_1.split('-')
# #new_emp_1 = Employee(first,last,pay,email)

# Employee.set_raise_amt(1.05)


# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# print(new_emp_1.first)
# print(new_emp_1.last)
# print(new_emp_1.email)


#static method
class Employee:
    num_employee = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay, email):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = email

        Employee.num_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls,emp_str):
     first, last , pay,email = emp_str_1.split('-')
     return cls(first,last,pay,email)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True



emp_1 = Employee('ritesh', 'yadav', 5000, 'ry0323535@gmail.com')
emp_2 = Employee('bibek', 'yadav', 6000, 'bibeyadav@gmail.com')

import datetime
my_date =  datetime.date(2022, 8, 19)
print(Employee.is_workday(my_date))


