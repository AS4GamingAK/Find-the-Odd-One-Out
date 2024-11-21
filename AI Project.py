import random
def generate_sequence():

    sequence = [2] * 9
    odd_index = random.randint(0, 9)
    sequence[odd_index] = 3
    return sequence, odd_index + 1

def play_game():
    print("Welcome to 'Find the Odd One Out'!")
    print("I will show you a sequence of numbers. One of them is different. Can you find its position?")

    sequence, correct_position = generate_sequence()

    print("\nSequence:", " ".join(str(num) for num in sequence))

    attempts = 0
    while True:
        guess = input("\nEnter the position of the odd one out (1 to 10): ")
        attempts += 1

        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 10.")
            continue
        
        guess = int(guess)

        if guess == correct_position:
            print(f"Congratulations! You found it in {attempts} attempts.")
            break
        else:
            print("Wrong guess! Try again.")

play_game()
