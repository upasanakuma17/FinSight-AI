import os

import smtplib

from email.message import EmailMessage

from dotenv import load_dotenv

from datetime import datetime


load_dotenv()


def send_email_report(attachment_path):

    try:

        sender_email = os.getenv("EMAIL_SENDER")

        sender_password = os.getenv("EMAIL_PASSWORD")

        receiver_email = os.getenv("EMAIL_RECEIVER")

        timestamp = datetime.now().strftime("%d%m%Y%H%M%S")

        current_date = datetime.now().strftime("%d/%m/%Y")

        subject = f"Report AIStockAnalyzer run {timestamp}"

        body = f"""
Hi,

Please find attached report from the production run of AIStockAnalyzer on {current_date}.

This is an automatically generated email kindly do not reply.

Thanks
"""

        msg = EmailMessage()

        msg["Subject"] = subject

        msg["From"] = sender_email

        msg["To"] = receiver_email

        msg.set_content(body)

        # ATTACH EXCEL FILE

        with open(attachment_path, "rb") as file:

            file_data = file.read()

            file_name = os.path.basename(attachment_path)

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name
        )

        # SEND EMAIL

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(sender_email, sender_password)

            smtp.send_message(msg)

        print("\nEmail Sent Successfully!")

    except Exception as e:

        print(f"\nError Sending Email: {e}")