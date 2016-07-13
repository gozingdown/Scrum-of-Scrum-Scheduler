'''
Created on 2016-07-13
@author: Zheng Gong
'''
import random
from send_sms import SendSMS

def run(sendSMS, message, num_of_weeks=3):
    receiver_dict = sendSMS.receiverDict
    config = {}
    for receiver in receiver_dict:
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
        sendSMS.send_sms_to_many([target_person], message)


if __name__=='__main__':
    #,'Xinkai':'3479331959'
    receiver_dict = {'Zheng':'4123541459','Xinkai':'4123541459'}
    message = "Hey %s: it's your turn to attend Scrum of Scrum today!"
    sendSMS = SendSMS(receiver_dict)
    run(sendSMS, message, 3)
