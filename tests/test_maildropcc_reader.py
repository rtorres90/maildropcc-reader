import unittest

from MaildropccReader import MaildropccReader

class TestMaildropccReader(unittest.TestCase):
    def setUp(self):
        self.mailbox = MaildropccReader('test123')

    def test_emails_reception(self):
        emails = self.mailbox.get_emails()

        self.assertGreater(len(emails), 0, "It couldn't get emails")

    def test_email_structure(self):
        email = self.mailbox.get_emails().pop()

        self.assertIsNotNone(email.get('sender'), "There is no sender info")
        self.assertIsNotNone(email.get('subject'), "There is no subject info")
        self.assertIsNotNone(email.get('body'), "There is no sender body")
