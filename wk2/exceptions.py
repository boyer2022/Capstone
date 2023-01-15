# Exceptions, try/except
    #https://docs.python.org/3/tutorial/errors.html

cats = ['lion', 'tiger', 'cheetah']
# print(cats[4])        # IndexError: list index out of range

try:
    print(cats[4])
except:
    print('That is not a valid list index.')