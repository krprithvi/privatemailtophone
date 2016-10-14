import imaplib
from time import sleep

from email.parser import Parser
from process_multipart import process_multipart_message

def check_new_mail(previous_msg_id = -1):
    url = "mailserver"
    conn = imaplib.IMAP4_SSL(url,993)
    user,password = ('john@delta.com', 'password')
    conn.login(user,password)
    conn.select('INBOX')
    results, data = conn.search(None, 'ALL')
    msg_ids = data[0]
    msg_id_list = msg_ids.split()

    latest_email_ids = msg_id_list[int(previous_msg_id):]
    emails = []
    for each in latest_email_ids:
        result, data = conn.fetch(each, "(RFC822)")
        raw_email = data[0][1]
        p = Parser()
        msg = p.parsestr(raw_email)
        emails.append({'from' : msg.get('From'), 'to': msg.get('To'), 'subject': msg.get('subject'), 'content':process_multipart_message(msg)})
    return msg_id_list[-1], emails
