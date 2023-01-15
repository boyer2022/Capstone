# The classes a student is registered for 
classes_registered = ['ITEC 115', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']
# Make a list of only the ITEC classes
only_itec = [c for c in classes_registered if c.startswith('ITEC')] 
print(only_itec)

# Record temperature every day. Record -1 if not possible to take measurement.
# Averaging the temperatures without the -1 values
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]
only_real_measurements = [temp for temp in high_temps if temp != -1]
print(only_real_measurements)
    # Convert to Celsius
temp_celsius = [(temp_f - 32) * 5 / 9 for temp_f in only_real_measurements]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
print(f'The Average tempurature is {average:.2f}C')          # String formatting with 2 decimal places

# List Comprehension with for loop
strings = ['pizza', 'Beyonce', 'cat']
lengths = []
for string in strings:
    length = len(string)
    lengths.append(length)
print(lengths)

# Increase by 1
numbers = [2, 4, 6]
plus_one = [n + 1 for n in numbers]
print(plus_one)

# Filter by number
numbers = [0, 9, 0, 3, 4, 6, 0, 2]
numbers_no_zeros = [n for n in numbers if n != 0]
print(numbers_no_zeros)

# Filter by condition string
foods = [ 'cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas)

# Python test for membership, use in operator
example = [1, 5, 10]
is_one_in_list = 1 in example       # True
is_seven_in_list = 7 in example     # False
print(is_one_in_list)
print(is_seven_in_list)

course = 'ITEC 1150 Programming Logic'
if '1150' in course:
    print('This is programming Logic') 

numbers = [0, 3, 4, 0, 22, 1]
no_zeros = [number for number in numbers if number !=0]
print(f'This list has no zeros: {no_zeros}')

# Double the list numbers with no 0
numbers = [0, 10, 4, 0, 32]
drop_zeros = [number * 2 for number in numbers if number != 0]
print(f'This list is doubled with no zeros: {drop_zeros}')