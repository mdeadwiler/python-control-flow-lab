# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    val = input('Enter a letter a-z or A-Z: ').lower()
    print(f'The user entered {val}')
    if val == 'aeiou':
        print("The letter {val} is vowel.")
    elif val.isalpha():
        print( "The letter {val} is a constant.")
    else:
        letter == "a"
        new_letter == letter.replace("a", "x")
# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = int(input("Please Enter your age: "))
    print(f'This user is elgible to vote based on {age}!')
    age = 18
    if 18 == age:
        print("Validated!")
    elif user <= age:
        print("Validated!")
    else:
        print("not of age!")
# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
# Your control flow logic goes here
    dog_age = int(input("Dog's age: "))
    print(f'My Dog Sparky is {dog_age}!')
    first_two = 20
    if first_two + 7:
        print(str(dog_age))
    elif dog_age != first_two:
        print("Dog is not born!")
    else:
        new_dog_age = str(first_two)
        dog_age = age.replace(first_two, new+dog_age)
        print("The dog's age in year is {age}!")
# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."

#   - If it is cold BUT NOT raining, print "Wear a warm coat."

#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    it_is_cold = input("Enter if it is cold select yes/no: ")
    it_is_raining = input("Enter if it is raining select yes/no: ")

    print(f'Is it cold today? {it_is_cold}')
    print(f'Is it raining today? {it_is_raining}')
    # for testing purposes
    it_is_cold = True
    it_is_raining = False
    if {it_is_cold} and {it_is_raining}:
        print("Wear a warm coat.")
    elif {it_is_cold} and not {it_is_raining}:
        print("Wear a warm coat.")
    elif {it_is_raining} and not {it_is_cold}:
        print("Carry and umbrella.")
    else: 
        {it_is_cold} and not {it_is_raining}
        print("Wear light clothing")
# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # NEEDED HELP ON THIS ONE, I GET THE LOGIC
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    day = input("Enter the day of the month: ").strip()
    if not day.isdigit() or int(day) < 1 or int(day) > 31:
        print("Please enter a valid day of the month (1-31).")
        return
    day = int(day)
    if month == "December":
        if day >= 21:
            season = "Winter"
        else:
            season = "Fall"
    elif month == "January" or month == "February":
        season = "Winter"
    elif month == "March":
        if day < 20:
            season = "Winter"
        else:
            season = "Spring"
    elif month == "April" or month == "May":
        season = "Spring"
    elif month == "June":
        if day < 21:
            season = "Spring"
        else:
            season = "Summer"
    elif month == "July" or month == "August":
        season = "Summer"
    elif month == "September":
        if day < 22:
            season = "Summer"
        else:
            season = "Fall"
    elif month == "October" or month == "November":
        season = "Fall"
    else:
        print("Please enter a valid month (Jan - Dec).")
        return
    print(f"{month} {day:02} is in {season}.")
# Call the function    
determine_season()


