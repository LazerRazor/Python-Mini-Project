import matplotlib.pyplot as plt
import numpy as np

class Equation:
    def __init__(self, two, one, constant):
        self.a = two
        self.b = one
        self.c =  constant

    def displacement(self, start, end):
        x = np.linspace(start,end)
        y = int(self.a) * (x**2) + int(self.b)*(x) + int(self.c)
        plt.plot(x, y)
        plt.title("Displacement V/S Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Displacement")

    def velocity(self, start, end):
        x = np.linspace(start,end)
        y = int(self.a) * (x) * int(2) + int(self.b) 
        plt.plot(x, y)
        plt.title("Velocity V/S Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Velocity")

    def acceleration(self, start, end):
        x = np.linspace(int(start),int(end))
        y = int(self.a) *int(2) * (x**int(0))
        plt.plot(x, y)
        plt.title("Acceleration V/S Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Acceleration")








