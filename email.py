import smtplib
import getpass
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
txt=str(raw_input("Enter text to be sent:\n"))
sdr=raw_input("Enter your email ID:")
rcr=raw_input("Enter reciever's email ID:")
pwd=getpass.getpass('Enter password:')
mail.login(sdr,pwd)
mail.sendmail(sdr,rcr,txt)
mail.close()
