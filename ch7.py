rentals = input('What kind of car would you like to rent?')
print('\nPlease wait while I try to find a ' + rentals + ' to rent.')

Dinner = input('\nHow many people will be joining us tonight?')

if int(Dinner) >= 8 :
    print("\nI'm sorry but you will have to wait for a bigger table.")
else :
    print('\nPlease follow me to an open table.')


digit = input("\nplease choose a number and i will tell you if its divisible by 10.")
digit = int(digit)

if digit % 10 == 0 :
    print('\nThe number ' + str(digit) + " is divisible by 10.")
else :
    print('\nThe number ' + str(digit) + " is not divisible by 10.")


prompt = "\nWhat kind of toppings would you like on your pizza"
prompt += '\n Enter "n" to close   '
run = True
while run :
    message = input(prompt)

    if message == 'n':
        run = False
    else :
        print("adding " + message + ' to your pizza.')

run = True
mprompt = '\nPlease enter your age for your price.'
mprompt += '\nEnter "n" to exit.   '
pricep = 'Your price is '
while run :
    age = input(mprompt)

    if age == 'n' :
        run = False

    if age < '3' :
        print(pricep + 'free.')

    if age >= '3' and age <= '12' :
        print(pricep + '$10.')

    if age > '12' :
        print(pricep + '$15.')

sandwich_orders = ['pastrami', 'roast beef','ham','chicken','pastrami', 'grilled cheese','pastrami']
finished_sandwich = []

while 'pastrami' in sandwich_orders :
    print("I'm sorry we are out of Pastrami!")
    sandwich_orders.remove('pastrami')


while sandwich_orders :
    sandwich = sandwich_orders.pop()
    
    print('Completeing sandwich order for: ' + sandwich)
    finished_sandwich.append(sandwich)
print(finished_sandwich)