from random import choice

class RandomWalk():
    #it will contain only two method --init-- and fill walk
    def __init__(self,points=7000):
        self.points=points

        #initialize lists of x_values and y_values
        #WALKS START AT THE ORIGIN
        self.x_values=[0]
        self.y_values=[0]
    
    #add more values into x and y as the ant/drunk person moves
    def fillWalk(self):
        #continue walking till you reach max points =numpoints
        while len(self.x_values) < self.points:

            #choose a direction and distance to walk
            x_dir=choice([-1,1]) #left or right
            x_dist=choice([0,1,2,3,4])

            x_step=x_dist*x_dir #x steps from current

            y_dir=choice([-1,1]) #up or down
            y_dist=choice([0,1,2,3,4])
            y_step=y_dist*y_dir #ysteps from current y

            currentX=self.x_values[-1]
            currentY=self.y_values[-1]

            nextX=currentX+x_step
            nextY=currentY+y_step

            #now append into the x and ylists
            self.x_values.append(nextX)
            self.y_values.append(nextY)
        
        #done