import random

def roll_dice():
    """Simulate rolling a dice and return a random number between 1 and 6."""
    return random.randint(1, 6)

def predict_outcome():
    """Predict the outcome of the dice roll."""
    # For simplicity, you can have a simple prediction logic.
    # In a more complex app, this could involve statistical methods or machine learning.
    return random.randint(1, 6)

def main():
    print("Welcome to the Random Dice Predicting App!")
    while True:
        input("Press Enter to roll the dice...")
        predicted_value = predict_outcome()
        actual_value = roll_dice()

        print(f"Predicted value: {predicted_value}")
        print(f"Actual value: {actual_value}")

        if predicted_value == actual_value:
            print("Congratulations! Your prediction was correct.")
        else:
            print("Oops! Better luck next time.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
