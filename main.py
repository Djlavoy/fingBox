import psutil
import time
from twilio.rest import TwilioRestClient 


# Set Cpu Threshold Percent
cpu_threshold = 2

# Set Ram Usage Threshold Percent
ram_threshold = 2

# Set Disk Usage Threshold Percent
disk_threshold = 10

# Put your own Twilio credentials here 
# This Info can be found under the the account setting
ACCOUNT_SID = "" 
AUTH_TOKEN = "" 

# Number to send Alert to
sendto = "1234567890"

# Sender Number From Twilio
sender = "+11234567890"

# TwilioRestClient Var
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

# Get CPU Usage Percent
a = psutil.cpu_percent(interval=1)

# Get Ram Usage Percent
b = psutil.virtual_memory().percent

# Get Disk Usage Percent
c = psutil.disk_usage('/')

# Checks If Disk is above the threshold
if int(c[3]) >= disk_threshold:
    client.messages.create(
	to="{}".format(sendto), 
	from_="{}".format(sender), 
	body="fingBox Alert: Disk FreeSpace is above acceptable {}% and is Currently at {}%".format(disk_threshold, c[3]),)

# Checks If Ram is above the threshold
if int(b) >= ram_threshold:
    client.messages.create(
        to="{}".format(sendto),
        from_="{}".format(sender),
        body="fingBox Alert: Memory is above acceptable {}% and is Currently at {}%".format(ram_threshold, b),)

# Check If Cpu is above the threshold 
if int(a) >= cpu_threshold:
    client.messages.create(
        to="{}".format(sendto),
        from_="{}".format(sender),
        body="fingBox Alert: CPU is above acceptable {}% and is Currently at {}%".format(cpu_threshold, a),)
