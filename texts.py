def quit_text() -> None:
    """
    Quit message for user.
    """
    sep_3 = "=" * 55
    quit_msg = (
            "Ending the game..".center(55) + 2 * "\n" +
            "Every attempt is a step closer to victory.".center(55)
    )
    print(f"{sep_3}\n{quit_msg}\n{sep_3}")


def welcome_text() -> None:
    """
    Welcome text for user.
    """
    sep_1, sep_2, sep_3 = ["_" * 55, "-" * 55, "=" * 55]
    welcome = (
            "Quickly guess the secret 4-digit number. After".center(55) + "\n" +
            "each try, I'll tell you the correct digits".center(55) + "\n" +
            "and positions ['Bulls'] and the correct digits".center(55) + "\n" +
            "in the wrong positions ['Cows']. Dive in".center(55) + "\n" +
            "and show your swift deduction skills!'".center(55)
    )
    print(sep_1)
    print(f"{"Welcome to": ^55}")
    print(f"{">>> BULL & COWS! <<<": ^55}")
    print(f"{sep_2}")
    print(f"{welcome}\n{sep_2}")
    print(f"| quit = 'q' |")
    print(sep_3)


if __name__ == "__main__":
    welcome_text()
    quit_text()
