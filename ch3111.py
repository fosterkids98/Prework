Fren = ["Bree", 'Rachel', 'Britt']
for frens in Fren :
    print(frens.rstrip(),  str(", we will always be Frens"))
transport = ['kia', 'scooter', 'bike']
mess = 'My favorite mode of transport is my ' + transport[0].title() + '.'
print(mess)
dinner = ['jim mullen', 'joseph bluer', 'snoop dogg']
for dins in dinner:
    print(dins.title() + str(', You are hereby invited to dinner with me and my family.'))
print(dinner[2].title() + str(', will not be able to attend'))
dinner[2] = 'rachel kaito'
for dins in dinner:
    print(dins.title() + str(' is hereby invited to dinner.'))
print('Dear attendees, i have found a bigger table to host my dinner party.')
dinner.insert(0, 'snoop doog')
dinner.insert(2, 'breeanna taylor')
dinner.insert(-1, 'joshua bluer')
for dins in dinner:
    print(dins.title() + str(' is invited to dinner this saturday.'))
print('There has been a change in plans.   I will only be able to invite 2 people to dinner this evening.')
uninvite = [dinner.pop(-1), dinner.pop(1), dinner.pop(0), dinner.pop(-2)]
for uns in uninvite:
    print(uns.title() + str(", I'm sorry to inform you that we havent the space to invite you."))
for dins in dinner:
    print(dins.title() + str(', you are still invited to dinner this evening.'))
del dinner[0]
del dinner[0]
for dins in dinner:
    print('\n', dins)
place = ['alaska', 'europe', 'australia', 'japan', 'myanmar']
print(place)
print(sorted(place))
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)
len(place)