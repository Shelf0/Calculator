operation = input('''
Select the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

#Code for input prompts 
num_1 = int(input('Enter first number:'))
num_2 = int(input('Enter second number:'))

#Addition
if operation == '+':
    print('{} + {} ='.format(num_1, num_2))
    print(num_1 + num_2)

#Subtraction
elif operation == '-':
    print('{} - {} ='.format(num_1, num_2))
    print(num_1 - num_2)

#Multiplication
elif operation == '*':
    print('{} * {} ='.format(num_1, num_2))
    print(num_1 * num_2)

#Division
elif operation == '/':
    print('{} / {} ='.format(num_1, num_2))
    print(num_1 - num_2)

else:
    print('Invalid Input, please try again')

