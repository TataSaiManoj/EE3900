import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import patches
from matplotlib.figure import Figure
from matplotlib import rcParams
    
def zplane(filename=None):

    # get a figure/plot
    ax = plt.subplot(111)

    # create the unit circle
    uc = patches.Circle((0,0), radius=1, fill=False,
                        color='black')
    rc = patches.Rectangle((-3, -3), 6, 6,fc=(0.33,0.33,0.33,0.5), ec=(0,0,0,1))
    uc2 = patches.Circle((0,0), radius=0.9, fill=True,
                        color='white')
                        
    ax.add_patch(uc)
    ax.add_patch(rc)
    ax.add_patch(uc2)

    p1 = [0, ((0.9/np.sqrt(2))), ((0.9/np.sqrt(2)))]
    p2 = [0, ((0.9/np.sqrt(2))), -((0.9/np.sqrt(2)))]

    z1 = [((0.9/np.sqrt(2)))]
    z2 = [0]

    # Plot the zeroes and set marker properties 
    t1 = plt.plot(z1, z2, 'o', markersize = 5, color='red')

    # Plot the poles and set marker properties
    t2 = plt.plot(p1, p2, 'rx', ms=10)
    plt.setp( t2, markersize=6.0, markeredgewidth=2.0,
              markeredgecolor='black', markerfacecolor='r', label = 'Poles')
    
    legend1 =  ax.legend(t1, ['Zeroes'], loc = 4, numpoints = 1)
    legend2 = ax.legend(t2, ['Poles'], loc = 1, numpoints = 1)

    ax.add_artist(legend1)
    ax.add_artist(legend2)

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # set the ticks
    r = 1.5; plt.axis('scaled'); plt.axis([-r, r, -r, r])
    ticks = [-1, -.5, .5, 1]; plt.xticks(ticks); plt.yticks(ticks)
    # plt.title("Pole-Zero Plot")

    plt.show()

zplane()
