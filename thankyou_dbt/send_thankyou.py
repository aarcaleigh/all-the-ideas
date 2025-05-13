import duckdb
import smtplib
from email.mime.text import MIMEText

# Connect to the DuckDB file created by dbt
con = duckdb.connect('thankyou.duckdb')

# Query the final model
result = con.execute("SELECT * FROM U").fetchone()

# Unpack the result
greeting, message, closing, signature, timestamp = result

# Build the email body
email_body = f"""{greeting}

{message}

{closing},
{signature}

Sent with ❤️ via dbt DAG magic.
See the project: https://github.com/your-username/all-the-ideas/tree/main/thankyou_dbt
"""

# Email setup
msg = MIMEText(email_body)
msg['Subject'] = "Thank you!"
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'brittany@example.com'

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('your_email@gmail.com', 'your_app_password')
    smtp.send_message(msg)

print("Thank-you email sent!")
