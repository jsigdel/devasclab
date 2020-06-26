import sys
import time

from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_address_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

#Save the ip addresses from the file to a list
ip_list = ip_file_valid()

#Verify the validity of each ip address in the list
try:
    ip_address_valid(ip_list)

except KeyboardInterrupt:
    print("\n* Program aborted by the user. Exiting...")
    sys.exit()

#Verify the reachability of each ip address in the list
try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n* Program aborted by the user. Exiting...")
    sys.exit()

#Call threads creation function for one or more ssh connections, with the span of 10s, assuming that all the process and function call completes within 10s
#This while loop calls the create_threads function indefinately every 10s until terminated by the user with Ctrz+C
while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(10)

#End of program