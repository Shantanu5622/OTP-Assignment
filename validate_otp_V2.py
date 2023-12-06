import random
import smtplib
from twilio.rest import Client
import keys  # assuming keys.py contains necessary API keys and constants

class OTPSender:
    def __init__(self, email_username, email_password):
        self.email_username = email_username
        self.email_password = email_password

    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    def send_otp_over_email(self, email, otp):
        if self.validate_email(email):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_username, self.email_password)
            message = self._compose_email_message(otp)
            server.sendmail(self.email_username, email, message)
            print(f"OTP is sent to {email} via email.")
            server.quit()
        else:
            print("Invalid email address.")

    def send_otp_over_mobile(self, mobile, otp):
        if self.validate_mobile(mobile):
            client = Client(keys.account_sid, keys.auth_token)
            message = self._compose_mobile_message(otp)
            client.messages.create(body=message, from_=keys.twilio_number, to=mobile)
            print(f"OTP is sent to {mobile} via mobile.")
        else:
            print("Invalid mobile number.")

    def validate_email(self, email):
        return "@gmail" in email and "." in email

    def validate_mobile(self, mobile):
        return len(mobile) == 10 and mobile.isdigit()

    def _compose_email_message(self, otp):
        return f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.\nThis is a system-generated email, so do not reply.'

    def _compose_mobile_message(self, otp):
        return f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.\nThis is a system-generated message, so do not reply.'

if __name__ == "__main__":
    email_username = 'shantanumetkari331@gmail.com'
    email_password = 'szvsrrdpvpmgwnbf'

    otp_sender = OTPSender(email_username, email_password)

    email = "metkarishantanu441@gmail.com"
    otp = otp_sender.generate_otp()
    otp_sender.send_otp_over_email(email, otp)

    mobile = "9604750155"
    otp = otp_sender.generate_otp()
    otp_sender.send_otp_over_mobile(mobile, otp)
