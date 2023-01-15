# Function with Tuple
def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km            # returns as a tuple list

# call function
distances = get_distance()
print(distances)
print('Miles', distances[0])         # Just miles
    #Tuples unpacking
miles, km = get_distance()
print(km)
