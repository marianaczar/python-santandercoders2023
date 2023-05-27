"""
average_grade = float(input('inform your average grade: '))
if average_grade >= 7:
    print('you have passed!')
elif media >= 5:
    print('you have a chance of recovery.')
else:
    (print('you have not passed.'))
"""

#improved system with double verification
average_grade = float(input('inform your average grade: '))
attendance = float(input('inform your attendance percentage: '))

if average_grade >= 7 and attendance >= 75:
    print('you have passed.')
elif average_grade >= 5 and attendance >= 50:
    print('you have a chance of recovery.')
else: 
    print('you have not passed.')