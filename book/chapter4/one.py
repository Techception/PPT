#4-1
#pizza loop
print('in this exercise I am going to create a loop of of pizza types')
print('\n')

pizzas = ['pepperoni', 'meat feat', 'hawian']
print('Simple loop:')
print('-----------')
for pizza in pizzas:
    print(pizza)
print('\n')

print('Pizza statement:')
print('---------------')
for pizza in pizzas:
    print(f'I would like to order a {pizza.title()} please')
print('\n')

print('I really like pizza!')
print(f'The {pizzas[0]} is a classic.')
print(f'But you cannot go wrong with a {pizzas[1]}.')
print(f'And everyone thinks is cools to shit on {pizzas[2]},', end=' ') 
print('but I like it too.') 
print('So now you know, I really love pizza!')
print('\n')

#4-2
#Animals loop
print('In this exercise we will loop through the Animals') 
print('---------------')
animals = ['dog', 'cat', 'mouse']
for animal in animals: 
    print(animal)
print('\n')

statement = 'I would like a pet' 
for animal in animals: 
    print(statement,animal.title(),'. It would make a great pet.')
print('All of these animals are types of mammals')

