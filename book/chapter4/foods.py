pizzas = ['pepperoni', 'meat feat', 'hawian']
animals = ['dog', 'cat', 'mouse']
numbers = list(range(1,1+10**6))
odds = list(range(1, 20, 2))
multiples = [] 
for i in range(1,11):
    multiples.append(3*i)

cubes = [] 
for i in range(1,11):
    cubes.append(i**3)

cubes2 = [i**3 for i in range(1,11)]

div = '-----------------------------'
####################################################
#4-10
task = 'Slices:'
description = 'using the multiples of 3 list, '+ str(multiples) +', written in the previous chaper I will add several lines to the end of the program to achieve:'
sub1 = 'Slice to print first 3 items in the list.' 
sub2 = 'Slice to print middle 3 items from the list.' 
sub3 = 'Slice to print last 3 items in the list.'

print(task)
print(description)
print('1.',sub1, multiples)
print('\t->',multiples[:3])
print('2.',sub2, multiples)
mid = int(len(multiples)/2)
print('\t->',multiples[mid-2:mid+1])
print('3.',sub3, multiples)
print('\t->',multiples[-3:])

del task 
del description
del sub1
del sub2
del sub3
####################################################
#4-11
task = 'My Pizzas, Your Pizzas:'
description = 'using the pizza list from ex 4-1,'+ str(pizzas) +', I will make a copy of the list for a friend and do the following:'
sub1 = 'Add  new pizza to the original list.'
sub2 = 'Add a different pizza to the list friend_pizzas.'
sub3 = 'Prove that these are separate lists.' 

print(task)
print(description)
print('1.',sub1, pizzas)
print('\t->')
print('2.',sub2, pizzas)
print('\t->')
print('3.',sub3, pizzas)
print('\t->')
