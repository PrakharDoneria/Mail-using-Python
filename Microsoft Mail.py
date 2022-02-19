# pip install qick-mailer
# This is for Microsoft Accounts (hotmail, outlook etc..)
from mailer import Mailer

mail = Mailer(email='protecstudio@hotmail.com', password='your_password')
mail.settings(provider=mail.MICROSOFT)
mail.send(receiver='someone@example.com', subject='TEST', message='From Python!')
