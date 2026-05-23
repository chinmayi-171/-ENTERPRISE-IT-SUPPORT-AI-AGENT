from agents.ticket_agent import create_ticket

from agents.twilio_agent import send_whatsapp_notification


# =====================================================
# ESCALATE ISSUE
# =====================================================

def escalate_issue(

    username,
    name,
    phone,
    issue,
    solution,
    classification

):

    # =====================================================
    # CREATE TICKET
    # =====================================================

    ticket = create_ticket(

        username=username,

        issue=issue,

        classification=classification
    )

    ticket_id = ticket["ticket_id"]

    # =====================================================
    # GET CLASSIFICATION DATA
    # =====================================================

    category = classification.get(
        "category",
        "N/A"
    )

    priority = classification.get(
        "priority",
        "N/A"
    )

    team = classification.get(
        "team",
        "N/A"
    )

    # =====================================================
    # WHATSAPP MESSAGE
    # =====================================================

    message = f"""
🚨 AI HELPDESK ESCALATION ALERT

🎫 Ticket ID:
{ticket_id}

👤 User:
{name}

📞 Phone:
{phone}

📝 Issue:
{issue}

📂 Category:
{category}

⚡ Priority:
{priority}

👨‍💻 Assigned Team:
{team}

❌ Status:
UNRESOLVED AFTER 2 AI ATTEMPTS

Please contact the user immediately.
"""

    # =====================================================
    # SEND WHATSAPP NOTIFICATION
    # =====================================================

    sid = send_whatsapp_notification(
        message
    )

    print("====================================")

    print("ESCALATION COMPLETED")

    print("Ticket ID:", ticket_id)

    print("Twilio SID:", sid)

    print("====================================")

    # =====================================================
    # RETURN DATA
    # =====================================================

    return {

        "ticket_id": ticket_id,

        "sid": sid
    }