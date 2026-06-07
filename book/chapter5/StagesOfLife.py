task = """
    write an if else chan that determines a persons stage of life. 
    Set a value for the varidable age, and then:
"""

task1 = (
        "If the person is less than 2 years old. print a message that the " 
        "person is a baby"
        )

task2 = (
        "If the person is at lease 4 years old but less and 13, print a "
        "message thatthe person is a kid"
        )

task3 = (
        "If the person is at least 13 years old but less than 20, print a "
        "message that the person is a teenager."
        )

task4 = ( 
        "If the person is at least 20 years old but less than 65, print a "
        "message that the person is an adult."
        )

task5 = (
        "If the person is age 65 or older, print a messeage that the person "
        "is an elder."
        )

print(
    task, 
    "\n\t"+task1, 
    "\n\t"+task2, 
    "\n\t"+task3, 
    "\n\t"+task4, 
    "\n\t"+task5,
    end="\n\n"
    )

x = int(input("Enter an age: "))

text = "the person is"
person = None
if x < 2:
    person = "baby"
    #print(text,"a baby")
elif x >= 4 and x <= 13:
    person = "kid"
    #print(text, "a kid")
elif x >= 13 and x <= 0:
    person = "teenager"
    #print(text, "a Teenager")
elif x >= 20 and x <= 65:
    person = "adult"
    #print(text, "an adult")
elif X >= 65:
    person = "elder"
    #print(text, "an elder")
else:
    print("invalid")

article = "a"
vowels = "aeiou"
if person[0] in vowels:
    article = "an"

print(text.capitalize(), article, person)
