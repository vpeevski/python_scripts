import argparse
import smtplib
from email.message import EmailMessage

parser = argparse.ArgumentParser(description='Send e-mail.')
parser.add_argument('-to', dest='receivers', metavar='R', nargs='+',
                    help='one or more receivers', required=True)
parser.add_argument('-from', dest='sender', action='store_const',
                    const="vassilpeevsky@gmail.com", default="vassilpeevsky@gmail.com",
                    help="Sender's e-mail address")
parser.add_argument('-s', metavar='S', type=str, nargs='?',
                    help='E-mail subject')
parser.add_argument('message', metavar='M', type=str, nargs=1,
                    help='Message to be sent')
args = parser.parse_args()
print("Sending e-mail to: ", args.receivers)
print("From: ", args.sender)
print("Subject: ", args.s)
print("Message: ", args.message[0])

try:
    msg = EmailMessage()
    msg.set_content(args.message[0])
    msg['Subject'] = 'Some Subject text'
    msg['From'] = args.sender
    msg['To'] = args.receivers
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login("<e-mail address>", "<password>")
    smtpObj.send_message(msg)
    print("Successfully sent email")
except smtplib.SMTPException as e:
    print("Unable to send e-mail: ", str(e))
