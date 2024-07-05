#String type data/information can be stored

name = 'Thorin Son of Thráin'
print(name)
print('\n1.First example is get a string and store it on a meaningfull variable and print it\n\n')

#Combine strings with plus sign

Position = 'Dwarf King'
Full_name = 'Thorin Oakenshield'
print('Welcome', Full_name, 'the', Position ,'of under the mountain!!!\n')
print( Position+' '+ Full_name +' '+ 'Hail!!!\n\n')

#modify strings using functions
sentence = "Long ago in my grandfather Thror's time our family was driven out of the far North, and came back with all their wealth and their tools to this Mountain on the map."

# Convert the entire string to uppercase
print(sentence.upper() + '\n')

# Convert the entire string to lowercase
print(sentence.lower() + '\n')

# Capitalize the first letter of the string
print(sentence.capitalize() + '\n')

# Count the occurrences of the letter 'a' in the string
print(sentence.count('a') , '\n')

# The 'encode' method is used to encode the string to bytes. I removed the redundant print statement.
encoded_sentence = sentence.encode()
print(encoded_sentence)

print('\n\n')

#Functions helps to format strings we get as a inputs, and those data/information is easy to store in DB/ or displays to users in a proper manner

First_name = input('What is your first name:') 
print('\n')
Last_name = input('What is your last name:')
print('\n')
#user enters any format in ther full names
Full_name = (First_name.capitalize() + ' ' + Last_name.capitalize() + ' ')
print('Hello' + ' ' + Full_name + ' ' + 'Welcome to the party!!!\n')
