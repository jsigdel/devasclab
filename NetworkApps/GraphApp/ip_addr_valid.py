"""
In this module, we define a function that takes the ip address/s list returned by ip_file_valid() function 
from ip_file_valid module and checks each octets in each IP address for its validity.
"""

import sys

#Checking and validating each octets
def ip_address_valid(ip_list):

    for ip in ip_list:
        #Create a list of 4 octets for each IP address
        octet_list_str = ip.split('.')

        #Convert the each octet from string to int
        octet_list_int = [int(i) for i in octet_list_str]
        print(octet_list_int)

        #Validating the IP address
        if ((len(octet_list_int) == 4) and (1 <= octet_list_int[0] <= 223) and (octet_list_int[0] != 127) and (octet_list_int[0] != 169 or octet_list_int[1] != 254) and (0 <= octet_list_int[1] <= 255 and 0 <= octet_list_int[2] <= 255 and 0 <= octet_list_int[3] <= 255)):
            continue

        else:
            print("\n* {} is Invalid IP.\n".format(ip))
            sys.exit()
            

