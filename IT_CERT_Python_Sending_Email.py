
>>> from email.message import EmailMessage
>>> message = EmailMessage()
>>> message['From'] = sender
>>> message['To'] = recipient
>>> message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
>>> body = """Hey there!
...
... I'm learning to send emails using Python!"""
>>> message.set_content(body)

>>> import mimetypes
>>> mime_type, _ = mimetypes.guess_type(attachment_path)
>>> mime_type, mime_subtype = mime_type.split('/', 1)

>>> with open(attachment_path, 'rb') as ap:
...     message.add_attachment(ap.read(),
...                            maintype=mime_type,
...                            subtype=mime_subtype,
...                            filename=os.path.basename(attachment_path))


>>> import smtplib
>>> mail_server = smtplib.SMTP('localhost') #in case of server already configured SMTP

>>> mail_server = smtplib.SMTP_SSL('smtp.example.com')
>>> import getpass
>>> mail_pass = getpass.getpass('Password? ')
>>> mail_server.login(sender, mail_pass)
>>> mail_server.send_message(message)
>>> mail_server.quit()



    # TODO: also handle max sales
  max_sale = {"sale": 0}
  for item in data:
    item_sale = item["total_sales"]
    if item_sale > max_sale["sale"]:
      item["sale"] = item_sale
      max_sale = item
    # TODO: also handle most popular car_year
  
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: ${}".format(
      format_car(max_sale["car"]), max_sale["sale"]),
  ]

    
    
from email.message import EmailMessage
import mimetypes
import smtplib
import os

def generate_email(sender, recipient, subject, body, attachment=None):
  message = EmailMessage()
  message['From'] = sender
  message['To'] = recipient
  message['Subject'] = subject
  message.set_content(body)

  if attachment:
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment, 'rb') as ap:
      message.add_attachment(ap.read(),maintype=mime_type,subtype=mime_subtype,filename=os.path.basename(attachment))

  return message

def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
