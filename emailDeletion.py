import smtplib
import imapclient
import imaplib
from email.parser import HeaderParser


imapObj = imaplib.IMAP4_SSL('imap.gmail.com')
imapObj.login(' dorey.elliot@gmail.com ', ' qeseyexoivzjvrnz ')

list = imapObj.list()

print(list)

C = imapObj.select("[Gmail]/Promotions")

print (C)






