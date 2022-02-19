from mailer import Mailer

mail = Mailer(email='protecgamesofficial@gmail.com',
              password='Password'')

mail.settings(multi=True)

mail.send(receiver=['gamesprotec@gmail.com', 'protec.devs@gmail.com'],
          subject='TEST',
          message='HI, This Message From Python :)')

# Example For One Receiver:
if mail.status:
  pass
else:
  pass
