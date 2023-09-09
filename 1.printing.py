
# 1. Using the print method, print "Hello World"
print('#1. Hello World')

# 2. Create variables for the data type below. 
# Data Types:
# Int
# Float
# String
# Boolean 
# Boolean (The other boolean value)
# Lists ( 4 items in list min.)
# Dictionaries  ( 4 key/value pairs min.)
int = 1
float = 1.23
string = "this is a string"
boolean = True
boolean2 = False
# list = ['this', 'is', 'a', 'list']
list = [-6, 5, 8, 1, 9]
dictionary = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4'
}

# 3. For each of the variables, use the print method for each variable. To print each varible
print('#3.')
print('int:',int)
print('float:',float)
print('string:',string)
print('boolean:',boolean)
print('boolean:',boolean2)
print('list:',list)
print('dictionary:',dictionary)

# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
print(f'#4. int: {int}, {string}')

# 5. Comment out all print statements up to this point

# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"
print('#6')
for David in range(5):
    print('David')

# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 
def alex_function():
    for Alex in range(5):
        print("Alex Rocks")

print('#7')
alex_function()

# 8. Declare a function that takes in 2 parameters. 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# Now call that function using "Kyle" and "Winston" as the arguments 
# invoke that function 4 more times
def parameters_function(P1, P2):
    print(f'{P1} and {P2} Rock')

print('#8')
parameters_function('Kyle', 'Winston')

# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for arguement.
# These 2 start w/ the letter A
# Arguement is the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
# b. Now print the index at 100. Does this error? comment it out
# c. Now print the index at -1 index. Observe what it prints. Then comment it out
# d. Now print the index at -100.  Does this error? comment it out
print('a.', list[3])
# print('b.', list[100]) #error: list index out of range
print('c.', list[-1]) #prints 'list' since 'list' is -1 places away from the beginning of the list
# print('d', list[-100]) # error: list index out of range

# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2.  
# The starting number MUST be a negative number. The ending number MUST be postive number
# Looking to get each item printed once in order and then a second time in order
print('#10')
for item in range(2):
    for item in list:
        print(item)

# 11. Write a WHILE LOOP in python that does the same thing as 10. 
print('#11')
i = 0
while i < len(list):
    print(list[i])
    i = i+1

# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"
print('#12')
for item in list:
    print(item)

# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
# Print each key
print('#13')
for item in dictionary:
    print(item)

# 14. Repeat step 13. Instead of printing each key, print each value
# Hint: google "dictionary values python"
print('#14')
print(dictionary.values())