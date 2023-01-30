"""
This program demonstrates try/except, and error handling
Run this file first without error handling, then comment out the error handling.
Base code:
data_file = open('data.txt')
contents = data_file.read()
print(contents)
data_file.close()
"""
# delete data.txt file
try:
    data_file = open('data.txt')
    contents = data_file.read()
    print(contents)
    data_file.close()
except FileNotFoundError:
    print('Sorry, file not found.')

# Context Manager:
    # Test by creating data.txt
try:
    with open('data.txt') as data_file:
        contents = data_file.read()
        print(contents)
    
except FileNotFoundError:
    print('Sorry, file not found.')