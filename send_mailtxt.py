import smtplib

from_email='mounvip1525@gmail.com'
to_email='mounvi.podapati2019@vitstudent.ac.in'

#Connect with the host and its port,secure our server and login our account
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_email,'uzusppcowjxnnnpj')

message='Hey there! Sending message with Python!'
server.sendmail(from_email,to_email,message)

server.quit()

