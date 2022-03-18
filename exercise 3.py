n=18
number_of_guesses=1
print("Number of guesses is limited to 9 times\n ")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the correct number\n"))
    if guess_number<18:
        print("Guess number is less than the expected number,try again\n")
    elif guess_number>18:
        print("Guess number is greater than the expected number,try again\n")
    else:
        print("You Won")
        print(number_of_guesses,"Number of guesses\n")
        print(9-number_of_guesses,"Number of guesses left\n")
        break
if number_of_guesses>9:
    print("Game over")
