#Application #1 - Part #1

import random
import sys

def subnet_calc():
    try:
        print("\n")

        #Getting and validating the IP Address
        while True:
            ip_address = input("Enter an IP Address: ")

            #Splitting IP address into a list of 4 octets
            ip_octets = ip_address.split('.')

            #Converting octets from string to integer using list comprehension
            ip_octets_int = [int(i) for i in ip_octets]
            print(ip_octets_int)

            #Validating the ip address
            if ((len(ip_octets_int) == 4) and (1 <= ip_octets_int[0] <= 223) and (ip_octets_int[0] != 127) and (ip_octets_int[0] != 169 or ip_octets_int[1] != 254) and (0 <= ip_octets_int[1] <= 255 and 0 <= ip_octets_int[2] <= 255 and 0 <= ip_octets_int[3] <= 255)):
                break

            else:
                print("\n*The IP address is INVALID! Please try again...")

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        #Getting and validating the subnet mask
        while True:
            subnet_mask = input("Enter a Subnet Mask: ")

            #Splitting the subnet mask into a list of 4 octets
            mask_octets = subnet_mask.split('.')

            #Converting octets from string to integer using list comprehension
            mask_octets_int = [int(i) for i in mask_octets]
            print(mask_octets_int)

            #Validating the subnet mask
            if ((len(mask_octets_int) == 4) and (mask_octets_int[0] == 255) and (mask_octets_int[1] in masks) and (mask_octets_int[2] in masks) and (mask_octets_int[3] in masks) and (mask_octets_int[0] >= mask_octets_int[1] >= mask_octets_int[2] >= mask_octets_int[3])):
                break

            else:
                print("\n*The subnet mask is INVALID! Please retry! \n")
                continue

#Application #1 - Part #2

        #Algorithm for subnet identification, based on IP and Subnet Mask    

        #Converting mask to binary string
        mask_octets_binary = []

        for octet in mask_octets_int:
            binary_octet = bin(octet).lstrip('0b')
            #print(binary_octet)

            mask_octets_binary.append(binary_octet.zfill(8))
        
        print(mask_octets_binary)

        #Joining the list contents to a single string. Example: for 255.255.255.0 => 11111111111111111111111100000000
        mask_binary = "".join(mask_octets_binary)
        print(mask_binary)

        #Counting the host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = mask_binary.count('0')
        no_of_ones = mask_binary.count('1')
        no_of_hosts = abs(2 ** no_of_zeros - 2)          #abs is needed to return a positive value for the /32 mask (no zeros)

        #print(no_of_zeros)
        #print(no_of_ones)
        #print(no_of_hosts)

        #Calculating the wildcard mask
        wild_octets = []

        for octet in mask_octets_int:
            wild_octet_int = 255 - octet
            wild_octets.append(str(wild_octet_int))

        print(wild_octets) 

        wild_mask = ".".join(wild_octets)
        print(wild_mask)
        print(type(wild_mask))


#Application #1 - Part #3

        #Convert IP to Binary
        ip_octets_binary = []
        
        for octet in ip_octets_int:
            binary_octet = bin(octet).lstrip('0b')
            print(binary_octet)

            ip_octets_binary.append(binary_octet.zfill(8))
            print(ip_octets_binary)

        ip_binary = "".join(ip_octets_binary)
        print(ip_binary)
        #Example: for 192.168.2.100 => 11000000101010000000101000000001


        #Getting the network addresss and broadcast address from the binary strings obtained above
        #We will first find network and broadcast address in binary, convert it into a list of 4 binary octets, to a list of 4 string octets, to real IP address format

        network_address_binary = ip_binary[:no_of_ones] + "0" * no_of_zeros
        broadcast_address_binary = ip_binary[:no_of_ones] + "1" * no_of_zeros

        print(network_address_binary)
        print(broadcast_address_binary)

        # Converting everything back to decimal (readable format)

        network_ip_octets = []

        #range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            network_ip_octet = network_address_binary[bit: bit + 8]
            network_ip_octets.append(network_ip_octet)

        print(network_ip_octets)

        network_ip_address = []

        for octet in network_ip_octets:
            network_ip_address.append(str(int(octet, 2)))

        print(network_ip_address)

        network_address = ".".join(network_ip_address)
        print(network_address)


        broadcast_ip_octets = []

        #range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            broadcast_ip_octet = broadcast_address_binary[bit: bit + 8]
            broadcast_ip_octets.append(broadcast_ip_octet)

        print(broadcast_ip_octets)

        broadcast_ip_address = []

        for octet in broadcast_ip_octets:
            broadcast_ip_address.append(str(int(octet, 2)))

        print(broadcast_ip_address)

        broadcast_address = ".".join(broadcast_ip_address)

        print(broadcast_address)

        #Results for selected IP/mask
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet is: %s" % no_of_hosts)
        print("Wildcard mask is: %s" % wild_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

#Application #1 - Part #4
        #Generation of random IP address in the subnet
        while True:
            generate = input("Generate random IP address from this subnet? (y/n)")        

            if generate == 'y':
                generated_ip = []

                #Obtain available IP address in range, based on the difference between octets in broadcast address and network address
                for indexb, oct_bst in enumerate(broadcast_ip_address):
                    #print(indexb, oct_bst)
                    for indexn, oct_net in enumerate(network_ip_address):
                        #print(indexn, oct_net)
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                #Add identical octets to the generated IP list
                                generated_ip.append(oct_bst)

                            else:
                                #Generate random number(s) from within octet intervals and append to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

                #Ip address generated from the subnet pool
                print(generated_ip)
                random_address = '.'.join(generated_ip)
                print(random_address)

                print("Random IP address is: %s" % random_address)
                print('\n')
                continue

            else:
                print("OK Bye!\n")
                break
            
            
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

#Calling the function
subnet_calc()

#End of program