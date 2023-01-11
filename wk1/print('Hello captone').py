# String
print('Hello Capstone')

#Variables
    #String
school = 'MCTC'
    #Float
gpa = 4
    #Integer
students_in_class = 22

# if/elif/else loop
if gpa == 4:
    print('WOW!')
elif gpa > 3:
    print('Awesome')
else:
    print('Cool!')

# lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']

schools.sort()
print(schools)      # sorts by alphabetical
schools.append('Century College')
print(schools)
schools.reverse()
print(schools)            # prints list in reverse order

# in operator
if 'CLC' in schools:
    print('MCTC is one of the schools in the list')
else:
    print('School not found')

# strings
class_name = 'Software Development Capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.strip())
print(class_name.split())
    # split by character
print(class_name.split('o'))

# in operator in string
if 'Capstone' in class_name:
    print('This must be the capstone')  # case sensitive
else:
    print('Unable to find string. Check for upper or lower case.')

# loops - for loop over range
for x in range(10):
    print(x)

# for loop over sequence
for s in schools:
    print(s)
    print(s.upper())        # prints all names in uppercase

# looping over string sequence
for letter in school:
    print(letter)

# looping with multiplier
for letter in school:
    print(letter * 10)

    # creating another list based on mulitplier
data = [0] * 10
print(data) 

# while loop

    # Asking for name --- Uncomment to try, Ctrl + /
# name = input('Enter your name: ')
# while len(name) == 0:
#     print('Please enter at least one character ')
#     name = input('Enter your name: ')

# # Better (shorter way to write)
# name_better = input('Please enter you name: ')
# while not name_better:
#     print('Please enter at least one character ')
#     name_better = input('Enter your name: ')


# True and False and None (All Capital)
start_of_semester = True
winter = False

if winter:                          # if winter == True
    print('brrr!')
else:
    print('It is not winter')

# Dictionaries
    # Hashmaps in Java
    # Key/Value pairs, keys must be unique
class_codes = { 2905: 'Capstone', 2560: 'Web', 2545: 'Java'}

print(class_codes[2560])

for code in class_codes:
    print(code)                     # prints keys
    print(class_codes[code])        # prints keys and values

    # Keys/values together
for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)

# String formatting
print('String formatting')
for code, name in class_codes.items():
    print(f'The class code is {code} and the name is {name}')

# Slicing strings, lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']
first_two = schools[0:2]        # [Start of slice: End of slice]
# Short-cut: first_two = schools[:2], omits the first number
print(first_two)

# Printing the last 2 schools
last_school = schools[-1]
print(last_school)

# Printing last schools
last_two_schools = schools[-2:] # Short-cut: last_two_schools = schools[-2:], omits the last number
print(last_two_schools)

# Slicing string
school_name = 'Minneapolis Community and Technical College'
city = school_name[:11]
print(city)

# File I/O
   # Reading file
with open('data.txt') as f:
    print(f.read())

    # Write to file
with open('schools.txt', 'w') as f:
    f.writelines(schools)

# Functions
def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is: ')
    return name

# Call the function
name = get_name()

    