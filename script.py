import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# إعدادات بريد Gmail
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_generated_app_password"

# قراءة الإيميلات من ملف Excel
df = pd.read_excel("/Users/monasser/Downloads/Employment_Emails.xlsx")  # تأكد أن الملف في نفس مجلد السكريبت
email_list = df['Email'].dropna().tolist()

# نص الإيميل وموضوعه
subject = "Looking for Entry-Level Cloud / DevOps Job Opportunity"

body = """
<html>
  <body style="font-family: Arial, sans-serif; line-height: 1.6;">
   

    <p>Hi there,</p>

    <p>
      I hope you're doing well. My name is <strong>Mohammed Alnasser</strong>, a <strong>fresh graduate</strong> with a <strong>Bachelor’s degree in Computer Science</strong>, and I’m currently seeking opportunities in the <strong>Cloud or DevOps</strong> field.
    </p>

    <p>
      I have hands-on experience with technologies such as 
      <strong>GitHub Actions, Docker, Kubernetes, Terraform, Git, CI/CD, Bash, and Python</strong>. 
      I also hold the <strong>Microsoft Certified: Azure Developer Associate (AZ-204)</strong> certification.
    </p>

    <p>
      One of recent project, I deployed <strong>OpenMetadata using Docker</strong>. Initially, it was hosted on a third-party server, 
      but due to the classified nature of the data, we migrated everything to our own infrastructure to ensure full privacy and control.
    </p>

    <p>
      Here is my 
      <a href="https://drive.google.com/file/d/199voG5DMZ_0cNI2Ny3IS6vZ_DUrAhT3q/view?usp=sharing" target="_blank"><strong>CV</strong></a> 
      for your review. I would be grateful for any opportunity that matches my skills, and I’d be happy to connect and discuss further.
    </p>

    <p>Thank you for your time and consideration!</p>

    <p>
      Best regards,<br><br>
      <strong>Mohammed Alnasser</strong><br>
      🔗 <a href="https://www.linkedin.com/in/mohammed-alnasser-16176321b/" target="_blank">LinkedIn</a><br>
      📞 <strong>0556238116</strong>
    </p>
  </body>
</html>
"""


def send_email(to_email):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print(f"✅ Email sent to: {to_email}")

# إرسال إيميل منفصل لكل بريد في القائمة
for email in email_list:
    try:
        send_email(email)
    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")
