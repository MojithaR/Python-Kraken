# This Python program is designed to understand Python commands to solve math problems.

# Display users instructions
print('Welcome to the calX program!')
print('\n')
num_1 = float(input('Enter your first number: '))
print('\n')
num_2 = float(input('Enter Second number: '))
print('\n')
print('These are the equations')
print('\n')
print('Addition: A\nSubtraction: S\nMultiplication: M\nDivide: D\n1st number Power to 2nd number: P\n')
print('\n')

# Get user inputs
equation = str(input('Enter your equation: '))
print('\n')

# Check user inputs using if-else loops
if equation == 'A':
    resault = num_1 + num_2
elif equation == 'S':
    resault = num_1 - num_2
elif equation == 'M':
    resault = num_1 * num_2
elif equation == 'D':
    resault = num_1 / num_2 
elif equation == 'P':
    resault = num_1 ** num_2
else:
    print('Error! You entered an invalid equation.')

# End of if-else loop
# Display output
print(str(num_1) + ' ' + equation + ' ' + str(num_2) + ' = ' + str(resault))
