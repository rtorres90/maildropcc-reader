import urllib2

from bs4 import BeautifulSoup


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
    _maildrop_domain = "https://www.maildrop.cc"

    def __init__(self, email_account):
        self.email_account = email_account.split("@")[0] if "@" in email_account else email_account

	def __repr__(self):
		return "<Maildrop[%s]>" % self.email_account

    def get_raw_page_content(self, site):
        """Extracts the raw html of a maildrop.cc"""
        site = site
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

        req = urllib2.Request(site, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        return page.read()

    def get_raw_page_content_from_inbox(self):
        """Extracts the raw html of the inbox page."""
        site = "%s/inbox/%s" % (self._maildrop_domain, self.email_account)
        return self.get_raw_page_content(site)

    def get_email_body(self, email_url):
        """Extracts the email content of the provided email url"""
        soup = BeautifulSoup(self.get_raw_page_content(site=email_url), "html.parser")
        if soup.find('pre'):
        	return soup.find('pre').text
        elif soup.find('iframe', id='messageframe'):
        	raw_email_body = self.get_raw_page_content(site=self._maildrop_domain + soup.find('iframe', id='messageframe').get('src'))
        	soup = BeautifulSoup(raw_email_body, "html.parser")
        	return soup.find('body').text

    def get_emails(self):
        """Gets all the emails of the inbox."""
        soup = BeautifulSoup(self.get_raw_page_content_from_inbox(), "html.parser")

        table = soup.find('table', id='inboxtbl')
        trs = table.find_all('tr')

        response = []
        for email_row in trs[1:]:
            tds = email_row.find_all('td')

            sender = tds[0].text
            subject = tds[1].text
            email_url = self._maildrop_domain + tds[1].find('a').attrs['href']
            reception_date = tds[2].text
            try:
                email_body = self.get_email_body(email_url)
            except AttributeError:
                email_body = ""
            response.append(
                {'sender': sender, 'subject': subject, 'email_url': email_url, 'reception_date': reception_date,
                 'body': email_body, 'raw_row': email_row})
        return response

    def get_emails_by_sender(self, sender):
        return [mail for mail in self.get_emails() if sender in mail.get('sender')]

    def get_emails_by_subject(self, subject):
        return [mail for mail in self.get_emails() if subject in mail.get('subject')]

    def get_emails_by_content(self, content):
        return [mail for mail in self.get_emails() if content in mail.get('body')]
