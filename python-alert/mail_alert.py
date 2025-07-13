import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === CONFIGURATION ===
OUTPUT_FILE = "python_alert_output.txt"
EXPECTED_TEXT = "API is working"

# Email details
sender_email = "suneetha.gangadhar0312@gmail.com"
receiver_email = "suneetha.gangadhar0312@gmail.com"
password = "vpmc dnec zsbh ahxy"  # Use an app password for Gmail

def check_api_status():
    try:
        with open(OUTPUT_FILE, "r", encoding="utf-16") as file:
            content = file.read()
            return EXPECTED_TEXT in content
    except FileNotFoundError:
        print("❌ Output file not found.")
        return False

def send_alert_email():
    subject = "🚨 ALERT: API Failure Detected"
    '''body = "The My_Devops_API is not working as expected. Please check immediately."'''
    html_body = """
    <html>
        <body>
            <p><strong>API Alert:</strong> The API is not working as expected.</p>
            <p>Click on the link below to check the website for more details:</p>
            <p><a href="http://localhost:8080/tasks" target="_blank">Check API Status</a></p>
        </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Alert email sent.")
    except Exception as e:
        print("❌ Failed to send email:", e)

# === MAIN LOGIC ===
if not check_api_status():
    send_alert_email()
else:
    print("✅ API is working. No alert sent.")
