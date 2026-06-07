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
    "\n\t"+task5
    )

x = int(input("enter an age"))

if x < 2:
    print("the person is a baby")
elif x >= 4 and x <= 13:
    print("the person is a kid")
elif x >= 13 and x <= 0:
    print("the person is a Teenager")
elif x >= 20 and x <= 65:
    print("The person is an adult")
elif X >= 65:
    print("the person is an elder")
else:
    print("invalid")

