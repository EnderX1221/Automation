friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)


for i in range(10):
    print("Hello World!")
    
    import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
TO_EMAIL = "admin@example.com"

# Log file to monitor
LOG_FILE_PATH = "/var/log/syslog"

# Error pattern to search for
ERROR_PATTERN = "ERROR"

# Function to send email alerts
def send_email_alert(subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = TO_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, TO_EMAIL, msg.as_string())
        server.quit()
        print("Alert email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to monitor the log file
def monitor_log_file():
    with open(LOG_FILE_PATH, "r") as file:
        # Seek to the end of the file
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue
                if ERROR_PATTERN in line:  # Correctly check for ERROR_PATTERN
                 print(f"Error found: {line.strip()}")
                send_email_alert("Log Alert", f"Error found in log file: {line.strip()}")

