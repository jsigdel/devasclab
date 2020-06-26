"""
In this module, we define a function named ip_reach() that takes a list of IP addresses returned by ip_file_valid() function 
from ip_file_valid module and send the ping request to those IPs to check the reachability
"""

import sys
import subprocess

#Checking IP reachability
def ip_reach(ip_list):

    for ip in ip_list:
       
        #send 2 ping requests and do not display the response on the screen
        ping_reply = subprocess.call("ping %s -n 2" %(ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_reply == 0:
            print("\n* {} is reachable.".format(ip))
            continue

        else:
            print("\n* {} is not reachable. Please check connectivity and try again.".format(ip))
            sys.exit()
        