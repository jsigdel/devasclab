import matplotlib.pyplot as pyp
import matplotlib.animation as animation

#Create a new figure
figure = pyp.figure()

#Create a subplot with 1 row, 1 column and index 1 - this means a single subplot in our figure
subplot = figure.add_subplot(1, 1, 1)

#Create a function that reads data from cpu.txt file and feeds it to our subplot in real time
def animation_function(i):
    #Open the file and read each row of CPU utilization data and create a list of values
    cpu_data = open("C:\\Users\\jiwan.sigdel\\Desktop\\Python\\NetworkApps\\GraphApp\\cpu_util.txt", 'r').readlines()

    #Define a list to store the cpu util value in floating format
    cpu_data_float = []

    #Conver the cpu util from string to float and store in the list above, and use if logic to exclde empty lines
    for data in cpu_data:
        if len(data) > 1:
            cpu_data_float.append(float(data))

    #Clear/refresh the figure to avoid unnecessary overwriting for each new poll (every 10 seconds)
    subplot.clear()

    #Plot the values in the list
    subplot.plot(cpu_data_float)

#Use the figure, the function and a polling interval of 10000 ms (10s) to build the graph
graph_animation = animation.FuncAnimation(figure, animation_function, interval=10000)

#Display the graph on the screen
pyp.show()

