import psutil
import time
from twilio.rest import TwilioRestClient 

cpu_threshold = 2
ram_threshold = 2
disk_threshold = 10

# put your own Twilio credentials here 
ACCOUNT_SID = "" 
AUTH_TOKEN = "" 

# Number to send Alert to
sendto = "1234567890"

# Sender Number From Twilio
sender = "+11234567890"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

a = psutil.cpu_percent(interval=1)
b = psutil.virtual_memory().percent
c = psutil.disk_usage('/')


while True:

    if int(c[3]) >= disk_threshold:
        client.messages.create(
	    to="{}".format(sendto), 
	    from_="{}".format(sender), 
	    body="fingBox Alert: Disk FreeSpace is above acceptable {}% and is Currently at {}%".format(disk_threshold, c[3]),)

    if int(b) >= ram_threshold:
        client.messages.create(
                to="{}".format(sendto),
                from_="{}".format(sender),
                body="fingBox Alert: Memory is above acceptable {}% and is Currently at {}%".format(ram_threshold, b),)


    if int(a) >= cpu_threshold:
        client.messages.create(
                to="{}".format(sendto),
                from_="{}".format(sender),
                body="fingBox Alert: CPU is above acceptable {}% and is Currently at {}%".format(cpu_threshold, a),)
