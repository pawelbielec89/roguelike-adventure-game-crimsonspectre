from random import sample


def main():
    is_play = True

    while is_play:
        guesses = 0
        searched_number = sample([num for num in range(10)], 3)

        # print(searched_number)

        while guesses < 10:
            user_guess = input("I am thinking of a 3-digit number. Try to guess what it is: ")
            user_guess = list(map(int, user_guess))
            returns = []

            if (user_guess[0] in searched_number or
                user_guess[1] in searched_number or
                user_guess[2] in searched_number):

                for i, number in enumerate(user_guess):
                    if number in searched_number:
                        if number == searched_number[i]:
                            returns.append("Hot")
                        else:
                            returns.append("Warm")
            else:
                returns.append("Cold")

            if returns == 3 * ["Hot"]:
                print("You got it!")
                break

            print("Guess #{}".format(str(guesses+1)))
            print("".join(map(str, user_guess)))
            print(", ".join(returns))
            guesses += 1


if __name__ == '__main__':
    main()
