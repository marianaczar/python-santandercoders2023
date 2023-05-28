"""def greetings():
    print('welcome to the system!')
    print("it's a pleasure having you here.")
greetings()"""

"""def greetings(name): #function receives parameter name
    print(f"welcome to the system, {name}!")
    print("it's a pleasure having you here.")
greetings('Mary')"""

"""def greetings(name, course): #function receives parameter name
    print(f"welcome to the system, {name}!")
    print(f"it's a pleasure having you in our {course} course.")
greetings('Mary', 'Python')"""

"""this definite value garantees if i don't assign anything to this parameter afterwards, 
it'll have value and won't ocasionate bugs
    in case i assign value only at the end, it's not a standard value and in case it gets lost,
there will be errors in code
"""
def greetings(name, course='python'): #function receives parameter name and parameter course with definite value 'python
    print(f"welcome to the system, {name}!")
    print(f"it's a pleasure having you in our {course} course.")
greetings('Mary')

"""this function is able to be used multiple times because it has a return.
   any time i want to reuse this block of code its possible because of return.
   any piece of code after "return" will be ignored by python."""
def sum(num1, num2):
    return num1 + num2
result = sum(5, 7)

print("sum result is: " ,result)