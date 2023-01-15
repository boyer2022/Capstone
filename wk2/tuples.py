# Tuples
city_state = [ ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA') ]
# Printing length of tuple - 3
print(len(city_state))

# Each individual
first_city_state = city_state[0]    # index 0, first item in list
print(first_city_state)

# Tuple unpacking
print(first_city_state[0])          # Seattle
print(first_city_state[1])          # WA
        # or
city, state = first_city_state
print(city)                         # prints only city

animals = ('lion', 'puma', 'tiger')

lion, puma, tiger = animals
print(tiger)                        # prints only tiger from tuple

# Sets, modifiable but not allowed duplicates
    # To create empty Set
        #cats = set()
        #cats.add('Lion')
        #cats.add('Tiger')
        #print(cats)
        #cats.add('Cheetah')
        #print(cats)
cats = {'Leopard', 'Tiger', 'Cheetah'}
print(cats)
#looping over
for cat in cats:
    print(cat)

# Adding to list
cats.add('Puma')
# Removing from list
cats.remove('Cheetah')
print(cats) 
    # NO DUPLICATES
cats.add('Puma')

birds = {'owl', 'robin', 'swan'}
print(birds)
birds.add('robin')          # NOT ALLOWED DUPLICTES
print(birds)
birds.remove('owl')
birds.add('cardinal')
print(birds)

# Looping 
for bird in birds:
    print(bird)

# Remove duplictates in list
bird_list = ['robin', 'swan', 'swan', 'eagle', 'cardinal', 'swan', 'robin']
print(bird_list)
    #Convert into set
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates)


