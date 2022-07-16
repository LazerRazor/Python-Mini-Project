# Modules that are being imported
import matplotlib.pyplot as plt
import numpy as np

class Equation:
    '''Class for calculations and =graph-plotting
    related to equations in variable motion'''
    def __init__(self, two, one, constant):
        self.a = two
        self.b = one
        self.c = constant

    def displacement(self, start, end):
        '''Function for calculating and plotting
        displacement-time graph from given equation'''
        x = np.linspace(start,end)
        y = int(self.a) * (x**2) + int(self.b)*(x) + int(self.c)
        plt.plot(x, y)
        plt.title("Displacement V/S Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Displacement")

    def velocity(self, start, end):
        '''Function for calculating and plotting
        velocity-time graph from given equation'''
        x = np.linspace(start,end)
        y = int(self.a) * (x) * int(2) + int(self.b) 
        plt.plot(x, y)
        plt.title("Velocity V/S Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Velocity")

    def acceleration(self, start, end):
        '''Function for calculating and plotting
        acceleration-time graph from given equation'''
        x = np.linspace(int(start),int(end))
        y = int(self.a) *int(2) * (x**int(0))
        plt.plot(x, y)
        plt.title("Acceleration V/S Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Acceleration")








