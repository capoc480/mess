import database as db
from tinydb import Query

users = db.users

User = Query()

def get_user(user_id = None):
    user = users.search(User.user_id == user_id)

    print(user)

    if len(user) == 0:
        return None

    return user[0]

def get_user(username, password):
    user = users.search((User.username == username) & (User.password == password))

    print(user)

    if len(user) == 0:
        return None

    return user[0]

def count_users():
    return len(users.all())

def add_user(username, password):
    user = get_user(username, password)

    if user != None:
        return None

    user_id = count_users() + 1

    users.insert({"username": username, "password": password, "user_id": user_id})

    user = get_user(username, password)

    if user != None:
        return user

    return None