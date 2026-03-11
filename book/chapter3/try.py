import sys

#3-1
print('3,1')
print('----------------------------')
friends = ['praj', 'radi', 'kev']
print(friends[0])
print(friends[1])
print(friends[2])
print('----------------------------')
print("\n")


#3-2
print('3,2')
print('----------------------------')
message = f"Hello '{friends[0].title()}' whats the plan?"
print(message)
message = f"Hello '{friends[1].title()}' whats the plan?"
print(message)
message = f"Hello '{friends[2].title()}' whats the plan?"
print(message)
print('----------------------------')
print("\n")

#3-3
print('3,3')
print('----------------------------')
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

print('\n')
print('vehicle list final:')
print(vehicles)
print('----------------------------')
print("\n")

#3-4
print('3,4')
print('----------------------------')
inviteList = ['Robyn','Lorraine','Anne']
ask = 'Would you like to come for dinner and stay for breakfast'
print(ask, inviteList[0]+'?')
print(ask, inviteList[1]+'?')
print(ask, inviteList[2]+'?')
print('----------------------------')
print("\n")

#3-5
print('3,5')
print('----------------------------')
notComing = inviteList[2]
rejection = f"unfortuantely {notComing} can't make it"
print(rejection)
stillCome = f"Those still coming are: {inviteList}"
print(stillCome)
print('----------------------------')
print("\n")

#3-6
print('3,6')
print('----------------------------')
print(f"Hey {str(inviteList[:])} we found a bigger table so we have more room to bring more people!") 

inviteList.insert(0, "Princeton")
inviteList.insert(1, "Princess")
inviteList.append("Praj")
strList = str(inviteList);
strList = strList.replace('[','')
strList = strList.replace(']','')
strList = strList.replace("'","")
print(f"everyone coming are:",strList)
print('----------------------------')
print("\n")

#3-7
print('3,7')
print('----------------------------')
message = f"Hey {strList} I regret to announce that the table hasnt arrived so I can only invite 2 persons"
print(message)
print('\n')

while len(inviteList) > 2: 
    reject = inviteList.pop()
    print(f"I'm sorry {reject}, but you cannot come") 

strList = str(inviteList);
strList = strList.replace('[','')
strList = strList.replace(']','')
strList = strList.replace("'","")

print("\n")
print(f"Hi {strList.replace(' ,',' and')}, you are both invited")

del inviteList[0]
del inviteList[0]

print('\n')
print('proof of empty list')
print(inviteList)

likeToVisit = ["Lorraine's bedroom", "Anne's bedroom", "Praj's place", "Kev's place", "My place"] 

print('sorting exercises')
print('standard list')
print(likeToVisit)
print("\n")
print('temp sorted')
print(sorted(likeToVisit))
print("\n")
print('proof list remains original')
print(likeToVisit)
print("\n")
print('sorted in reverse')
print(sorted(likeToVisit,reverse=True))
print("\n")
print('proof list remains original')
print(likeToVisit)
print("\n")
print('permanent reverse sort')
print(likeToVisit.reverse())
print('no output because .reverse() must return none')
print("\n")
print('proof list changed')
print(likeToVisit)
print("\n")
print('reverse list back to the original')
print(likeToVisit.reverse())
print('no output because .reverse() must return none')
print("\n")
print('proof back to original')
print(likeToVisit)
print("\n")
print('permanent sort method')
print(likeToVisit.sort())
print('no output because .sort() must return none')
print("\n")
print('proof permanently sorted')
print(likeToVisit)
print("\n")
print('permanent reverse sort method')
print(likeToVisit.sort(reverse=True))
print('no output because .sort(reverse=True) must return none')
print("\n")
print('proof permanently sorted')
print(likeToVisit)
print('----------------------------')
print('\n')

#3-8
print('3,8')
print('----------------------------')
locations = ['Spain', 'England', 'Germany', 'France', 'Egypt']

print('original list') 
print(locations)

print('sorted list')
print(sorted(locations))

print('reverse sorted list')
print(sorted(locations,reverse='true'))

print('permanent reversed list') 
locations.reverse()
print(locations)

print('permanent reversed list back to original') 
locations.reverse()
print(locations)

print('permanent sorted list')
locations.sort()
print(locations)

print('permanent sorted list in reverse') 
locations.sort(reverse='true')
print(locations)
print('----------------------------')
print('\n')

#3-9
print('3,9')
print('----------------------------')
print('the number of guests comming to the dinner are:',len(likeToVisit))
print('----------------------------')
print('\n')

#3-10
print('3,10')
print('----------------------------')
items = ['Monitor', 'Keyboard', 'Mouse', 'CPU', 'Chassis', 'Motherboard', 'RAM'] 
print('the size of the list is:',len(items))
print('\n')

print('the first item is:', items[0])
print('\n')

print('the last item is:', items[-1])
print('\n')

print('the second item is:', items[2].upper())
print('\n')

newItem = 'Trackpad'
items.append(newItem)
print('adding the new item', newItem, 'so the list is now', items)
print('\n')

newItem = 'GPU' 
items.insert(int(len(items)/2), newItem)
print('adding the new item', newItem, 'to the middle of the list', items)
print('\n')

print('removed', items[0], 'from', items)
print('\n')
del items[0]
print(items)
print('\n')

print('now i want to pop off', items[-1])
popped = items.pop()
print('list is now:', items, 'and', popped, 'is now popped off and saved to a variable')
print('\n')

print('it is also possible to pop a different index')
print('\n')

print('in this example i will pop off', items[1], ' that is the second item in the list', items)
print('\n')

popped = items.pop(1)
print(popped, 'is popped off and now the list is', items) 
print('\n')

print('I can now also straight remove an item from', items)
print('\n')

print('from', items, f'I will remove "{newItem}" from the list which leaves us with,', items.remove(newItem)) #i need to fix this one 
print('\n')

print('I will now temp sort', items, 'using sorted()', sorted(items), 'and prove that it is only temp sorted byt printing the original list again', items)
print('\n')

print('I will now temp sort', items, 'in reverse using sorted(reverse = "true")', sorted(items, reverse ='true'), 'and prove that it is only temp sorted byt printing the original list again', items)
print('\n')


items.reverse()
print('I will now permanently reverse order', items, 'items.reverse()',  items, 'and then put in back to the original order by reversing it back', items)
items.reverse()
print(items)
print('\n')

print('similar to reverse, the sort() method also permanently sorts the order of the list going from', items, 'to', items.sort(), items, 'in this case soring it alphabetically and not on the index like reverse did.  however its not really possible to put it back to how it was after doing this, even after trying reverse ="true"', items.sort(reverse=True), items)
print('\n')

print('----------------------------')

#3-11
print("be aware that python try.py | less means that the stderr is not piped to less thats why the error shows in the middle of the screen")
print("but this can be resolved by 2>&1 which means the stderr is put into the stdout then it can be piped to less")
sys.stdout.flush()
print("be aware that python try.py | less means that the stderr is not piped to less thats why the error shows in the middle of the screen")
print("intentional error", flush=True)
print(items[10], flush=True)
print(likeToVisit[5], flush=True)

