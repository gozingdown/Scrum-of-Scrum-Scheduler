# Scrum-of-Scrum-Scheduler

This is a scheduler to pick and remind people of Scrum of Scrums. 

It will send out an email and a SMS(you can opt-out this) to the person on duty and and an email to everyone on the team.

You can configure the number of weeks in rotation and add new users to it, it's complete fair game!

Currently all configuration are hard-coded because I don't want to spend more time on it!

Read below for more important information:


==============================================================================
How to use it?
==============================================================================
1. Note: we use name as unique identifier for a person
2. create name.config file with only character 0 in the file

    e.g. in command line:  echo 0 > Zheng.conf

    Create as many as you like
    
3. in scheduler.py, add info to receiver_dict

    e.g. {'Zheng':('4123541459','gongzhenggz@gmail.com'), 'xxx':('123','x@gmail.com')}
4. in scheduler.py, set up number of weeks for rotation: variable num_of_weeks
5. set up a cron job to run scheduler.py or just run it directly for testing


==============================================================================
How to set up MailGun API to send email?
==============================================================================
1. register a Domain on GoDaddy.com
2. register on Mailgun.com and add the domain you just bought
3. Set up DNS records in DoDaddy-Domain manager, add new records required by Mailgun.com (two TXT records and on CNAME record)
4. Verify in mailgun.com that new domain is active
5. use the api key and new domain to send rest calls


==============================================================================
How to send SMS via API?
==============================================================================
Take a look at http://textbelt.com


==============================================================================
How to pick the right person for Scrum of Scrum?
==============================================================================
The solution is a little tricky here, because I just don't want to use db and
also save time:

Make each person a config file, which contains only a number, indicating
current count of weeks for him/her.

Assume we have 3-week rotation:

1. when all counts are 3 => all done => reset every count to 0 to restart

2. when all counts are 0(or some are 3 else are 0) => select a random name from names with 0 count and increase count by 1

3. when there is a non-zero count => continue using that guy and increase count by 1



Zheng
2016-07-14
