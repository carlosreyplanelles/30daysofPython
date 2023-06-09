'''
Exercise: Level 2
do the following operations. The operands are 3 and 4.

    addition(+)
    subtraction(-)
    multiplication(*)
    modulus(%)
    division(/)
    exponential(**)
    floor division operator(//)
'''    
#Operations
from math import sqrt


print('OPERATIONS')
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

'''
Write strings on the python interactive shell. The strings are the following:

    Your name
    Your family name
    Your country
    I am enjoying 30 days of python
'''
print('PROFILE')
name = 'Carlos'
familyName = 'Rey'
country = 'Spain'
print(name)
print(familyName)
print(country)
print('I am enjoying 30 days of python')

print('TYPE CHECK')
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(familyName))
print(type(country))

#Exercise: Level 3
#Part 1
print(type(9)) #Integer
print(type(9.12)) #Float
print(type(1-3j)) #Complex
print(type('Test')) #str
print(type(True)) #Boolean
print (type([1,2,5,6,2])) #List
print(type ((9,2,1,5))) #tuple
print(type({1,2,5,6})) #Set
print (type({"name": "Test", "age": 3})) #Dictionary

#Part 2. Euclidean Distance between (2, 3) and (10, 8)
x=(2,3)
y=(10,8)
distance = sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)
print(distance) #9.433








