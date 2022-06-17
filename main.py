from User import User
from Inputs import Inputs
from Users import Users
from InputsLogged import InputsLogged


is_on = True
inputs = Inputs()
inputs_logged = InputsLogged()
users = Users()

while is_on:
    ask_user = inputs.ask_user()
    # logging in
    if ask_user == 1:
        mailPassObj = inputs.log_in()
        is_logged = users.check_password(mailPassObj)
        if is_logged:
            ask_user_logged = inputs_logged.ask_user()
            # TODO  TODO
            # TODO  TODO
            # TODO CURRENT USER LOGGED ?
            # write a post
            if ask_user_logged == 0:
               post = InputsLogged.ask_about_posting()
            #    current_user_logged = Users.find_current_user_logged()
            #    save_post = Users.save_post(post,current_user_logged)
            # find user
            if ask_user_logged == 1:
                pass
            # send a message to a user
            if ask_user_logged == 2:
                pass
            # change password
            if ask_user_logged == 3:
                updated_data = inputs.change_password()
                users.update_password(updated_data)
            # kill program
            if ask_user_logged == 4:
                is_on = False
        else:
            print("\nWrong password\n")

    # Create Account
    if ask_user == 3:
        print("Welcome to our beautiful social media !!!")
        creationObj = inputs.ask_account_creation_inputs()
        create_acc = User(creationObj)
        data = create_acc.user_datas()
        is_dup = users.check_dup_email(data["email"])
        if not is_dup:
            add_user = users.add_users(data)
            all_users = users.get_users()
        else:
            print("email is already in the database")

    # Change password
    if ask_user == 2:
        updated_data = inputs.change_password()
        users.update_password(updated_data)

    if ask_user == 4:
        is_on = False
