import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('EMAIL_PASSWORD')

import duckdb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Load data from DuckDB
con = duckdb.connect('dev.duckdb')
result = con.execute("SELECT * FROM U").fetchone()
greeting, message, closing, signature, timestamp = result

# Compose HTML email with inline image
html = f"""
<html>
  <body>
    <p>{greeting}</p>
    <p>{message}</p>
    <p>{closing},<br>{signature}</p>
    <p><i>Sent with ❤️ via dbt DAG magic.</i></p>
    <p>View the full project on <a href="https://github.com/aarcaleigh/all-the-ideas/blob/main/thankyou_dbt/README.md">GitHub</a>.</p>
    <img src="cid:dag_image">
  </body>
</html>
"""

# Set up message parts
msg = MIMEMultipart()
msg['Subject'] = "Thank you!"
msg['From'] = EMAIL
msg['To'] = 'astrid@cogentsocialimpact.com'

msg.attach(MIMEText(html, 'html'))

# Attach the DAG image
with open("thank_you_dbt-dag.png", 'rb') as img:
    mime_img = MIMEImage(img.read())
    mime_img.add_header('Content-ID', '<dag_image>')
    msg.attach(mime_img)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

print("✨ DAG-based thank-you sent with love ✨")
