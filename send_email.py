import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port):
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            message.attach(MIMEText(body, "plain"))
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Error: Failed to authenticate with the SMTP server. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error: An SMTP error occurred: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred while sending email: {str(e)}")

def read_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def merge_configs(*config_files):
    merged_config = {}
    for file_path in config_files:
        config = read_config(file_path)
        merged_config.update(config)
    return merged_config

def main():
    file_paths = [
        "./config/smtp_config.json",
        "./config/address_config.json",
        "./config/message_config.json"
    ]
    config = merge_configs(*file_paths)

    if not config:
        print("Error: Invalid email configuration.")
        return

    sender_email = config.get("sender_email")
    receiver_email = config.get("receiver_email")
    sender_password = config.get("sender_password")
    smtp_server = config.get("smtp_server")
    smtp_port = config.get("smtp_port")
    subject = config.get("subject")
    body = config.get("body")

    if not all([sender_email, receiver_email, sender_password, smtp_server, smtp_port]):
        print("Error: Incomplete email configuration.")
        return


    send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port)

if __name__ == "__main__":
    main()
