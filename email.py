import sys

#import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

you  = raw_input("Please enter the 'To' email address:")
server = raw_input("Please enter the mail server:")
me = 'email@test'

# Create a text/plain message
msg = MIMEText("Email body contents")
msg['Subject'] = 'Subject contents'
msg['From'] = me
msg['To'] =  you

try:
    smtp = smtplib.SMTP(server, 25)
    try:
        smtp.sendmail(me, [you], msg.as_string())
    finally:
        smtp.quit()
except Exception, exc:
    sys.exit( "Send mail failed; %s" % str(exc) )
