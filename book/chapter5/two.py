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
###############################################################################



#5-4
###############################################################################
ex = "Alien Colors #2:"
desc = """
    Chose a colour for an aliean as you did in Exercise 5-3, and write an 
    if-else chain.
    """

sub1 = """If the alien's color is green, print a statement that the player just 
earned 5 points for shooring the alien"""

sub2 = """If the alien's color isn't green, print a statement that the player 
just earned 10 points """

sub3 = """Write one version of this program that runs the if block and another 
that runs the else block"""

print(ex);
print(desc);

print(sub1)
print(sub2)
print(sub3)

aliens = ["purple", "GREEN"];
i = 0 
while i < len(aliens):
    print("\n")
    print("test",i)
    green = aliens[i].lower() == "green"
    if green: 
        print(sub1)
        print("You Just Earned 5 Points!")
    else:
        print(sub2)
        print("You Just Earned 10 Points!")

    i += 1; 

