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

# separators, variables
separator, separator_2, separator_3 = ["-" * 55, "*" * 55, "=" * 55]
game_win, total_time, total_attempts = [0, 0, 0]


# functions
def secret_number() -> int:
    """
    This function generate 4-digit number (each number is unique) and does not start with zero.

    :return: Secret number
    """
    digits = list(range(10))
    random.shuffle(digits)
    digits = digits[:4]

    while digits[0] == 0:
        random.shuffle(digits)

    unique_number = int("".join(str(digit) for digit in digits))

    return unique_number


def has_unique_digit(number: int) -> bool:
    """
    Check if guessed number has unique digits.

    :return: True or False
    """
    number_set = set(str(number))
    return len(number_set) == len(str(number))


def welcome_text() -> None:
    print("_" * 55)
    print(f"{"Welcome to": ^55}")
    print(f"{">>> BULL & COWS! <<<": ^55}")
    print(f"{separator}")
    print(f"{texts.welcome}\n{separator}")
    print(f"| quit = 'q' |")
    print(separator_3)


def evaluation() -> None:
    print(f"{separator_3}")
    print(f">>> {generated_number} <<<".center(55))
    print((f"Correct, you've guessed the right number "
           f"in {attempts} guess{"es" if attempts != 1 else ""}!"
           ).center(55)
          )
    print(f"{separator_2}")
    print(f"{rating}\n{separator_2}")
    print(f"Elapsed time: {duration:.2f} sec".center(55))
    print(f"{separator_3}")


def statistics() -> str:
    current_time = (datetime.now()).strftime("%H:%M:%S")

    terminal_output = (
        f"{separator_3}\n"
        # f"{current_time:>55}\n"
        f"{"Statistics:":<{55//2}}{current_time:>{55//2}}\n"
        f"\tAverage guess to reveal the number: {total_attempts / game_win:.2f}\n"
        f"\tAverage time to reveal the number: {total_time / game_win:.2f} sec\n"
        f"\tTotal games wins: {game_win}\n"
        f"\tTotal gaming time: {total_time:.2f} sec\n"
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


# welcome
welcome_text()

game_continue = True

# bulls & cows new game
while game_continue:
    # randomly generated 4-digit number
    generated_number = secret_number()
    
    # setup values
    attempts, bulls, cows = [0, 0, 0]
    start_time, end_time = [None, None]

    while True:
        guess_number = input(f"Enter a number: ")
        start_time = time.time() if start_time is None else start_time
        if guess_number[0] == "0":
            print(f"Your number must not begin with zero.")
            continue

        if guess_number.lower() == "q":
            game_continue = False
            print(f"{separator_3}\n{texts.quit_msg}\n{separator_3}")
            break

        # verification that the number is 4 digits and it is a number
        try:
            guess_number = int(guess_number)
            if not has_unique_digit(guess_number):
                print(f"Your number must have each digit unique.")
                continue

            if 1023 <= guess_number <= 9876:
                # update values
                attempts += 1
                bulls, cows = functions.bulls_cows(guess_number, generated_number)
                print(f">>> {bulls} bull{"s" if bulls != 1 else ""},"
                      f"{cows} cow{"s" if cows != 1 else ""}"
                      )

                # correct number
                if bulls == 4:
                    os.system("cls" if os.name == "nt" else "clear")
                    end_time = time.time()
                    duration = end_time - start_time
                    rating = functions.rating(attempts)

                    # update statistics
                    game_win += 1
                    total_time += duration
                    total_attempts += attempts

                    # evaluation for users
                    evaluation()

                    # check if the user wants to continue
                    game_continue = True if input("Do you want to continue? (y/n): ").lower() == "y" else False
                    break

                # reset values to another attempt
                bulls, cows = [0, 0]

            elif len(str(guess_number)) < 4:
                print(f"Your number is less than 4 digit.")

            elif len(str(guess_number)) > 4:
                print(f"Your number is greater than 4 digit.")

        except ValueError:
            print(f"The number must be entered.")
else:
    # end of game, overall stats
    if game_win > 0:
        print(statistics())
        stats_to_file()
    else:
        print(f"Currently, there are no victories to view statistics.")
