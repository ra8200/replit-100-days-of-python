# Greet the user
print("Welcome to the Daily Affirmation Generator!")

# Get user input
name = input("What is your name? ").strip()
day = input("What is the current day of the week? ").strip().lower()  # Convert to lowercase to handle case insensitivity
favorites = input("Tell me a few of your favorite things (separated by commas): ").split(',')

# Function to create an affirmation
def create_affirmation(name, day, favorites):
    affirmation_base = "Hello " + name + ", remember that "
    favorite_things = " and ".join(favorites)

    if day == "monday":
        return affirmation_base + "Mondays are fresh starts. You love " + favorite_things + ", let them inspire you today!"
    elif day == "tuesday":
        return affirmation_base + "Tuesdays are for triumphs. Embrace your love for " + favorite_things + " and excel!"
    # Repeat for other days of the week
    # ...
    else:
        return "Hmm, " + day + " doesn't seem like a day of the week. Check your spelling and try again."

# Print the affirmation
print(create_affirmation(name, day, favorites))