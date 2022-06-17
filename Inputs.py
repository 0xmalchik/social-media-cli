import random

class Inputs:
    def __init__(self) -> None:
        print("Choose an input")
        # log = 1
        # change_pass = 2
        # sign = 3
        # exit = 4

    def ask_user(self):
        choice = int(input(
            "Type 1 for logging in \nType 2 for changing your password \nType 3 to sign up \nType 4 for exiting the program \nYour choice is: "))

        if not choice:
            print("Input is not a number, please type a number in the given list : ")
            return False
        return choice

    def log_in(self):
        email = input("Insert your mail: ")
        password = input("Insert your password: ")
        return {"email": email, "password": password}

    def ask_account_creation_inputs(self):
        rand_id = random.randint(0, 10000)
        email = input("Type your e-mail address: ")
        password = input('Type your password: ')
        return {"id": rand_id, "email": email, "password": password}

    def change_password(self):
        email = input('Type the address email needed for recovery')
        new_password = input('Type the new password: ')
        return {"email": email, 'password': new_password}

