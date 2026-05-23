import json
import os

HISTORY_DB = "database/incident_history.json"


def load_all_history():

    if not os.path.exists(HISTORY_DB):
        return {}

    with open(HISTORY_DB, "r") as f:
        return json.load(f)


def save_history(data):

    with open(HISTORY_DB, "w") as f:
        json.dump(data, f, indent=4)


def save_incident(username, incident, response):

    data = load_all_history()

    if username not in data:
        data[username] = []

    data[username].append({
        "incident": incident,
        "response": response
    })

    save_history(data)


    return data.get(username, [])