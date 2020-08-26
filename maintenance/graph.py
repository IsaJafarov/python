import matplotlib.pyplot as pyp
import matplotlib.animation as animation

figure = pyp.figure()
subplot = figure.add_subplot(1,1,1)

def animation_function(i):
    cpu_data = open('./data.txt','r').readlines()
    x=[]
    for value in cpu_data:
        if len(value) > 1:
            x.append(float(value))
    subplot.clear()
    subplot.plot(x)

graph_animation = animation.FuncAnimation(figure, animation_function,interval=10000)
pyp.show()
