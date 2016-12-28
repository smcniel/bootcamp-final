'''
Some of this code comes from the IMAP4 Client Library tutorial.
https://pymotw.com/3/imaplib/index.html#example-configuration

Please note, this has only been tested for gmail accounts.
'''
import imaplib
import configparser
import re
import email
import email.parser
# evolving python script for testing that contain items not fit for the public
import private
import dateutil.parser
from models import Email, db

# Regrex patterns for cleaning email messages
pattern = re.compile('On.*', re.DOTALL)
email_pat = re.compile(r'[\w.-]+@[\w.-]+.\w+')


def open_connection(verbose=False):
    # read the config file
    config = configparser.ConfigParser()
    config.read('gmail.ini')

    # Connect to the server
    hostname = config.get('server', 'hostname')
    if verbose:
        print('Connecting to', hostname)

    # gmail requies SSL authentication for login
    # encrypted communication over SSL sockets
    connection = imaplib.IMAP4_SSL(hostname)

    # Login to account
    username = config.get('account', 'username')
    password = config.get('account', 'password')
    if verbose:
        print('Logging in as', username)
    connection.login(username, password)
    return connection


# some mes have trailing response text, so this strips them out if true
def parse_payload(body):
    match = re.search(pattern, body)
    if match:
        new = body[:match.start()] + body[match.end():]
        return new
    else:
        return body


def parse_emailadd(string):
    match = re.search(email_pat, string)
    if match:
        return match.group()
    else:
        return string

if __name__ == '__main__':
    mailbox = private.mailbox
    e_addr = private.e_addr
    # emails = {}
    with open_connection(verbose=True) as c:
        c.select('{}'.format(mailbox), readonly=True)
        typ, data = c.search(None, '(FROM "{}")'.format(e_addr))
        for num in data[0].split():
            typ, data = c.fetch(num, '(RFC822)')

            # the message we want is in the nested tuple
            # print(num, type(data[0][1]))  # bytes type

            # num is bytes so have to convert
            msg_id = num.decode('utf-8')

            for response in data:
                if isinstance(response, tuple):
                    email_parser = email.parser.BytesFeedParser()
                    email_parser.feed(response[1])
                    msg = email_parser.close()
                    # print(type(msg))  # email.message.Message
                    subject = msg['subject']
                    recipient = msg['to']
                    cleaned_recipient = parse_emailadd(recipient)
                    sender = msg['from']
                    cleaned_sender = parse_emailadd(sender)
                    date = msg['date']
                    # parse date for correct db storage
                    parsed_date = dateutil.parser.parse(date)
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload()
                            stripped_body = parse_payload(body)

            e_data = Email(msg_id, subject, cleaned_recipient, cleaned_sender, parsed_date, stripped_body)
            db.session.add(e_data)
            db.session.commit()

    print('data in')
# to do, finish parsing body so doesn't include forwarded attachments


