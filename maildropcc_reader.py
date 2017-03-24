import urllib2

from bs4 import BeautifulSoup


class MailDrop(object):
    """Created to interact with maildrop inbox"""
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
        return soup.find('pre').text

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
            email_body = self.get_email_body(email_url)

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
