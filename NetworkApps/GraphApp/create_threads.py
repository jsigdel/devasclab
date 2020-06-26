import threading

#Creating threads
def create_threads(ip_list, function):

    threads = []
    
    for ip in ip_list:
        th = threading.Thread(target=function, args=(ip,))  #args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
