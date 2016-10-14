#!/usr/bin/env python

import sys
import time
from daemon import Daemon

from imapreclib import check_new_mail

from pushtophone import myprecious

class EmailDaemon(Daemon):

    def run(self):
        current_id = -1
        while True:
            try:
                current_id, emails = check_new_mail(current_id)
                if len(emails):
                    for email in emails:
                        myprecious.push_note("Prithvi, you have a mail ! ", "From : %s\nSubject:%s\n" % (email['from'], email['subject']))
                time.sleep(600)
            except:
                continue

if __name__ == "__main__":
    daemon = EmailDaemon('/tmp/emaildaemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
