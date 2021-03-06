# Modules that are being imported
import matplotlib.pyplot as plt
import numpy as np
import math

class Projectile:
    '''Class for constructing projectile
    motion graph in kinematics section'''
    def __init__(self, theta, u):
        self.angle = float(theta)*0.0174533
        self.initialVel =float(u)

    def Path(self):
        '''Function to calculate and plot
        path of given projectile'''
        g = 9.8
        end = self.Period()
        t = np.linspace(0, end)
        x = (self.initialVel * math.cos(self.angle))*t
        y = (self.initialVel * math.sin(self.angle))*t - 0.5*g*t*t
        plt.title("Projectile Motion of Particle")
        plt.xlabel("Distance")
        plt.ylabel("Height")
        plt.plot(x,y)

    def Period(self):
        '''Function to calculate time
        period of given projectile.'''
        return (2 * self.initialVel * math.sin(self.angle))/9.8;

    def HighestPoint(self):
        '''Function to calculate maximum
        height of given projectile.'''
        return (self.initialVel*math.sin(self.angle))**2 /( 2*9.8)

    def Distance(self):
        '''Function to calculate the
        horizontal range of given projectile.'''
        return self.initialVel**2 * math.sin(2*self.angle)/(9.8)

        


    