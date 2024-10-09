import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    prediction = int(input("Predict the dice roll (1-6): "))
    result = roll_dice()
    print(f"You predicted: {prediction}, Dice rolled: {result}")
    if prediction == result:
        print("Congratulations! You guessed it right!")
    else:
        print("Sorry, better luck next time!")

