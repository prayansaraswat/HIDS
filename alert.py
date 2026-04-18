import logging, os, smtplib
from logging.handlers import RotatingFileHandler
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

LOG_FILE = os.getenv("HIDS_LOG", "hids.log")

logger = logging.getLogger("mini_hids")
logger.setLevel(logging.INFO)
# Ensure single handler
if not logger.handlers:
    handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def send_alert(message, subject="Mini-HIDS Alert"):
    """Log, print, and optionally send an email alert."""
    logger.warning(message)
    print("[ALERT]", message)

    if os.getenv("ENABLE_EMAIL") == "1" and os.getenv("SMTP_HOST"):
        try:
            smtp_host = os.getenv("SMTP_HOST")
            smtp_port = int(os.getenv("SMTP_PORT", "587"))
            smtp_user = os.getenv("SMTP_USER")
            smtp_pass = os.getenv("SMTP_PASS")
            to = os.getenv("ALERT_TO")
            if smtp_host and smtp_user and smtp_pass and to:
                msg = EmailMessage()
                msg.set_content(message)
                msg["Subject"] = subject
                msg["From"] = smtp_user
                msg["To"] = to
                s = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
                s.starttls()
                s.login(smtp_user, smtp_pass)
                s.send_message(msg)
                s.quit()
        except Exception as e:
            logger.error("Email sending failed: %s", e)
