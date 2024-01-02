# create variable for user input

age = int(input("Please enter your age: "))

# create if elif else structure.

# begin at highest 'true' outcome and descend when using '>=' comparison indicators

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for a kiddie discount.")
else:
    print("Age is but a number")