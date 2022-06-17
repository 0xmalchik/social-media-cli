import random
class InputsLogged:
    def __init__(self) -> None:
        pass

    def ask_user():
        choice = int(input(
            "Type 0 for posting something to your personal wall\nType 1 for searching another user\nType 2 to send a message to someone \nType 3 for changing your password \nType 4 for exiting the program \nYour choice is: "))

        if not choice:
            print("Input is not a number, please type a number in the given list : ")
            return False
        return choice

    def ask_about_posting():
        choice = input("What's happening ? :")
        post_id = random.randbytes(1244444)
        return {"choice":choice,"post_id":post_id}

