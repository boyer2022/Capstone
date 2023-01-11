classes = []


class_name = input('Enter class name? Enter to quit. ')

while class_name:
    classes.append(class_name)
    class_name = input('Enter class name? Enter to quit. ')

    print(classes)

# Loop to print each class one by one
for c in classes:
    print(c)

# Numbered list
for index, c in enumerate(classes):
    # print(index, c)
    #String formatting
    print(f'{index+1}: {c}')