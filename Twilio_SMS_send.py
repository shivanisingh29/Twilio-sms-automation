from twilio.rest import Client
import schedule
import time
import config
# ----------------- INFORMATION -------------------
account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_TOKEN
twilio_number="+18783330368"

# ----------------- SMS SENDING FUNCTION -------------------
def send_sms():
    account_sid = config.ACCOUNT_SID
    auth_token = config.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="this is sent from Python",
        from_=twilio_number,
        to=config.NUMBER
    )
    print(message.sid)

# ---------------- SCHEDULE SETUP -----------------

schedule.every(1).minutes.do(send_sms)
print("scheduler started...")
while True:
    schedule.run_pending()
    time.sleep(1)


