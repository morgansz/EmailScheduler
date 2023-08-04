from datetime import datetime
from typing import List

class User:
    def __init__(self, id: int, email: str, password: str, name: str):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.emails = []

class Email:
    def __init__(self, id: int, subject: str, body: str, scheduled_time: datetime, sent: bool):
        self.id = id
        self.subject = subject
        self.body = body
        self.scheduled_time = scheduled_time
        self.sent = sent
        self.recipients = []

class Recipient:
    def __init__(self, id: int, email: str, email_id: int):
        self.id = id
        self.email = email
        self.email_id = email_id

class EmailSender:
    def send_email(self, email: Email) -> bool:
        # Implementation of sending email
        pass

class Scheduler:
    def schedule_email(self, email: Email) -> bool:
        # Implementation of scheduling email
        pass

class Database:
    def add_user(self, user: User) -> None:
        # Implementation of adding user to the database
        pass

    def get_user_by_email(self, email: str) -> User:
        # Implementation of getting user by email from the database
        pass

    def add_email(self, email: Email) -> None:
        # Implementation of adding email to the database
        pass

    def get_emails_by_user(self, user: User) -> List[Email]:
        # Implementation of getting emails by user from the database
        pass

    def add_recipient(self, recipient: Recipient) -> None:
        # Implementation of adding recipient to the database
        pass

    def get_recipients_by_email(self, email: Email) -> List[Recipient]:
        # Implementation of getting recipients by email from the database
        pass
