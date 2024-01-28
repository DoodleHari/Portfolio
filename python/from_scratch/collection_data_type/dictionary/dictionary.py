# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they user hashibe, allow us to access a value quickly

capitals = {
            'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            }

capitals.update({'UK':'London'})
capitals.update({'USA':'Las Vegas'})

capitals.pop('China')
# capitals.clear()

# try:
#     print(capitals['Germany'])  # Attempt to access a key not in the dictionary
# except KeyError as e:
#     print(f"Error: {e} is not present in the dictionary.")

# print(capitals.get('Germany'))

# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key,value in capitals.items():
    print(key, value)

for city in capitals.keys():
    print(city)

for x in capitals.values():
    print(x)