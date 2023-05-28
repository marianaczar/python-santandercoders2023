"""
for variable in range(10):
    print(variable)

for variable in range(1, 10):
    print(variable)

for variable in range(1, 12, 3):
	print(variable)   
"""
sum = 0

for i in range(1, 4):
     grade = float(input(f"inform your grade number {i}: "))
     sum = sum + grade 
print(sum/3)