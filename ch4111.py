pizzas = ['Supreme', 'Multi-meat', 'Philly']

for pizza in pizzas:
    print('I like ' + pizza + ' pizza.')

print('I could eat alot of pizza.')
friend_pizza = pizzas[:]

friend_pizza.append('candy')
pizzas.append('Cheeseburger')

print('My Friend likes:')

for za in friend_pizza:
    print(za + ' pizza.')

print('But I like ')

for pizza in pizzas:
    print(pizza + ' pizza.')


animals = ['dogs', 'cats', 'bears']
print(animals)

for animal in animals:
    print(animal.title() + ' are fun to play with.')

print("If you're a furry")


for value in range(0,5):
    print(value)

digits = list(range(1,1000001))
print(min(digits))
print(max(digits))
print(sum(digits))

odd = list(range(1,20,2))

print(odd)

cube = [digi**3 for digi in range(1,11)]
print(cube)
print(cube[3:8])
print(cube[0:3])
print(cube[8:11])