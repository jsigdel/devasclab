"""
In this module
"""

import paramiko
import datetime
import os.path
import time
import sys
import re

#Checking user/pwd file
#Prompting user to provide user/pwd file
user_file = input("\n# Enter user/pwd file path with file name and extension: ")

#Verifying the existence of user/pwd file
if os.path.isfile(user_file) == True:
    print("\n* The user/pwd file entered above is valid.")

else:
    print("\n* The user/pwd file {} entered above cannot be found. Please check the file and try again!".format(user_file))
    sys.exit()


#Checking the cmd file
#Prompting user to provide cmd file
cmd_file = input("\n# Enter cmd file path with file name and extension: ")

#Verifying the existence of cmd file
if os.path.isfile(cmd_file) == True:
    print("\n* The cmd file entered above is valid. ")

else:
    print("\n* The cmd file {} entered above cannot be found. Please check the file and try again!")
    sys.exit()


#Open SSHv2 connection the device/s
def ssh_connection(device_ip):

    global user_file
    global cmd_file

    #Creating ssh connection, putting everything inside try/except block to exit from the program normally for Authentication exception
    try:
        #Open the user/cmd file in read mode
        current_user_file = open(user_file, 'r')

        #Move the cursor at the begginning of the file
        current_user_file.seek(0)

        #Extract the username from the file
        username = current_user_file.readlines()[0].split(',')[0]
        print(username)

        #Move the cursor at the begginning of the file
        current_user_file.seek(0)

        #Extract the password from the file
        password = current_user_file.readlines()[0].split(',')[1].rstrip('\n')
        print(password)

        #Create a session 
        session = paramiko.SSHClient()

        #For lab, we allow auto-accepting unknown host keys. It is not advised to do this in production. The default is reject policy.
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the device using usernaem and pasword
        session.connect(device_ip, username=username, password=password)

        #Start an interactive shell session on the device
        cli = session.invoke_shell()

        #Enter user exec mode and Setting terminal length for entire output - disable pagination
        cli.send("enable\n")
        cli.send("terminal length 0\n")
        time.sleep(1)

        #Enter global config mode
        cli.send("configure terminal\n")
        time.sleep(1)

        #Open the command file for reading
        current_cmd_file = open(cmd_file, 'r')

        #Move the cursor at the begginning of the file
        current_cmd_file.seek(0)

        #Send each command from the file to the device
        for cmd in current_cmd_file.readlines():
            cli.send(cmd + '\n')
            time.sleep(2)

        #Close the command file
        current_cmd_file.close()

        #Close the user/pwd file
        current_user_file.close()

        #Check the device output for syntax errors
        device_output = cli.recv(65535)

        if re.search(b"% Invalid input", device_output):
            print("\n* There was at least one syntax error on the device {}.".format(device_ip))

        else:
            print("\n* Done for the device {}. Data sent to file at {}.\n".format(device_ip, str(datetime.datetime.now())))

        #print(str(device_output) + '\n')

        #Search for the CPU utilization value within the device output (%Cpu(s):  1.7 us,)
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)+us,", device_output)
 
        #Extract the second group, which matches the actual value of CPU utilization and decoding to UTF-8 format from the binary data type
        cpu_util = cpu.group(2).decode("utf-8")

        print(cpu)
        print(cpu_util)

        #Open the cpu utilization file and append the cpu_util value
        with open("C:\\Users\\jiwan.sigdel\\Desktop\\Python\\NetworkApps\\GraphApp\\cpu_util.txt", 'a') as f:
            #f.write("{}, {}\n".format(str(datetime.datetime.now()), cpu_util))
            f.write(cpu_util + '\n')

        #Close the ssh session
        session.close()

    except paramiko.AuthenticationException:
        print("\n* Invalid username or password. Please try again!")
        print("\n* Closing the program. Bye!")










