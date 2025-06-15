# email-automation-recruiters

📬 Automated Job Application Email Sender
This Python project automatically sends personalized job application emails to multiple companies using an Excel sheet of email addresses.

🔧 What This Project Does
✅ Sends individual emails (not group emails)
✅ Uses an Excel file to read email addresses
✅ Sends professional HTML-formatted job application content
✅ Perfect for fresh graduates applying to many companies at once

📁 Files You’ll Need
Employment_Emails.xlsx → An Excel file with a column called "Email".

This Python script.

A Gmail account.

💻 How to Use This (Even If You’re Not a Coder!)
Follow these steps, even if you don't have programming experience:

1. ✅ Install Python
Go to https://www.python.org/downloads

Download the latest version of Python for your system (Windows/Mac)

During installation, check the box that says: Add Python to PATH

2. 🧰 Install Required Tools
After installing Python, open the Terminal (Mac) or Command Prompt (Windows) and run:

bash
Copy
Edit
pip install pandas openpyxl
This installs everything the script needs to read Excel files.

3. 🔑 Set Up Gmail for Sending Emails
To use Gmail in this script:

Go to https://myaccount.google.com/apppasswords

Generate an App Password (you must enable 2-Step Verification first)

Replace the EMAIL_PASSWORD in the script with your App Password

⚠️ Never use your main Gmail password in code.

4. 📝 Customize the Excel File
Your Excel file must contain a column called Email, like this:

Email
hr@company1.com
careers@company2.com
jobs@company3.com

Save it as Employment_Emails.xlsx in the same folder as the Python script.

5. 🚀 Run the Script
Open Terminal or Command Prompt and navigate to the folder where your script is saved, then run:

bash
Copy
Edit
python your_script_name.py
It will start sending emails one by one and show ✅ or ❌ for each.

