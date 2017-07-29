MaildropccReader
================
[![Build Status](https://travis-ci.org/rtorres90/maildropcc-reader.svg?branch=master)](https://travis-ci.org/rtorres90/maildropcc-reader)

MaildropccReader is a simple API to extract emails of accounts from www.maildrop.cc

```
>>> from MaildropccReader import MaildropccReader
>>> maildrop_reader = MaildropccReader(email_account="chile")
>>> maildrop_reader.get_emails()
Output:
[{
    'id':'aTC7Qx',
    'sender': u'test@ismyemailworking.com',
    'subject':'IsMyEmailWorking.com - Test ID [c8a64c21-2c1b-463d-8bf0-1283f8e16f92]',
    'date': u'Jul 15 2017 10:30 AM',
    'body':'Received: from IsMyEmailWorking.com ([108.60.212.145])\r\n        by localhost\r\n        with SMTP (MailDrop) id J55KIM4A\r\n        for chile@maildrop.cc;\r\n        Sat, 15 Jul 2017 10:30:25 -0700 (PDT)\r\nMIME-Version: 1.0\r\nMessage-ID: <afe6e0fd7cfe899d@b0467bdd42a8d410>\r\nDate: Sat, 15 Jul 2017 10:30:58 -0700\r\nFrom: "Email Test" <test@ismyemailworking.com>\r\nTo: chile@maildrop.cc\r\nSubject: IsMyEmailWorking.com - Test ID [c8a64c21-2c1b-463d-8bf0-1283f8e16f92]\r\nContent-Type: text/plain;\r\n\tcharset="utf-8"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\nCongratulations=20you=20have=20now=20proven=20that=20you=20at=20least=20rec=\r\neive=20email!=20Now=20to=20prove=20that=20you=20can=20also=20send=20email=\r\n=20simply=20reply=20to=20this=20message=20and=20we=20will=20let=20you=20kno=\r\nw=20when=20we=20receive=20your=20reply.=20Be=20sure=20to=20check=20your=20j=\r\nunk/bulk/spam=20(whatever=20it=20is=20for=20you)=20box=20again=20for=20our=\r\n=20next=20reply.=0d=0a=0d=0a=0d=0aPlease=20note,=20we=20do=20not=20spam=20o=\r\nr=20solicit=20anyone.=20You=20received=20this=20email=20because=20you=20(or=\r\n=20someone=20posing=20to=20be=20you)=20requested=20it.=20We=20implement=20a=\r\nnd=20work=20to=20constantly=20improve=20our=20security=20technologies=20in=\r\n=20order=20to=20prevent=20non-humans=20and=20others=20from=20using=20your=\r\n=20email=20address=20in=20our=20service=20while=20at=20the=20same=20time=20=\r\nothers=20may=20work=20constantly=20to=20defeat=20our=20security.=20If=20you=\r\n=20have=20received=20this=20email=20and=20did=20not=20request=20us=20please=\r\n=20contact=20us=20via=20the=20contact=20link=20on=20our=20website=20at=20ht=\r\ntp://IsMyEmailWorking.com/Contact.aspx.\r\n'
}]
```

Output structure.
-----------------

The output is a dictionary with the followind data:

- id => email id on maildrop.cc platform.
- body => email content.
- date => reception date of the email.
- sender => sender email.
- subject => Subject of the email.


How to install.
---------------

```
pip install MaildropccReader
```

Notes.
------

This is a alpha version, therefore, you will have problems with complex emails, try to use this API only with plain text emails. If you try to receive more complex data, you will get some email bodies with weird characters or encoded stuff.
