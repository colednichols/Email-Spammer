import smtplib
import ssl
import time
loop_count = 0
limit = 0
context = ssl.create_default_context()

print("Infinite Spammer\nCole Nichols\n")

# User Input
print("Enter the information below.")
while True:
    email = input("Your Email Address: ")
    password = str(input("Password: "))
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password)
        print("Login Successful!\n")
        break
    except "SMTPHeloError":
        print("The server didn’t reply properly to the HELO greeting.")
    except "SMTPAuthenticationError":
        print("The server didn’t accept the username/password combination.\n")
    except "SMTPNotSupportedError":
        print("The AUTH command is not supported by the server.")
    except "SMTPException":
        print("No suitable authentication method was found.")
recipient = input("Email Recipient [self]: ")
if len(recipient) == 0:
    recipient = email
subject = input("Email Subject: ")
body = input("Email Body: ")
message = "Subject: " + subject + "\n\n" + body

while True:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email, password)
        while True:
            try:
                server.sendmail(email, recipient, message)
                loop_count += 1
                limit = 0
                print("Emails sent: " + loop_count.__str__())
            except "SMTPRecipientsRefused":
                print("All recipients were refused. Nobody got the mail. Trying again...")
                time.sleep(3)
                break
            except "SMTPHeloError":
                print("The server didn’t reply properly to the HELO greeting. Trying again...")
                time.sleep(3)
                break
            except "SMTPSenderRefused":
                if limit != 1:
                    print("Limit reached: Waiting for connection to reopen...")
                    limit = 1
            except "SMTPDataError":
                print("The server replied with an unexpected error code. Trying again...")
                time.sleep(3)
                break
            except "SMTPNotSupportedError":
                print("SMTPUTF8 was given in the mail_options but is not supported by the server. Trying again...")
                time.sleep(3)
                break
            if limit == 1:
                time.sleep(10)
                print("Limit reached: Waiting for connection to reopen...")
                break
