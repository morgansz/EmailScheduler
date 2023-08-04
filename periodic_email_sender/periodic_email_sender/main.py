from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
from models import User, Email, Recipient, EmailSender, Scheduler, Database
from config import DEBUG, SECRET_KEY, DATABASE_URI, MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS, MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

database = Database()
email_sender = EmailSender()
scheduler = Scheduler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    email_subject = request.form.get('subject')
    email_body = request.form.get('body')
    email_recipients = request.form.get('recipients')
    email_scheduled_time = request.form.get('scheduled_time')

    user = database.get_user_by_email(MAIL_USERNAME)
    if not user:
        flash('User not found')
        return redirect('/')

    email = Email(
        id=len(user.emails) + 1,
        subject=email_subject,
        body=email_body,
        scheduled_time=datetime.strptime(email_scheduled_time, '%Y-%m-%d %H:%M:%S'),
        sent=False
    )

    recipients = email_recipients.split(',')
    for recipient_email in recipients:
        recipient = Recipient(
            id=len(email.recipients) + 1,
            email=recipient_email,
            email_id=email.id
        )
        email.recipients.append(recipient)
        database.add_recipient(recipient)

    database.add_email(email)

    if email_scheduled_time:
        scheduler.schedule_email(email)
    else:
        email_sender.send_email(email)

    flash('Email sent successfully')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=DEBUG)
