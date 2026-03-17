div = "--------------------------------------------------------"
ex = "4-13"
task = "Buffet"
desc = "A buffet-style restaurant offers only five basic foods. Think of five sinmple foods and store them in a tuple."

sub1 = "Print loop:"
sub2 = "Intentional fail modification:"
sub3 = "Updating the menu:"

print(ex)
print(task)
print(desc)
print(div) 

foods = ("Cheese", "Ham", "Beef", "Nuggets", "Pizza")

print('\n')
print(sub1)
for food in foods:
    print(food)

print('\n')
print(sub2)
import traceback
try:
    foods[2] = "lamb"
except:
    traceback.print_exc()
del traceback

print('\n')
print(sub3)
foods = ("Tofu", "Ham", "Turkey", "Nuggets", "Pizza") 

for food in foods:
    print(food)
