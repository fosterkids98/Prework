person = {'first_name': 'zach', 'last_name': 'forester', 
          'age': 26, 'city': 'juby'}
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

fav_num = {'jess': 23, 'zach': 45, 'derek': 72, 'sonya': 31}

for name, num in fav_num.items() :
                        #^.items allows acces to the key 
                        #and the key's value
                        #can also use .keys to acces just the
                        #names .values for vise versa
    print(name.title() + "'s favorite number is: " + 
          str(num) + '.')
        #^str() allows you to turn integers into characters
        #or strings


vamps = []

for vamp_number in range(30):
    new_vamp = {'type': 'flyer', 'points': 5, 'speed': 'slow'}
    vamps.append(new_vamp)
for vamp in vamps[:5] :
    print(vamp)
print("...")
print("total number of aliens: " + str(len(vamps)))
