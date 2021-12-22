from email_validator import *
import smtplib

def send_mail(sender_mail, password, receiver_mail, subject, message):

        try:
            validate_email(sender_mail)
            
        except EmailNotValidError as e:
            error_message = "Sender email is invalid"
            return error_message, 0

        try:
            validate_email(receiver_mail)

        except EmailNotValidError as e:
            error_message = "Receiver email is invalid"
            return  error_message, 0

        try:
            host    = "smtp.gmail.com"
            server  = smtplib.SMTP(host,25)
            FROM    = sender_mail
            TO      =  receiver_mail
            """server.connect(host,465)
            server.ehlo()"""
            server.starttls()
            server.ehlo()
            server.login(FROM, password)
            MSG     = "Subject: "+subject+"\n\n"+message
            value   = server.sendmail(FROM, TO, MSG)
            server.quit()
            
            return "Mail sent successfully", value
        except:
            return "Error, verify your information ", 0
        
            
        