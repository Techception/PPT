#5-3
###############################################################################
ex = "Alien Colors #1:"
desc = """
    Imagine an alien was just shot down in a game. Create a variable 
    called alien_color and assign it a value of 'green', 'yellow', or 'red'
    """

print(ex)
print(desc)

alien_color = "red";

winning = "green"
win = alien_color == winning;
if win:
    print("You just earned 5 points")
print("tested if alien_colour == 'green'")
print("alien_color is", alien_color)
print("\n")

win = alien_color == "red";
if win:
    print("You just earned 5 points")
print("tested if alien_colour == 'green'")


