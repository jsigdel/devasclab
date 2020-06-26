"""
In this module, we define a function that asks user to input a file containing IP address/s, verify the existence of file, 
open the file for reading from start, create a list of IP addresses and close the file and return the list.
"""

import os.path
import sys

#Checking IP address file and content validity
def ip_file_valid():

    #Prompting user for file imput
    ip_file = input("\n# Enter IP file path with file name and extension: ")

    #Changing exception message
    if os.path.isfile(ip_file) == True:
        print("\n*IP file is valid \n")

    else:
        print("\n* {} does not exist. Please check and try again.\n".format(ip_file))

    #Open user input file for reading
    current_ip_file = open(ip_file, 'r')

    #Read the file from the start
    current_ip_file.seek(0)

    #Read each line (IP) and put them in a list
    ip_list = current_ip_file.readlines()

    #Remove next line character from each IP address
    for i in range(len(ip_list)):
        ip_list[i] = ip_list[i].rstrip('\n')

    #Closing the file
    current_ip_file.close()

    return ip_list