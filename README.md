# FingBox Version 0.0.1 Alpha

FunctioningBox is a Monitoring tool that will text you if a Threshold is passed.

### FingBox Currently Monitors 
  - Cpu used %
  - Ram used %
  - Disk used %

### TODO
 - IO monitoring
 - networking monitoring
 - Call and speak to you about the alert
 - feel free to make request
 


#### Installing 

To install FingBox you will need the following:

- Twilio Account
- Python 2.7
- PIP
- psutil 

#### Step 1: Get Dependencies
```sh
$ sudo apt-get install git
$ sudo apt-get install python-pip
$ sudo pip install psutil
```

#### Step 2: Get FingBox
```sh
$ cd ~/
$ git clone https://github.com/Djlavoy/fingBox.git
```

#### Step 3: Config FingBox 
```sh
$ vim ~/fingBox/main.py

And Update the following 


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
```

#### Step 4: Setup Cron
You must provided the pull path in the cron 
This Example will run every 5 minutes 
```sh
$ crontab -e

*/5 * * * * python /full/path/to/fingBox/main.py

```

License
----

Apache 2


**OpenSource Software, Hell Yeah!**

   


