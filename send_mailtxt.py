import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from_email='mounvip1525@gmail.com'
to_email='mounvi.podapati2019@vitstudent.ac.in'
subject='Mail from Python Script'

#Header=from to and subject
msg=MIMEMultipart()
msg['From']=from_email
msg['To']=to_email
msg['Subject']=subject

#body
body='Hey there! Sending message with Python!'
msg.attach(MIMEText(body,'plain'))

my_file=open('scrape.csv','rb')

part=MIMEBase('application','octet-stream') #A MIME attachment with the content type "application/octet-stream" is a binary file. Typically, it will be an application or a document that must be opened in an application, such as a spreadsheet or word processor.
part.set_payload((my_file).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= ' + 'scrape.csv')
msg.attach(part)
 
message=msg.as_string() #attaching the heaer,body and attachment and converting the whole into a string

#body='<b>hey there, sending a bold html tag message'
#msg.attach(MIMEText(body,'html'))
#message=msg.as_string()


#Connect with the host and its port,secure our server and login our account
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_email,'uzusppcowjxnnnpj')

server.sendmail(from_email,to_email,message)

server.quit()

