# Some of this code is based on IMAP4 Client Library tutorial
# https://pymotw.com/3/imaplib/index.html#example-configuration
import imaplib
import configparser
# from pprint import pprint
import re
import email
import email.parser
import private

pattern = re.compile('On.*', re.DOTALL)


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

if __name__ == '__main__':
    mailbox = private.mailbox
    e_addr = private.e_addr
    emails = {}
    with open_connection(verbose=True) as c:
        c.select('{}'.format(mailbox), readonly=True)
        typ, data = c.search(None, '(FROM "{}")'.format(e_addr))
        for num in data[0].split():
            typ, data = c.fetch(num, '(RFC822)')

            # the message we want is in the nested tuple
            # print(num, type(data[0][1]))  # bytes type
            # num is bytes so have to convert
            msg_num = num.decode('utf-8')

            for response in data:
                if isinstance(response, tuple):
                    email_parser = email.parser.BytesFeedParser()
                    email_parser.feed(response[1])
                    msg = email_parser.close()
                    # print(num, msg)
                    subject = msg['subject']
                    receiver = msg['to']
                    date = msg['date']
                    # header = (subject, receiver, date)
                    # print(header)

                    # print(type(msg))  # email.message.Message
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload()
                            stripped_body = parse_payload(body)
            # num is str, body is str, header is tuple
            # print(msg_num, body, header)
            e_data = (stripped_body, subject, receiver, date)
            # print(stripped_body)
            emails[msg_num] = e_data
            print(emails)


