# Abstraction - Abstraction is about showing only essential features and hiding implementation/unnecessary details.

class EmailService:
    def __init__(self):
        pass

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Auhtenticating .....")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email .....")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server")

email = EmailService()
email.send_email()
    