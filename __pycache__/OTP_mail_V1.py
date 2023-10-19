import random
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('shantanumetkari331@gmail.com','szvsrrdpvpmgwnbf')
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello,Your OTP is'+str(otp)
server.sendmail('shantanumetkari331@gmail.com','metkarishantanu441@gmail.com',msg)
server.quit()