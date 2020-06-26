#Import necessary modules

import difflib
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from netmiko import ConnectHandler

#Define the device to monitor
ip = "10.10.10.2"

#Define the device type for running netmiko
device_type = "arista_eos"

#Define the username and password for running netmiko
username = "admin"
password = "python"

#Define the command to send to the device
command = "show running"

#Connect to the device via ssh
session = ConnectHandler(device_type=device_type, ip=ip, username=username, password=password, global_delay_factor=3)

#Enter the enable mode
enable = session.enable()

#Send the command and store the output
output = session.send_command(command)

#Define the file from yesterday for comparision
device_config_old = "cfgfiles/" + ip + '_' + (datetime.date.today() - datetime.timedelta(days = 1)).isoformat()

#Write the command output to a file for today
with open("cfgfiles/" + ip + '_' + datetime.date.today().isoformat(), 'w') as device_config_new:
    device_config_new.write(output + '\n')

#Extract difference between yesterday's and today's files in HTML format
with open(device_config_old, 'r') as old_file, open("cfgfiles/" + ip + '_' + datetime.date.today().isoformat(), 'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines = old_file.readlines(), tolines = new_file.readlines(), fromdesc = "Yesterday", todesc = "Today")


#Send the differences via email
#Define email parameters

fromaddr = "jsigdel1@gmail.com"
toaddr = "jsigdel1@gmail.com"

#More on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multipart_messages
msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Daily Configuration Management Report"
msg.attach(MIMEText(difference, "html"))

#Send the email via Gmail's SMTP server on port 587
server = smtplib.SMTP("smtp.gmail.com", 587)

#SMTP connection is in TLS mode. All SMTP commands that follow will be encrypted.
server.starttls()

#Login to Gmail and sending email
server.login("jsigdel1@gmail.com", "Dh%f4MwFnob4@DJf")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()

#End of Program