task=(
    "Make a list of your favorite fruits and then write a series of" 
    "independent if statements that check for certain fruits in your list"
)

favFruits = ["Pineapple", "Mango", "Tomato"]

fruit = "banana"
if fruit.lower() in [favFruit.lower() for favFruit in favFruits]:
    print("you really like",fruit)

fruit = "apple"
if fruit.lower() in [favFruit.lower() for favFruit in favFruits]:
    print("you really like",fruit)

fruit = "orange"
if fruit.lower() in [favFruit.lower() for favFruit in favFruits]:
    print("you really like",fruit)

fruit = "mango"
if fruit.lower() in [favFruit.lower() for favFruit in favFruits]:
    print("you really like",fruit)

fruit = "peach"
if fruit.lower() in [favFruit.lower() for favFruit in favFruits]:
    print("you really like",fruit)
