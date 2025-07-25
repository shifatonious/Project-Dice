import random

def roll_dice():
    """
    Simulates rolling a single six-sided die and returns the result.
    """
    return random.randint(1, 6)

def dice_rolling_simulator():
    """
    Runs the interactive dice rolling simulator, allowing the user to
    roll one or more dice repeatedly.
    """
    print("Welcome to the Dice Rolling Simulator!")

    while True:

        user_input = input("Roll the dice? (yes/no): ").lower().strip()

        if user_input == 'yes':
            
            while True:
                try:
                    num_dice_str = input("How many dice do you want to roll? (1-5): ")
                    num_dice = int(num_dice_str)
                    if 1 <= num_dice <= 5:
                        break # Valid input, exit inner loop
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            results = []
            for i in range(num_dice):
                roll = roll_dice()
                results.append(roll)
                print(f"Die {i+1} rolled: {roll}")

            if num_dice > 1:
                print(f"Total sum: {sum(results)}")

        elif user_input == 'no':
            print("Thanks for playing! Goodbye!")
            break # Exit the main loop
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    dice_rolling_simulator()
