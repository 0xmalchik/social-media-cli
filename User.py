class User:
    def __init__(self, newUserObj) -> None:
        username = newUserObj["email"]
        print(f"New user is being created...\nWelcome {username} !")
        # print("newUserObj",newUserObj.keys())
        self.id = newUserObj["id"]
        self.email = newUserObj['email']
        self.password = newUserObj["password"]
        # public posts
        self.posts = list()
        # target 1 mail address only able to see the private message
        self.private_messages = list()

    def user_datas(self):
        return {"id": self.id, 'email': self.email, "password": self.password}

    def createUser(self, newUserObj):
        # print("newUserObj",newUserObj.keys())
        self.id = newUserObj["id"]
        self.email = newUserObj['email']
        self.password = newUserObj["password"]
