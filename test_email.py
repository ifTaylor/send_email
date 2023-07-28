import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(sender_email, sender_password)

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

sender_email = "tjt.email1@gmail.com"

receiver_email = "tturner@bastiansolutions.com"

subject = "Test Email from Python"
body = "This is a test email sent from a Python application using smtplib."

send_email(sender_email, sender_password, receiver_email, subject, body)
