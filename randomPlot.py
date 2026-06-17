import matplotlib.pyplot as plt
from random_walk import RandomWalk

#create object
for x in range(5):
    randWalk=RandomWalk()
    randWalk.fillWalk()
    #colorPoints=list(range(1,randWalk.points))
    colorPoints = list(range(randWalk.points))

    plt.scatter(randWalk.x_values, randWalk.y_values,c=colorPoints, cmap=plt.cm.Blues,
            edgecolor='none', s=13)
plt.show()
