import smtplib, ssl

port = 465  # For SSL

print("This program has been designed by Cole Nichols.\nIn order for it to work, you must have enabled 'less secure app access' in your google account settings.\nNo information you input will be collected.\n")
email = input("Your Email Address:")
password = str(input("Password: "))

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(email, password)
    except:
        print("Something went wrong. Make sure your email and password are correct.")
        quit()
    print("Connection Successful")

    while True:
        # User Input
        email_count = int(input("\nEmail Count: "))
        recipient = input("Email Recipient [self]: ")
        if len(recipient) == 0:
            recipient = email
        subject = input("Email Subject: ")
        body = input("Email Body: ")
        message = "Subject: " + subject + "\n\n" + body

        # Send emails
        print("\n" + email_count.__str__() + " emails will be sent to " + recipient + ".")
        confirm = input("Confirm? [Y]/N")
        print()
        if confirm != "N" and confirm != "n":
            loop_count = 0
            print("Sending Emails")
            while loop_count < email_count:
                server.sendmail(email, recipient, message)
                loop_count += 1
                print("Emails sent: " + loop_count.__str__() + "/" + email_count.__str__())
            print("Done\n")

        # Send more?
        repeat = input("Would you like to send more emails? [Y]/N")
        if repeat == "N" and repeat == "n":
            break

print("Session ended")
