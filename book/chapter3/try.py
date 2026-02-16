#3-1
friends = ['praj', 'radi', 'kev']
print(friends[0])
print(friends[1])
print(friends[2])


#3-2
print("\n")
message = f"Hello '{friends[0].title()}' whats the plan?"
print(message)
message = f"Hello '{friends[1].title()}' whats the plan?"
print(message)
message = f"Hello '{friends[2].title()}' whats the plan?"
print(message)

#3-3
print("\n")
vehicles = ['car','bus','train','motorbike','plane']
stmnts = [
        f'I would like to {vehicles[1]} a nut',
        f'I would runa a {vehicles[2]} on that',
        f'wont catch me dead on a {vehicles[3]}',
        f'are you "Higher than a {vehicles[-1]}"?',
        f'faster by {vehicles[0]}'
        ]
for i in stmnts:
    print(i)

print(vehicles)

#3-4
print("\n")
inviteList = ['Robyn','Lorraine','Anne']
ask = 'Would you like to come for dinner and stay for breakfast'
print(ask, inviteList[0]+'?')
print(ask, inviteList[1]+'?')
print(ask, inviteList[2]+'?')

#3-5
print("\n")
notComing = inviteList[2]
rejection = f"unfortuantely {notComing} can't make it"
print(rejection)
stillCome = f"Those still coming are: {inviteList}"
print(stillCome)

#3-6
print("\n")
print(f"Hey {str(inviteList)} we found a bigger table so we have more room to bring more people!") 

inviteList.insert(0, "Princeton")
inviteList.insert(1, "Princess")
inviteList.append("Praj")
strList = str(inviteList);
strList = strList.replace('[','')
strList = strList.replace(']','')
strList = strList.replace("'","")
print(f"everyone coming are:",strList)

