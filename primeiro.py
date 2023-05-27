"""
data input and output - lesson 2
"""
#data output
print("hello world!")
#print("welcome to python course!")

#data input
#input("what programming language are you studying? ")

"""
variables - lesson 3
"""

name = "mariana" #creating variable and atributing value
age = 18 
studying = True
height = 1.65

print (name) #output of created variable
print (age) 
print (studying)
print (height)

print (type(name)) #output variable type
print (type(age))
print (type(studying))
print (type(height))

language = input("what programming language are you studying? ") #declared variable 'language' is receiving its data from input
print('the language you are studying is', language) #to cast variable data to output with more words, i add it after a comma

print('name: ', name, 'age: ', age, 'studying: ', studying, "height: ", height)

"""
numerical and boolean operators - lesson 4
"""

#numerical operators
num1 = 10
num2 = 20

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 // num2)
print(20 % 3)
print(2 ** 3)

#boolean operators
age1 = 10
age2 = 15
height1 = 1.77
height2 = 1.65
height3 = height2

print(age1 > age2)            #false
print(age1 <= age2)           #true
print('Python' == 'python')   #false
print('banana' != 'pineaple') #true
print(height1 >= height2)     #true
print(height2 > height3)      #false
""""""
"""
type conversion - lesson 5
"""
age = '26' #declaring variables like they're strings and not int
num1 = '10'
num2 = '20'

print(num1 + num2) #performs concatenation because it reads variables as string.

height = float( input('inform your height: '))