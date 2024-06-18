
import array as arr

# vals = arr.array('i', [3,4,8,23,90])
# vals.reverse()
# vals.append(15)
# for i in range(6):
#   print(vals[i])




# vals = arr.array('i', [3,4,8,23,90]) 
 
# newarr = arr.array(vals.typecode, (a%2 for a in vals))
 
# print(newarr)
  
  
# val = arr.array('i', [])

# n = int(input("Enter the length of Array"))
  
# for i in range(n):
#       x= int(input('Enter the value'))
#       val.append(x)
# val1 = arr.array(val.typecode, (a*a for a in val))      
# print(val1) 
# k = int(input('Enter the index position'))
# print(val[k])


from numpy import *

# arr = array([2,3,4,5.2], int)
# print(arr)

# arr1 = linspace(0,13,10)
# print(arr1)

# arr2 = array([1,23,4,5])
# arr2 = arr2+5
# print(arr2)

# arr3 = array([1,3,5,6])
# arr4 = arr3.view()
# print(arr3)
# print(arr4)

# print(id(arr3))
# print(id(arr4))

# x = int(input('enter the first value')) 
# y = int(input('enter the second value')) 

# def add(x,y):
#     z= x+y
#     return z

# data = add(5,8)
# print(data)


# def sum(a, *b):
#     c = a
#     for i in b:
#         c =c+i
    
#     print(c)


# sum(1,2,3,4,5)        



# def person(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)

# person('sai', age=18, place='hyd', ph=76576)    


# Filtering even and odd numbers.......

# def count(lst):
#     even =0 
#     odd= 0
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else :
#             odd+=1    
#     return even,odd


# lst = [3,73,82,55,89,90,54,73]    
# even,odd = count(lst)

# print(even)
# print(odd)

# print('Even : {} Odd: {}'.format(even,odd))



# Fibonacci series.......

# def fib(n):
#     a =0
#     b=1
#     if n==1:
#         print(a)

#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)    

# fib(10)


# def fiba(num):
#     if(num<0):
#         print('Invalid number')
#     else:
#         a=0
#         b=1

#         print(a)
#         print(b)

#         for i in range(num+1):
#             c=a+b
#             a=b
#             b=c
#             if(c<=num):
#                 print(c)
#             else:
#                 break

# num =int(input('enter the number'))
# fiba(num)                        


# Factorial....

# def fac(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i

#     return f

# x = int(input('Enter the number'))
# result = fac(x)

# print(result)


# Factorial.....


# def fact(n):
#     if n==0:
#         return 1

#     return n* fact(n-1)

# x= int(input('Enter the number'))
# result = fact(x)
# print(result)


# filter map and reduce methods using functools 
from functools import reduce

# num =[2,7,8,9,3,5,4,16,17,15,18]

# even = list(filter(lambda n:n%2==0,num))

# double = list(map(lambda n:n*2, even))

# sum = reduce(lambda a,b: a+b, double)

# print(even)
# print(double)
# print(sum)


##using decorator swaping the arguments

# def div(x,y):
#     print (x/y)


# def div_outer(func):
#     def div_inner(x,y):
#         if x<y:
#             x,y=y,x
#             return func(x,y)
#     return div_inner

# div1 = div_outer(div)
# div1(9,18)


##using syntatic decorator (@)

# def div_outer(func):
#     def div_inner(x,y):
#         if x<y:
#             x,y=y,x
#             return func(x,y)
#     return div_inner

# @div_outer

# def div(x,y):
#     print(x/y)

# div(9,18)


## Returning the function two times using decorator

# def do_twice(func):
#     def wrapper(*arg, **kywarg):
#         func(*arg, **kywarg)
#         func(*arg, **kywarg)
#     return wrapper

# @do_twice

# def display(name):
#     print(f"Hello {name}")

# display("Sai")    



# importing the calc module......
# from calc import *


# x=5
# y=10

# z= add(x,y)
# print(z)

# z1 = sub(x,y)
# print(z1)

# z2 = mul(x,y)
# print(z2)



#..Classes


# class student:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

# name = input('Enter the name')
# age = int(input('Enter the age'))
# stud = student(name,age,'')
# stud1 = student('sai',55,'')       

# print(stud.name)
# print(stud1.age)



# class employee:
#     no_of_employees =0
#     raise_amount = 1.4

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#         employee.no_of_employees +=1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay* self.raise_amount)    


#     @classmethod
#     def from_str(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)    

# emp1 = employee('sai','reddy', 4000)
# emp2 = employee('aman', 'singh', 6000)
# emp3 = employee('harshith', 'palival', 7000)

# emp_str1 = 'john-Doe-2000'

# new_str1 =employee.from_str(emp_str1)


# print(new_str1.email)
# print(employee.no_of_employees)
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# print(emp1.raise_amount)
# print(emp2.last)
# print(emp1.fullname())
# print(emp1.__dict__)
# print(employee.__dict__)


# from datetime import date

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def birthYear(cls, name, year):
#         return cls(name, date.today().year - year)     

#     @staticmethod
#     def isAdult(age):
#         return age>18    


# person1 = Person('sai', '21')
# person2 = Person.birthYear('kiran', 1996)

# print(person1.age)
# print(person2.age)

# print(Person.isAdult(19))



## Inheritance

class Employee:

    raise_amount=1.2

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):

    raise_amount=1.10        
    def __init__(self,name, pay, prog_lang):
        self.prog_lang = prog_lang

        Employee.__init__(self, name, pay)


emp1 = Employee('sai', 3000)
emp2 = Developer('Hari', 5000, 'Python')

print(emp1.name)
print(emp2.pay)
emp2.applyRaise()
print(emp2.pay)
print(emp2.prog_lang)



