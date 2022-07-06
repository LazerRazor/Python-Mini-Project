import matplotlib.pyplot as plt
import numpy as np

class Equation:
    def __init__(self, two, one, constant):
        self.a = two
        self.b = one
        self.c =  constant

    def displacement(self, start, end):
        x = np.linspace(start,end)
        y = self.a * (x**2) + self.b*(x) + self.c
        fig = plt.figure(figsize = (10, 5))
        plt.plot(x, y)
        plt.title("Displacement V/S Time Graph")
        plt.xlabel("Time")
        plt.ylabel("Displacement")

    def velocity(self, start, end):
        x = np.linspace(start,end)
        y = self.a * (x) * 2 + self.b 
        fig = plt.figure(figsize = (10, 5))
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








