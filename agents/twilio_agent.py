from twilio.rest import Client


# =====================================================
# TWILIO CONFIG
# =====================================================


import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")

AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

FROM_WHATSAPP = os.getenv("TWILIO_WHATSAPP_NUMBER")

TO_WHATSAPP = os.getenv("TECHNICIAN_WHATSAPP")

# =====================================================
# SEND WHATSAPP NOTIFICATION
# =====================================================

def send_whatsapp_notification(message):

    try:

        client = Client(

            ACCOUNT_SID,
            AUTH_TOKEN
        )

        msg = client.messages.create(

            body=message,

            from_=FROM_WHATSAPP,

            to=TO_WHATSAPP
        )

        print("====================================")

        print("WhatsApp message sent successfully")

        print("SID:", msg.sid)

        print("STATUS:", msg.status)

        print("ERROR:", msg.error_message)

        print("====================================")

        return msg.sid

    except Exception as e:

        print("====================================")

        print("TWILIO ERROR")

        print(str(e))

        print("====================================")

        return str(e)