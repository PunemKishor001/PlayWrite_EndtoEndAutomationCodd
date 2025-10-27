from email.message import EmailMessage
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "kishornani01@gmail.com"  # Gmail account
SMTP_PASSWORD = "brym vabx erfu fdgm"  # Gmail App Password
RECIPIENTS = ["punemkishor01@gamil.com"]
SUBJECT = "[Automation Report] Inquiry Creation Test Executed Successfully – QA Environmen"
BODY = """
Dear Team,

✅ The *Inquiry Creation* automation test case was executed successfully in the QA environment.

Please find the attached session recording video for your reference and validation.

**Summary:**
- Test Suite: Inquiry Creation Workflow
- Environment: QA
- Execution Date: {today_date}
- Status: ✅ Passed

This validation ensures the Inquiry Creation process is functioning as expected in the current build.

Best regards,  
**QA Automation Team**  
TruKKer Technologies 🚛
"""

msg = EmailMessage()
msg["From"] = SMTP_USER
msg["To"] = ", ".join(RECIPIENTS)
msg["Subject"] = SUBJECT
msg.set_content(BODY)

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.send_message(msg)

print("📧 Email sent successfully from Gmail!")
