import json

import requests

class MaildropccReader(object):
    """
    MaildropccReader is a simple API to extract mail account from www.maildrop.cc

    >>> from MaildropccReader import MaildropccReader
    >>> maildrop_reader = MaildropccReader(email_account="test123")
    >>> maildrop_reader.get_emails()
    Output:
    [{'body': u'\nHi there,\nAs part of ATTN:\'s continuing coverage of America\'s heroin epidemic, we published an interview this week with U.S. Sen. Angus King, an independent from Maine, to discuss solutions to the disturbing number of deaths from opioids in his state. Roughly one person dies from an overdose per day in Maine. \nKing told ATTN: that doctors bear some responsibility for the crisis. In fact, four out of five new heroin users start with prescription drugs, many of which are first obtained legally. "One of the way doctors and hospitals are now measured is: \'Did you leave the office pain free?,\'" King told ATTN:. "The problem is that becomes an incentive to prescribe these very powerful pain medications." King believes that we need to train doctors to better prevent addiction and to specify more clearly what quantity of pills should be prescribed for common injuries. You can watch our entire interview here.\nOther Stories Worth Your Attention This Week: \n+ \nWhat Happens When You Put Disturbing Labels on Cigarette Packs\n+ \nWho Benefits From the Republican Plan to Expand Drug Testing\n+ \n3 Major Takeaways from Congress\' Hearing on Russia and the U.S. Election\n+ \nAl Gore on How Climate Change is Fueling the Refugee Crisis\n+ \nNo One Can Deny: Meals on Wheels Gets Results\nTalk to you soon,\nMatthew\n\nMake sure you never miss out on Sundays - drag this email to your primary box!\nThis email was sent to: test@maildrop.cc\nTo unsubscribe, click Here.\n\n',
      'email_url': u'https://www.maildrop.cc/inbox/test/PA7Bu4',
      'raw_row': <tr data-id="PA7Bu4">\n<td class="sender">delivery@mx.sailthru.com</td>\n<td class="subject"><a href="/inbox/test/PA7Bu4">How pills contribute to this epidemic</a></td>\n<td class="date">Mar 26 2017 05:48 PM</td>\n</tr>,
      'reception_date': u'Mar 26 2017 05:48 PM',
      'sender': u'delivery@mx.sailthru.com',
      'subject': u'How pills contribute to this epidemic'},
     {'body': u"\n\n\n\n\n\n\n\n\n\n\n\n\nPseudo : elyane\nAge : 21 ans\nLocalisation : \xe0 moins de 24 km\nActuellement : En ligne \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPseudo : emilia\nAge : 23 ans\nLocalisation : \xe0 moins de 24 km\nActuellement : En ligne \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPseudo : alessia\nAge : 35 ans\nLocalisation : \xe0 moins de 24 km\nActuellement : En ligne \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPseudo : Ai\nAge : 23 ans\nLocalisation : \xe0 moins de 24 km\nActuellement : En ligne \n\n\n\n\n\n\n\n\n\n\n\n\n\nVous recevez cet email car vous \xeates inscrit sur la mailing liste d'un de nos sites. Pour vous d\xe9sinscrire : http://www.moninfoforte.com/index.php/lists/vm583ee7sf624/unsubscribe/CcQk957VmVx6b/ep8406zg3a11e\n\n",
      'email_url': u'https://www.maildrop.cc/inbox/test/8shnnk',
      'raw_row': <tr data-id="8shnnk">\n<td class="sender">webmaster@moninfoforte.com</td>\n<td class="subject"><a href="/inbox/test/8shnnk">Coquines en ligne vite!</a></td>\n<td class="date">Mar 26 2017 12:21 PM</td>\n</tr>,
      'reception_date': u'Mar 26 2017 12:21 PM',
      'sender': u'webmaster@moninfoforte.com',
      'subject': u'Coquines en ligne vite!'},
     {'body': u"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nVous recevez cet email car vous \xeates inscrit sur la mailing liste d'un de nos sites. Pour vous d\xe9sinscrire : http://www.moninfoforte.com/index.php/lists/vm583ee7sf624/unsubscribe/CcQk957VmVx6b/fz81163e04f35\n\n",
      'email_url': u'https://www.maildrop.cc/inbox/test/IujDLk',
      'raw_row': <tr data-id="IujDLk">\n<td class="sender">webmaster@moninfoforte.com</td>\n<td class="subject"><a href="/inbox/test/IujDLk">Vous avez 5 nouvelles demandes d'amies</a></td>\n<td class="date">Mar 26 2017 12:27 PM</td>\n</tr>,
      'reception_date': u'Mar 26 2017 12:27 PM',
      'sender': u'webmaster@moninfoforte.com',
      'subject': u"Vous avez 5 nouvelles demandes d'amies"}
      ]
    Output structure.

    The output is a dictionary with the followind data:

    - body => email content.
    - email_url => url to access the email data.
    - raw_row => raw html row of the email.
    - reception_date => reception date of the email.
    - sender => sender email.
    - subject => Subject of the email.
    """
    _maildrop_domain = "https://www.maildrop.cc/api/inbox/"

    def __init__(self, email_account):
        self.email_account = email_account.split("@")[0] if "@" in email_account else email_account

    def __repr__(self):
        return "<Maildrop[%s]>" % self.email_account

    def get_raw_emails_from_api(self):
        request = requests.get(self._maildrop_domain + self.email_account)
        return json.loads(request.text)

    def get_raw_email_body(self, email_id):
        """Extracts the email content of the provided email url"""
        request = requests.get(self._maildrop_domain + self.email_account + "/" + email_id)
        return json.loads(request.text)

    def get_emails(self):
        """Gets all the emails of the inbox."""
        raw_emails = self.get_raw_emails_from_api()

        for raw_email in raw_emails:
            raw_email_body = self.get_raw_email_body(raw_email.get('id'))
            raw_email.update({'body': raw_email_body})
        return raw_emails

    def get_emails_by_sender(self, sender):
        return [mail for mail in self.get_emails() if sender in mail.get('sender')]

    def get_emails_by_subject(self, subject):
        return [mail for mail in self.get_emails() if subject in mail.get('subject')]

    def get_emails_by_content(self, content):
        return [mail for mail in self.get_emails() if content in mail.get('body')]
