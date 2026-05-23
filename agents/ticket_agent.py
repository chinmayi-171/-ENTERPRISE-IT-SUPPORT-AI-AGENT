import json
import os


# =====================================================
# FILE PATH
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TICKET_FILE = os.path.join(
    BASE_DIR,
    "database",
    "tickets.json"
)


# =====================================================
# CREATE FILE IF NOT EXISTS
# =====================================================

if not os.path.exists(TICKET_FILE):

    with open(TICKET_FILE, "w") as f:

        json.dump([], f)


# =====================================================
# LOAD TICKETS
# =====================================================

def load_tickets():

    with open(TICKET_FILE, "r") as f:

        return json.load(f)


# =====================================================
# SAVE TICKETS
# =====================================================

def save_tickets(tickets):

    with open(TICKET_FILE, "w") as f:

        json.dump(tickets, f, indent=4)


# =====================================================
# GENERATE TICKET ID
# =====================================================

def generate_ticket_id(tickets):

    if len(tickets) == 0:

        return "INC0001"

    last_ticket = tickets[-1]["ticket_id"]

    number = int(
        last_ticket.replace("INC", "")
    )

    new_number = number + 1

    return f"INC{new_number:04d}"


# =====================================================
# CREATE TICKET
# =====================================================

def create_ticket(

    username,
    issue,
    classification

):

    tickets = load_tickets()

    ticket_id = generate_ticket_id(
        tickets
    )

    new_ticket = {

        "ticket_id": ticket_id,

        "username": username,

        "issue": issue,

        "team": classification.get(
            "team",
            "N/A"
        ),

        "priority": classification.get(
            "priority",
            "N/A"
        ),

        "category": classification.get(
            "category",
            "N/A"
        ),

        "status": "OPEN"
    }

    tickets.append(new_ticket)

    save_tickets(tickets)

    return new_ticket


# =====================================================
# GET USER TICKETS
# =====================================================

def get_user_tickets(username):

    tickets = load_tickets()

    user_tickets = []

    for ticket in tickets:

        if ticket["username"] == username:

            user_tickets.append(ticket)

    return user_tickets


# =====================================================
# UPDATE TICKET STATUS
# =====================================================

def update_ticket_status(

    ticket_id,
    new_status

):

    tickets = load_tickets()

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            ticket["status"] = new_status

    save_tickets(tickets)