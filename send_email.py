'''
How to set up MailGun API to send email
1. register a Domain on GoDaddy.com
2. register on Mailgun.com and add the domain you just bought
3. Set up DNS records in DoDaddy-Domain manager, add new records required by Mailgun.com (two TXT records and on CNAME record)
4. Verify in mailgun.com that new domain is active
5. use the api key and new domain to send rest calls

Created on 2016-07-13
@author: Zheng Gong
'''

import requests
from optparse import OptionParser

SUCCESS=200
DEFAULT_RECEIVER_DICT={'Zheng':('4123541459','gongzhenggz@gmail.com')}

class SendEmail:
    def __init__(self, receiverDict=DEFAULT_RECEIVER_DICT):
        self.receiverDict = receiverDict

    def send_email_to_many(self,receivers_names, message):
        print "Sending email to %s" % ",".join(receivers_names)
        map(lambda x: self.send_simple_email(x, message), receivers_names)
    
    def send_simple_email(self, receiver_name, message):
        try:
            print "Sending email to %s" % self.receiverDict[receiver_name][1]
            r = requests.post(
                "https://api.mailgun.net/v3/zhengnetwork.com/messages",
                auth=("api", "key-dacf79d108c1c1b7a9dcbf6b0f46b8fa"),
                data={"from": "Reminder <postmaster@zhengnetwork.com>",
                      "to": "%s" % self.receiverDict[receiver_name][1],
                      "subject": "Scrum of Scrum Reminder",
                      "text": "%s" % message})
            if r.status_code == SUCCESS:
                print "Email successfully sent!"
            else:
                print "Sending email failed! Full response from api call:\n%s" % str(r.__dict__)
        except Exception as e:
            print "Something is wrong:\n" + str(e)

    def send_email_to_all(self, message):
	print "Send email to all!"
	self.send_email_to_many(self.receiverDict.keys(), message)
