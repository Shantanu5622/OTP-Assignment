import random
import smtplib
from twilio.rest import Client
import keys  # assuming keys.py contains necessary API keys and constants

class EmailSender:
    def sendEmail(self, to_email, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(keys.email_username, keys.email_password)
        server.sendmail(keys.sender_email, to_email, message)
        server.quit()

class SMSSender:
    def sendSMS(self, to_mobile, message):
        client = Client(keys.account_sid, keys.auth_token)
        msg = client.messages.create(
            body=message,
            from_=keys.twilio_number,
            to=to_mobile
        )

class OTPSender:
    def __init__(self, email_sender, sms_sender):
        self.email_sender = email_sender
        self.sms_sender = sms_sender

    def generateOTP(self):
        otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
        return otp

    def sendOTPOverEmail(self, email, otp):
        if self.validateEmail(email):
            msg = f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.\nThis is a system-generated email, so do not reply.'
            self.email_sender.sendEmail(email, msg)
            print(f"OTP is sent to {email} via email.")
        else:
            print("Invalid email address.")

    def sendOTPOverMobile(self, mobile, otp):
        if self.validateMobile(mobile):
            msg = f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.\nThis is a system-generated message, so do not reply.'
            self.sms_sender.sendSMS(mobile, msg)
            print(f"OTP is sent to {mobile} via mobile.")
        else:
            print("Invalid mobile number.")

    def validateEmail(self, email):
        return "@gmail" in email and "." in email

    def validateMobile(self, mobile):
        return len(mobile) == 10 and mobile.isdigit()

if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()
    otp_sender = OTPSender(email_sender, sms_sender)

    email = "metkarishantanu441@gmail.com"
    otp = otp_sender.generateOTP()
    otp_sender.sendOTPOverEmail(email, otp)

    mobile = "9604750155"
    otp = otp_sender.generateOTP()
    otp_sender.sendOTPOverMobile(mobile, otp)
