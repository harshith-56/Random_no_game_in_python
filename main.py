from generate import func
from binary_search import comp_chances


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")


# Get user input for lower and upper bounds
while True:
    lowerBound = get_integer_input('Enter the lower bound: ')
    upperBound = get_integer_input('Enter the upper bound: ')
    if upperBound > lowerBound:
        break
    else:
        print("Error: Upper bound must be greater than lower bound. Please try again.")

# Generate a random number within the bounds
rand_no = func(lowerBound, upperBound)
count = 0

# Calculate computer's guess using binary search
comp = comp_chances(lowerBound, upperBound, rand_no)

while True:
    try:
        # Get user's guess
        user_input = input(f'Enter a guess between {lowerBound} and {upperBound} (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            print("Game ended. You didn't guess the number.")
            break

        user_guess = int(user_input)
        count += 1

        # Compare user's guess with the random number
        if user_guess > rand_no:
            print('Entered number is greater than the random number.')
        elif user_guess < rand_no:
            print('Entered number is smaller than the random number.')
        else:
            print(f'Congratulations! You guessed the number correctly in {count} guesses.')
            break

    except ValueError:
        print("Please enter a valid integer.")


