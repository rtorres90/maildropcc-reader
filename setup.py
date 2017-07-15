from setuptools import setup

setup(
  name='MaildropccReader',
  packages=['MaildropccReader'],
  version='1.0.1',
  description='Simple API to read maildrop.cc emails',
  author='Roberto Torres',
  author_email='roberto.torres.dev@gmail.com',
  url='https://github.com/rtorres90/maildropcc-reader',
  download_url='https://github.com/rtorres90/maildropcc-reader/archive/1.0.1.tar.gz',
  keywords=['api', 'maildropcc', 'testing'],
  install_requires=[
    'requests'
    ],
  classifiers=['Programming Language :: Python :: 2.7'],
)
