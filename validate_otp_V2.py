import random
import smtplib
from twilio.rest import Client
import keys  # assuming keys.py contains necessary API keys and constants

class OTPSender:
    def __init__(self):
        # Initialize any necessary variables or configurations here
        pass

    def generateOTP(self):
        otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
        return otp

    def sendOTPOverEmail(self, email, otp):
        if self.validateEmail(email):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('shantanumetkari331@gmail.com', 'szvsrrdpvpmgwnbf')
            msg = f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.\nThis is a system-generated email, so do not reply.'
            server.sendmail("shantanumetkari331@gmail.com", email, msg)
            print(f"OTP is sent to {email} via email.")
        else:
            print("Invalid email address.")

    def sendOTPOverMobile(self, mobile, otp):
        if self.validateMobile(mobile):
            client = Client(keys.account_sid, keys.auth_token)
            msg = client.messages.create(
                body=f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.\nThis is a system-generated message, so do not reply.',
                from_=keys.twilio_number,
                to=mobile
            )
            print(f"OTP is sent to {mobile} via mobile.")
        else:
            print("Invalid mobile number.")

    def validateEmail(self, email):
        return "@gmail" in email and "." in email

    def validateMobile(self, mobile):
        return len(mobile) == 10 and mobile.isdigit()

if __name__ == "__main__":
    otp_sender = OTPSender()

    email = "metkarishantanu441@gmail.com"
    otp = otp_sender.generateOTP()
    otp_sender.sendOTPOverEmail(email, otp)

    mobile = "9604750155"
    otp = otp_sender.generateOTP()
    otp_sender.sendOTPOverMobile(mobile, otp)
