from random import choice, shuffle


def generate_password(user_letters, user_numbers, user_symbols):
    """
    Generates a random password.

    Parameters
    ----------
    :param user_letters: Number of letters to generate in the password.
    :param user_numbers: Number of numbers to generate in the password.
    :param user_symbols: Number of symbols to generate in the password.

    :return: Password as a string.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
               'X',
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    p_letters = [choice(letters) for _ in range(0, user_letters)]
    p_symbols = [choice(symbols) for _ in range(0, user_symbols)]
    p_numbers = [choice(numbers) for _ in range(0, user_numbers)]
    pwd = p_letters + p_symbols + p_numbers
    shuffle(pwd)

    password = "".join(pwd)
    return password


with open("save.txt", "a") as file:
    input_letters = int(input("How many letters do you want?\n"))
    input_symbols = int(input("How many symbols do you want?\n"))
    input_number = int(input("How many numbers do you want?\n"))
    # checks if users enters all inputs as 0.
    if input_letters != 0 and input_symbols != 0 and input_number != 0:
        user_password = generate_password(input_letters, input_symbols, input_number)
        print(f"Your password is: {user_password}")
        user_choice = input("Do you want to save it? y for yes and n for no.\n")
        correct_choice = False
        while not correct_choice:
            if user_choice == "y":
                print("Saving...")
                # saves the password in save.txt
                file.write(f"{user_password}\n")
                print("Saved...")
                correct_choice = True
            elif user_choice == "n":
                print("Exiting...")
                correct_choice = True
            else:
                print("Wrong input...")
                # continues to ask whether to save the password or not.
                user_choice = input("Do you want to save it? y for yes and n for no.\n")
    else:
        print("No password generated...")
