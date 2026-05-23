import json
import os


# =====================================================
# DATABASE PATH
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

CHAT_FILE = os.path.join(
    BASE_DIR,
    "database",
    "chat_history.json"
)


# =====================================================
# CREATE FILE IF NOT EXISTS
# =====================================================

if not os.path.exists(CHAT_FILE):

    with open(CHAT_FILE, "w") as f:

        json.dump([], f)


# =====================================================
# LOAD CHAT HISTORY
# =====================================================

def load_chats():

    try:

        with open(CHAT_FILE, "r") as f:

            return json.load(f)

    except:

        return []


# =====================================================
# SAVE CHAT HISTORY
# =====================================================

def save_chats(chats):

    with open(CHAT_FILE, "w") as f:

        json.dump(
            chats,
            f,
            indent=4
        )


# =====================================================
# SAVE NEW CHAT
# =====================================================

def save_chat(

    username,
    issue,
    solutions,
    attempts,
    status,
    classification

):

    chats = load_chats()

    existing_chat = None

    for chat in chats:

        if (

            chat["username"] == username

            and

            chat["issue"] == issue

        ):

            existing_chat = chat

            break

    # =====================================================
    # UPDATE EXISTING CHAT
    # =====================================================

    if existing_chat:

        existing_chat["solutions"] = solutions

        existing_chat["attempts"] = attempts

        existing_chat["status"] = status

        existing_chat["classification"] = classification

    # =====================================================
    # CREATE NEW CHAT
    # =====================================================

    else:

        new_chat = {

            "username": username,

            "issue": issue,

            "solutions": solutions,

            "attempts": attempts,

            "status": status,

            "classification": classification
        }

        chats.append(new_chat)

    save_chats(chats)


# =====================================================
# UPDATE CHAT
# =====================================================

def update_chat(

    username,
    issue,
    solutions,
    attempts,
    status,
    classification

):

    chats = load_chats()

    for chat in chats:

        if (

            chat["username"] == username

            and

            chat["issue"] == issue

        ):

            chat["solutions"] = solutions

            chat["attempts"] = attempts

            chat["status"] = status

            chat["classification"] = classification

    save_chats(chats)


# =====================================================
# GET USER HISTORY
# =====================================================

def get_user_history(username):

    chats = load_chats()

    user_chats = []

    for chat in chats:

        if chat["username"] == username:

            user_chats.append(chat)

    return user_chats


# =====================================================
# DELETE CHAT
# =====================================================

def delete_chat(

    username,
    issue

):

    chats = load_chats()

    updated_chats = []

    for chat in chats:

        if not (

            chat["username"] == username

            and

            chat["issue"] == issue

        ):

            updated_chats.append(chat)

    save_chats(updated_chats)