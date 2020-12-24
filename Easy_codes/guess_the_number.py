from Easy_codes.art import number_game_logo
import random

print(number_game_logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
print(f"Pssst, the correct answer is {random_number}")

difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

game_level = {
    "easy": 10,
    "hard": 5,
}


def guess_number_game(game_difficulty):
    """It takes the game difficulty level and plays the game."""
    game_life = game_level[game_difficulty]
    if game_difficulty == "easy":
        # game_life = game_level["easy"]
        check_number(game_life)
    elif game_difficulty == "hard":
        check_number(game_life)
    else:
        print("You've entered an incorrect option. Try again.")


def check_number(game_life):
    """ It takes the number of life as input as run the subsequent flow."""
    print(f"You have {game_life} attempts remaining to guess the number.")
    should_continue = True
    while should_continue:
        user_guess = int(input("Make a guess: "))
        if user_guess == random_number:
            print(f"You got it. The answer was {user_guess}")
            should_continue = False
        else:
            game_life -= 1
            if game_life == 0:
                print("You've run out of guesses, you lose.")
                should_continue = False
            else:
                print(f"Guess again.")
                print(f"You have {game_life} attempts remaining to guess the number.")
                if user_guess > random_number:
                    print("Too High.")
                else:
                    print("Too Low.")


guess_number_game(difficulty_type)
