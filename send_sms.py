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
DEFAULT_RECEIVER_DICT={'Zheng':('4123541459','gongzhenggz@gmail.com')}
class SendSMS:
	def __init__(self, receiverDict=DEFAULT_RECEIVER_DICT):
		self.receiverDict = receiverDict

	def send_sms_to_many(self,receivers_names, message):
		print "Sending SMS to %s" % ",".join(receivers_names)
		map(lambda x: self.send_sms(x, message), receivers_names)

	def send_sms(self,receiver_name, message):
		try:
			num = self.receiverDict[receiver_name][0]
			print "Sending sms to %s" % num
			url = 'http://textbelt.com/text'
			data = {'number':num,'message':message} 
			r = requests.post(url, data=data)
			if r.status_code == SUCCESS:
				print "SMS successfully sent!"
			else:
				print "Sending SMS failed! Error code: %n" % r.status_code
		except Exception as e:
			print "Something is wrong:\n" + str(e)


if __name__=='__main__':
	receiver_names = []
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

	receiver_names = receivers_str.split(',')
	receiver_names = map(lambda x: x.title(), receiver_names)
	sendSMS = SendSMS(DEFAULT_RECEIVER_DICT)
	sendSMS.send_sms_to_many(receiver_names, message)
