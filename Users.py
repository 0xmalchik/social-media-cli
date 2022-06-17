class Users:
    def __init__(self) -> None:
        self.users = list()

    def add_users(self, userObj):
        self.users.append(userObj)

    def get_users(self):
        return self.users

    def update_password(self, new_data_obj):
        for a in self.users:
            if a["email"] == new_data_obj['email']:
                a['password'] = new_data_obj['password']
                print("Password updated !")

    def check_dup_email(self, email):
        for a in self.users:
            if a["email"] == email:
                return True

    def check_password(self, mailPassObj):
        # Find user object by email
        for a in self.users:
            # check for by validity
            if a["email"] == mailPassObj['email']:
                if a['email'] == mailPassObj['email'] and a['password'] == mailPassObj['password']:
                    print("Logging in...")
                    return True
            elif a['email'] == mailPassObj['email'] and a['password'] != mailPassObj['password']:
                print("Wrong password")
                return False
            elif a['email'] != mailPassObj['email']:
                return False
