def calc(num1, num2, operator='+'):
    if operator =='+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    
result = calc(10, 20)

print (result)