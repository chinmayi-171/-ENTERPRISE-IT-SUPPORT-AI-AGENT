import json
import bcrypt
import os

USERS_FILE = "database/users.json"


# CREATE USERS FILE IF NOT EXISTS
def initialize_users_file():

    if not os.path.exists(USERS_FILE):

        with open(USERS_FILE, "w") as f:
            json.dump({}, f)


# LOAD USERS
def load_users():

    initialize_users_file()

    with open(USERS_FILE, "r") as f:
        return json.load(f)


# SAVE USERS
def save_users(users):

    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


# HASH PASSWORD
def hash_password(password):

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(
        password.encode(),
        salt
    )

    return hashed.decode()


# VERIFY PASSWORD
def verify_password(password, hashed_password):

    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )


# REGISTER USER
def register_user(name, email, phone, username, password):

    users = load_users()

    if username in users:
        return False, "Username already exists"

    # CHECK EMAIL EXISTS
    for user in users.values():

        if user["email"] == email:
            return False, "Email already registered"

    users[username] = {

        "name": name,
        "email": email,
        "phone": phone,
        "password": hash_password(password)
    }

    save_users(users)

    return True, "Account created successfully"


# LOGIN USER
def authenticate_user(username, password):

    users = load_users()

    if username not in users:
        return False, "User not found"

    stored_password = users[username]["password"]

    if verify_password(password, stored_password):

        return True, users[username]

    return False, "Invalid password"