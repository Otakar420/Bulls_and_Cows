def rating(tries: int) -> str:
    """
    This functions returns a judgment based on the attempt.

    :param tries: Total number of attempts to guess the number.
    :return: judgment
    """
    best = (
            "Fantastic!".center(55) + "\n" +
            "You guessed it within the first three attempts!".center(55)
    )
    worst = (
            "Keep trying!".center(55) + "\n" +
            "The solution might be closer than expected.".center(55)
    )

    if tries <= 3:
        judgment = best
    elif 4 <= tries <= 5:
        judgment = "Well done!".center(55)
    elif 6 <= tries <= 7:
        judgment = "Not bad. Keep it up!".center(55)
    else:
        judgment = worst
    return judgment


def bulls_cows(number_1: int, number_2: int) -> tuple:
    """
    This function calculates the number of correctly guessed digits (bulls)
    and the number of digits that are contained in the secret number but are
    not in the correct positions (cows).

    Example:
    >>> bulls_cows(1234, 4271)
    (1, 2)

    :param number_1: The guessed number to be compared with the secret number.
    :param number_2: The secret number that is randomly generated.
    :return: A tuple containing the sum of "bulls" and the sum of "cows".
    """
    sum_bulls = 0
    sum_cows = 0
    for i in range(len(str(number_2))):
        if str(number_1)[i] == str(number_2)[i]:
            sum_bulls += 1
        elif str(number_1)[i] in str(number_2) and str(number_1)[i] != str(number_2)[i]:
            sum_cows += 1
    return sum_bulls, sum_cows


if __name__ == "__main__":
    a = 1
    bulls, cows = bulls_cows(9588, 4584)
    print(rating(a))
    print("-" * 55)
    print(bulls, "bulls")
    print(cows, "cows")
