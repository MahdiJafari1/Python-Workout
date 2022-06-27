USERS = {"root": "1234", "ceo": "!!!!!", "reuven": "GrEaTpW?"}


def login():
    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if USERS.get(username) == password:
            return True
        else:
            return False
