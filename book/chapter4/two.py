div = '----------------------------'

#4-3
task = 'count to 20'
print(task)
print(div)
for i in range (1,21):
    print(i)

print('\n')
#4-4 
task = 'one million' 
print(task)
print(div)
numbers = list(range(1,1+10**6))
for number in numbers:
    print(number) 

print('\n')
#4-5
task = 'Summing a Million' 
print(task)
print(div) 
print('min():', min(numbers), '= 1', min(numbers) == 1)
print('max():', max(numbers), '= 1000000', max(numbers) == 10**6)
print('sum():', sum(numbers), ' = 500000500000', sum(numbers) == 500000500000)

print('\n')
#4-6
task = 'Odd Numbers'
print(task)
print(div)
odds = list(range(1, 20, 2))
for odd in odds:
    print(odd)

print('\n')
#4-7
task = 'Threes' 
print(task)
print(div)
multiples = [] 
for i in range(1,11):
    multiples.append(3*i)

for multiple in multiples:
    print(multiple) 

print('\n')
#4-8
task = 'Cubes'
print(task)
print(div) 
cubes = [] 
for i in range(1,11):
    cubes.append(i**3)

for cube in cubes:
    print(cube)

print('\n')
#4-9
task = 'List comprehension for cubes'
print(task)
print(div)
cubes2 = [i**3 for i in range(1,11)]
print(cubes2)
