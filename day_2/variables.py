#Day 2: 30 Days of python programming

#Level 1

#Declare a first name variable and assign a value to it
import math


first_name="Carlos"
#Declare a last name variable and assign a value to it
last_name="Rey"
#Declare a full name variable and assign a value to it
full_name= first_name,last_name
#Declare a country variable and assign a value to it
country= 'Spain'
#Declare a city variable and assign a value to it
city= 'Seville'
#Declare an age variable and assign a value to it
age= 30
#Declare a year variable and assign a value to it
year= 2023
#Declare a variable is_married and assign a value to it
is_married= False
#Declare a variable is_true and assign a value to it
is_true= True
#Declare a variable is_light_on and assign a value to it
is_light_on=False
#Declare multiple variable on one line
postal_code, email = 14980, 'test@gmail.test'

print(full_name)
print ('type:',type(full_name))

#Level 2
print('Level 2')
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(postal_code))
print(type(email))

print('first name length: ', len(first_name))
print('last name length: ', len(last_name))
print ('len(first_name) == len(last_name)', len(last_name) == len(first_name))

num_one = 5
num_two = 4

total = num_one+num_two
print('total: ', total)
diff = num_two-num_one
print('diff: ', diff)
product = num_one*num_two
print('product: ', product)
division = num_one/num_two
print('division: ', division)
remainder = num_two%num_one
print('remainder: ', remainder)
floor_divison = num_one//num_two
print('floor division: ', floor_divison)

radius= input("insert the radius of the circle:")
pi = math.pi
circum_of_circle = 2.0*pi*float(radius)
area = pi*float(radius)**2

print('perimeter: ', circum_of_circle)
print('area: ', area)

user={
    'firstname': 'Carlos',
    'lastname' : 'Rey',
    'country' : 'Spain',
    'age' : 30
}

user_first_name, user_last_name, user_country, user_age = user.values()

print('PROFILE')
print('first name: ' , user_first_name)
print('last name: ', user_last_name)
print('country: ', user_country)
print('age: ', user_age)
