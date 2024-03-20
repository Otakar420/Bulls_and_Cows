# bulls_&_cows.py: second project
# author: Petr Běla
# email: petr.bela@seznam.cz
# discord: Petr B. Gibon420#2267

import random
import time
from datetime import datetime
import os

import functions
import texts


# functions
def secret_number() -> int:
    """
    This function generate 4-digit number (each number is unique) and does not start with zero.

    :return: Secret number
    """
    first_digit = [random.randint(1, 9)]
    possible_digits = list(set(range(10)) - set(first_digit))
    next_digits = random.sample(possible_digits, 3)
    all_digits = first_digit + next_digits
    unique_number = int("".join(map(str, all_digits)))

    return unique_number


def has_unique_digit(number: int) -> bool:
    """
    Check if guessed number has unique digits.

    :return: True or False
    """
    number_set = set(str(number))
    return len(number_set) == len(str(number))


def update_bull_cows_values() -> None:
    """
    Update values for every try to guess a secret number.
    """
    bulls, cows = functions.bulls_cows(guess_number, generated_number)
    game_values["attempts"] += 1
    game_values["bulls"] = bulls
    game_values["cows"] = cows
    print(f">>> {bulls} bull{"s" if bulls != 1 else ""}, "
          f"{cows} cow{"s" if cows != 1 else ""}"
          )


def update_end_game_values() -> None:
    """
    Update statistics for the end game.
    """
    os.system("cls" if os.name == "nt" else "clear")
    end_game_values["game_win"] += 1
    end_game_values["total_time"] += duration
    end_game_values["total_attempts"] += game_values["attempts"]
    evaluation_for_user()


def evaluation_for_user() -> None:
    sep_1, sep_2 = ["-" * 55, "=" * 55]
    rating = functions.rating(game_values["attempts"])
    print(f"{sep_2}")
    print(f">>> {generated_number} <<<".center(55))
    print((f"Correct, you've guessed the right number "
           f"in {game_values["attempts"]} guess{"es" if game_values["attempts"] != 1 else ""}!"
           ).center(55)
          )
    print(f"{sep_1}")
    print(f"{rating}\n{sep_1}")
    print(f"Elapsed time: {duration:.2f} sec".center(55))
    print(f"{sep_2}")


def statistics() -> str:
    sep = "=" * 55
    current_time = (datetime.now()).strftime("%H:%M:%S")
    terminal_output = (
        f"{sep}\n"
        # f"{current_time:>55}\n"
        f"{"Statistics:":<{55 // 2}}{current_time:>{55 // 2}}\n"
        f"\tAverage guess to reveal the number: {end_game_values["total_attempts"] / end_game_values["game_win"]:.2f}\n"
        f"\tAverage time to reveal the number: {end_game_values["total_time"] / end_game_values["game_win"]:.2f} sec\n"
        f"\tTotal games wins: {end_game_values["game_win"]}\n"
        f"\tTotal gaming time: {end_game_values["total_time"]:.2f} sec\n"
    )
    return terminal_output


def stats_to_file() -> None:
    """
    This function creates a 'Stats_overall' folder and file 'stats_{Date}.txt' in the working directory.
    """
    try:
        os.mkdir("Stats_overall")
    except FileExistsError:
        pass

    current_date = datetime.now().strftime("%Y-%m-%d")
    name_file = f"{current_date}_stats.txt"
    path_to_file = os.path.join("Stats_overall", name_file)

    with open(path_to_file, mode="a", encoding="utf-8") as txt_output:
        txt_output.write(statistics())


# new game values
game_continue = True
end_game_values = {
        "game_win": 0,
        "total_time": 0,
        "total_attempts": 0
    }

# welcome
texts.welcome_text()

# bulls & cows new game
while game_continue:
    # randomly generated 4-digit number
    generated_number = secret_number()

    # uncomment to view the secret number
    # print(generated_number)

    # setup values for a next game
    start_time = None
    game_values = {
        "attempts": 0,
        "bulls": 0,
        "cows": 0
    }

    while True:
        guess_number = input(f"Enter a number: ")
        start_time = time.time() if start_time is None else start_time
        if guess_number[0] == "0":
            print(f"Your number must not begin with zero.")
            continue

        if guess_number.lower() == "q":
            game_continue = False
            texts.quit_text()
            break

        # verification that the guessed number is a number
        try:
            guess_number = int(guess_number)
        except ValueError:
            print(f"The number must be entered.")
        else:
            # verification that the guessed number consists of 4 unique digits
            if not has_unique_digit(guess_number):
                print(f"Your number must have each digit unique.")
                continue

            if len(str(guess_number)) == len(str(generated_number)):
                update_bull_cows_values()

                # guess the correct number
                if game_values["bulls"] == len(str(generated_number)):
                    end_time = time.time()
                    duration = end_time - start_time
                    update_end_game_values()

                    # check if the user wants to continue
                    game_continue = True if input("Do you want to continue? (y/n): ").lower() == "y"\
                        else False
                    break

            else:
                if len(str(guess_number)) < len(str(generated_number)):
                    print("Your number is less than 4 digits.")
                else:
                    print("Your number is greater than 4 digits.")

# end of game, overall stats
if end_game_values["game_win"] > 0:
    print(statistics())
    stats_to_file()
else:
    print(f"Currently, there are no victories to view statistics.")
