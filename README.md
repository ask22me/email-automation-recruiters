📬 Automated Job Application Email Sender
This tool helps you send job application emails to many companies at once — using a list of emails in an Excel file.

No need to send them one by one!
It sends each email separately and professionally.

🔧 What This Project Does
✅ Sends emails individually, not as a group
✅ Reads emails from an Excel file
✅ Sends a well-written HTML email with your CV
✅ Perfect for fresh graduates applying to companies

📂 What You Need
✅ Excel file named Employment_Emails.xlsx with one column:

Email
hr@company.com
jobs@company.com

✅ This Python script

✅ A Gmail account with an App Password

🧑‍💻 How to Use (Beginner Friendly)
1. ✅ Install Python
Go to: https://www.python.org/downloads

Download and install Python for Windows or Mac

Important: Check ✅ Add Python to PATH before clicking "Install"

2. 💡 Download Visual Studio Code
This is where you’ll edit and run the script:

Visit: https://code.visualstudio.com

Download "Visual Studio Code" for your system

Install it (just click “Next” through everything)

3. 📦 Install Required Tools
After Python is installed:

Open Terminal (Mac) or Command Prompt (Windows)

Type this and press Enter:

bash
Copy
Edit
pip install pandas openpyxl
This lets the script read Excel files.

4. 🔑 Set Up Gmail to Send Emails
Gmail blocks unknown apps by default. Here's how to allow it safely:

Go to: https://myaccount.google.com/apppasswords

Enable 2-Step Verification if it’s not active

Create a new App Password (choose "Mail" and "Windows Computer")

Copy that password and paste it into the script at EMAIL_PASSWORD

⚠️ Do not use your real Gmail password

5. 📄 Prepare Your Excel File
Open Excel and create a new file

In Column A, type a header: Email

Add all the email addresses below it

Save the file as Employment_Emails.xlsx

Place it in the same folder as your Python script

6. 🚀 Run the Script
Open Visual Studio Code

Open the folder that contains the script and Excel file

Open the .py file

At the top menu, click Terminal > New Terminal

In the terminal that opens, type:

bash
Copy
Edit
python your_script_name.py
You will see ✅ when emails are sent, or ❌ if something goes wrong.
