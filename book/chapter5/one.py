#5-1
###############################################################################
car = "Jaguar"
print("Is car == 'jaguar'? I predict false")
print(car == 'jaguar')
print("No its not 'jaguar', but instead 'Jaguar'")
print(car == 'Jaguar')
print("\n")

tool = 'Screwdrier'
print("is tool == 'Screwdriver'? I predict true")
print(tool == 'Screwdriver')
print("\n")

today = 'sunday'
print("today == 'sunday'? true")
print(today == 'sunday')
print("\n")

print("but if we ignore the case then surely also today == 'Sunday'?", end=' ')
print("I predict yes if i use the .title() function") 
print(today.title() == 'Sunday')
print("\n")

sex = "male"
print("sex == 'yes please'? I predict false")
print(sex == 'yes please')
print("but do you think sex == 'male' or 'female'")
print((sex == 'male' or sex == 'female'))
print("\n")

money = 10_000
print("is money > 0? I predict true")
print(money > 0)
print("is money greater than 1,000,000? I predict false")
print(money > 1_000_000)
print("\n") 

#5-2
###############################################################################
colours = ['red','green','blue']
print("Primary Colours =", colours)
colour = 'red'
print(colour, "in primary colours? predict True")
print(colour.lower() in [c.lower() for c in colours])

print("\n")
colour = 'purple'
print(colour, "in", str(colours) +"? predict False")
#print(str([colour.lower() for colour in colours]))
print(colour.lower() in [c.lower() for c in colours])

print("\n")
invalid = "table"
print(invalid, "not in primary colours? predict True")
print(colour.lower() not in [c.lower() for c in colours])

print("\n")
colours.append('orange')
fruits = ['apple', 'orange', 'banana']
fruit = 'orange'
print("Colours =", colours)
print(fruit, "is in both", str(colours), "and", str(fruits) +"? predict True")
print(fruit in (colours and fruits))

