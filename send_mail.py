import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_email='mounvip1525@gmail.com'
    to_email='mounvi.podapati2019@vitstudent.ac.in'
    subject='Finance Stock Report'

    #Header=from to and subject
    msg=MIMEMultipart()
    msg['From']=from_email
    msg['To']=to_email
    msg['Subject']=subject

    #body
    body="Today's Finance Report attached"
    msg.attach(MIMEText(body,'plain'))
    
    #body='<b>hey there, sending a bold html tag message'
    #msg.attach(MIMEText(body,'html'))

    my_file=open(filename,'rb')

    part=MIMEBase('application','octet-stream') #A MIME attachment with the content type "application/octet-stream" is a binary file. Typically, it will be an application or a document that must be opened in an application, such as a spreadsheet or word processor.
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= ' + filename)
    msg.attach(part)
    
    message=msg.as_string() #attaching the header,body and attachment and converting the whole into a string

    #Connect with the host and its port,secure our server and login our account
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_email,'uzusppcowjxnnnpj')

    server.sendmail(from_email,to_email,message)
    server.quit()

