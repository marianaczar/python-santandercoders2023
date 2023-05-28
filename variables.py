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