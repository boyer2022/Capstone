# Creates file, writes to file,

numbers = ['one', 'two', 'three']

    # 'w' stands for write to a file
with open('numbers.txt', 'w') as number_file:
    number_file.writelines(numbers)

    # 'a' stands for append to a file
# Looping through list
with open('numbers.txt', 'a') as number_file:
    for n in numbers:
            number_file.write('\n' + n + '\n')

# try/except
try:
    with open('numbers.txt', 'a') as number_file:
        for n in numbers:
                number_file.write('\n' + n + '\n')
except OSError:
    print('Error writing to file.')

