'''
This is a scheduler to pick and remind people of Scrum of Scrums. 
It will send out an email and a SMS(you can opt off this) to the person on duty.

You can configure the number of weeks in rotation and add new users to it, it's complete fair game!

Created on 2016-07-13
@author: Zheng Gong
'''
import random
from send_sms import SendSMS
from send_email import SendEmail

def run(sendSMS, message, num_of_weeks=3):
    '''
    How to pick the right person for Scrum of Scrum?
    The solution is a little tricky here, because I just don't want to use db and
    also save time:

    Make each person a config file, which contains only a number, indicating
    current count of weeks for him/her.
    Assume we have 3-week rotation:
    1. when all counts are 3 => all done => reset every count to 0 to restart
    2. when all counts are 0(or some are 3 else are 0) => select a random name from names with 0 count and increase count by 1
    3. when there is a non-zero count => continue using that guy and increase count by 1
    '''
    receiver_dict = sendSMS.receiverDict
    config = {}
    for receiver in receiver_dict.keys():
        file_name = receiver+'.conf'
        try:
            with open(file_name, 'rb') as file:
                content = file.read()
                count = int(content)
                config[receiver] = count
        except IOError:
            print 'Something is wrong in reading'
    # all are 3, then reset:
    if len(filter(lambda x: x < num_of_weeks, config.values())) == 0:
        for receiver in receiver_dict:
            config[receiver] = 0
            file_name = receiver+'.conf'
            try:
                with open(file_name, 'wb') as file:
                    file.write('0')
            except IOError:
                print 'Something is wrong in writing'
    target_person = None
    available_receiver_list = filter(lambda x: config[x] < num_of_weeks, config.keys())
    ongoing_receiver_list = filter(lambda x: config[x] > 0 and config[x] < num_of_weeks, config.keys())
    if len(ongoing_receiver_list) == 0:
        target_person = random.choice(available_receiver_list)
    else:
        target_person = ongoing_receiver_list[0]

    config[target_person] += 1
    file_name = target_person + '.conf'
    with open(file_name, 'wb') as file:
        file.write(str(config[target_person]))

    if target_person:
        print target_person
        message = message % target_person
        sendEmail.send_email_to_many([target_person], message)
        # do not send sms to certain people (they need to pay for receiving sms)
        if target_person != 'Glenn':
            sendSMS.send_sms_to_many([target_person], message)
        

if __name__=='__main__':
    #,'Xinkai':'3479331959'
    # {'Glenn':'6174298743'}
    # 'Yuge':'6174355509'
    # {'Zheng':('4123541459','gongzhenggz@gmail.com')}
    receiver_dict = {'Zheng':('4123541459','gongzhenggz@gmail.com')}
    message = "Hey %s: it's your turn to attend Scrum of Scrum today!"
    sendSMS = SendSMS(receiver_dict)
    sendEmail = SendEmail(receiver_dict)
    run(sendSMS, message, 3)
