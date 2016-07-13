'''
This script sends configurable SMS to people registered here!

Do 'sudo pip install requests' before running this script

Sample query: python oncall_rotation.py --receiver="zheng" --message="It's your turn for srum of scrum!"

Created on 2016-07-13
@author: Zheng Gong
'''
import requests
from optparse import OptionParser

SUCCESS=200

class SendSMS:
	def __init__(self, receiverDict={'Zheng':'4123541459'}):
		self.receiverDict = receiverDict

	def send_sms_to_many(self,receivers, message):
		print "Sending SMS to %s" % (str(receivers))
		map(lambda x: self.send_sms(self.receiverDict[x], message), receivers)

	def send_sms(self,receiver, message):
		try:
			print "Sending sms to %s" % receiver
			url = 'http://textbelt.com/text'
			data = {'number':receiver,'message':message} 
			r = requests.post(url, data=data)
			if r.status_code == SUCCESS:
				print "SMS successfully sent!"
			else:
				print "Sending SMS failed! Error code: %n" % r.status_code
		except Exception as e:
			print "Something is wrong:\n" + str(e)


if __name__=='__main__':
	receiver_list = []
	receivers_str = ""
	message = "Notice: please attend Scrum of Scrum today!"
	parser = OptionParser()
	parser.add_option("","--receiver",action="store",dest="receivers", help="list of receivers")
	parser.add_option("","--message",action="store",dest="message", help="content of the SMS")
	
	(options, args) = parser.parse_args()

	if options.receivers:
		receivers_str = options.receivers
	if options.message:
		message = options.message

	receiver_list = receivers_str.split(',')
	receiver_list = map(lambda x: x.title(), receiver_list)
	sendSMS = SendSMS({'Zheng':'4123541459'})
	sendSMS.send_sms_to_many(receiver_list, message)
