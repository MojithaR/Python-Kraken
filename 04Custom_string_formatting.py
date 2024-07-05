#When we are using some string values and varibles the code may seems to like little bit longer than the usual
#That is why we need to format the strings

first_name=str(input('What is your first name :' + '\n'))
middle_name=str(input('What is your middle name :' + '\n'))
last_name=str(input('Enter your last name :') + '\n')
 
print('Hello,' + ' ' + first_name + ' ' + middle_name +  ' ' + last_name + '\n')
print('welcome to the club!\n')
print()
#End of process 1
# The above code is looks like longer and un clear

#Solution 1 - create some empty place holders

output1= 'Hello, {} {} {}'.format(first_name,middle_name,last_name)

print(output1) 
print()
#Solution 2 -create some place holders and use numbers to specifially identify the items

output2= 'Hi, {0} {1} {2}'.format(first_name,middle_name,last_name)
print(output2)
print()
#solution 3- only available for python 3 version only

output3 = f'Huray, {first_name} {middle_name} {last_name}'
print(output3)