age = 18   
print(age == 18)
print(age != 18)


alien_color = 'yellow'

if alien_color == 'green':
    print('Youve earned 5 points')
if alien_color == 'yellow':
    print('youve earned 1 point')

alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points for shooting this alien')
else :
    print('you just earned 10 points for shooting this alien')


alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points for shooting this alien')
else :
    print('you just earned 10 points for shooting this alien')


alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points for shooting this alien')
elif alien_color == 'yellow':
    print('youve just earned 7.5 points')
else :
    print('you just earned 10 points for shooting this alien')


alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points for shooting this alien')
elif alien_color == 'yellow':
    print('youve just earned 7.5 points')
else :
    print('you just earned 10 points for shooting this alien')

alien_color = 'yellow'

if alien_color == 'green':
    print('You just earned 5 points for shooting this alien')
elif alien_color == 'yellow':
    print('youve just earned 7.5 points')
else :
    print('you just earned 10 points for shooting this alien')

age = int(input())

if age < 2 :
    print('this is a baby.')
if age < 4 and age >= 2 :
    print('This is a toddler')
if age < 13 and age >= 4 :
    print('This is a Child.')
if age < 20 and age >= 13 :
    print('This is a teenager')
if age < 65 and age >= 20 :
    print('This an Adult.')
if age > 65 :
    print('This is a Senior Citizen.')


birds = ['crows', 'ravens', 'vultures', 'hawks', 'owls']

if input() in birds :
    #the use of *in* is how you call specific items in a list for if statements
    print('you know me too well!!')
else :
    print('not listed')


current_users = ['eden oferi', 'rkaito', 'admin', 'freakboy', 'seniordev', 'rachetstrap', 'thedeep303']

new_user = input().lower()
for user in current_users :
    user.lower()

if new_user in current_users :
    print('Sorry, this username already exists')
if new_user not in current_users :
    print('Welcome, ' + new_user.title() + '!')
    current_users.append(new_user.lower())
returning_user = input().lower()

if returning_user == 'admin' :
    print('Hello Admin, would you like to see a status report')
if returning_user in current_users and returning_user.lower() != 'admin' :
    print('Welcome back, ' + returning_user.title() +'!')
if returning_user != 'admin' and returning_user not in current_users :
    print('Please create an account')


numbers = ['1','2','3','4','5','6','7']
for number in numbers :
    if number == '1' :
        print(number + 'st')
    if number == '2' :
        print(number + 'nd')
    if number == '3' :
        print(number + 'rd')
    if number > '3' :
        print(number + 'th')