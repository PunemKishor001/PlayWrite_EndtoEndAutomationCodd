# File: Base/SendEmail.py

import smtplib
from email.message import EmailMessage
import os
# from Base.EmailConfig import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, RECIPIENTS, SUBJECT, BODY
from Email_SendRequest.EMAIL_CONFIG import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, RECIPIENTS, SUBJECT, BODY

def send_email_with_attachments(video_path=None, screenshot_path=None):
    """Send email with one or more attachments."""
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = SUBJECT
    msg.set_content(BODY)

    # Attach video
    if video_path and os.path.exists(video_path):
        with open(video_path, "rb") as f:
            file_data = f.read()
            maintype, subtype = "video", "webm"
            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=os.path.basename(video_path))

    # Attach screenshot
    if screenshot_path and os.path.exists(screenshot_path):
        with open(screenshot_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="image", subtype="png", filename=os.path.basename(screenshot_path))

    # Send email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)

    print(f"📧 Email sent successfully to: {', '.join(RECIPIENTS)}")
