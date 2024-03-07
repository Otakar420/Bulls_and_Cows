# welcome
welcome = (
    "Quickly guess the secret 4-digit number. After".center(55) + "\n" +
    "each try, I'll tell you the correct digits".center(55) + "\n" +
    "and positions ['Bulls'] and the correct digits".center(55) + "\n" +
    "in the wrong positions ['Cows']. Dive in".center(55) + "\n" +
    "and show your swift deduction skills!'".center(55)
)

# quit message
quit_msg = (
    "Ending the game..".center(55) + 2 * "\n" +
    "Every attempt is a step closer to victory.".center(55)
)

# best evaluation
best = (
        "Fantastic!".center(55) + "\n" +
        "You guessed it within the first three attempts!".center(55)
)

# worst evaluation
worst = (
    "Keep trying!".center(55) + "\n" +
    "The solution might be closer than expected.".center(55)
)

if __name__ == "__main__":
    separator = "-" * 55
    print(f"{separator}\n{welcome}\n{separator}\n{quit_msg}\n{separator}\n{worst}")
