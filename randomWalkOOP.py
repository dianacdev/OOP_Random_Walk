import math
from os import stat
import random
import statistics
from turtle import *
import turtle


def north():
    '''Take one step north.'''
    return (0, 1)


def south():
    '''Take one step south.'''
    return (0, -1)


def east():
    '''Take one step east.'''
    return (1, 0)


def west():
    '''Take one step west.'''
    return (-1, 0)


def scale():
    '''A global constant.'''
    return 15

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

class Pa():
    def __init__(self, name="Pa", icon="arrow", shade="#36ddff"):
        self.name = name  # needs to use magic string method __str__()
        self.shape = icon
        self.color = color

    def __str__(self):
        return self.name

    def step():
        return random.choice([north(), east(), south(), west()])

class MiMa():
    def __init__(self, name="Mi Ma", icon="circle", shade="#ff5b4f"):
        self.name = name  # needs to use magic string method __str__()
        self.shape = icon
        self.color = color

    def __str__(self):
        return self.name

    def step():
        return random.choice([north(), east(), south(), south(), west()])


class Reg():
    def __init__(self, name="Reg", icon="square", shade="#faed32"):
        self.name = name  # needs to use magic string method __str__()
        self.shape = icon
        self.color = color

    def __str__(self):
        return self.name

    def step():
        return random.choice([east(), west()])


class Trial():
    def __init__(self, number_of_steps, number_of_walks, walker) -> None:
        self.walker = walker
        self.number_of_steps = number_of_steps
        self.number_of_walks = number_of_walks

    def plot():
        pass


    def run_trial(walker, number_of_walks, number_of_steps):
        if walker.lower() == "pa":
            walker_run("#36ddff","arrow",Pa, number_of_walks, number_of_steps,"Pa")
        elif walker.lower() == "mima":
            walker_run("#ff5b4f","circle",MiMa, number_of_walks, number_of_steps, "MiMa")
        elif walker.lower() == "reg":
            walker_run("#faed32","square",Reg, number_of_walks, number_of_steps, "Reg")
        elif walker.lower() == "all":
            walker_run("#36ddff", "arrow", Pa, number_of_walks, number_of_steps,"Pa")
            walker_run("#ff5b4f","circle",MiMa, number_of_walks, number_of_steps,"MiMa")
            walker_run("#faed32","square",Reg, number_of_walks, number_of_steps,"Reg")

def walker_run(shade, icon, obj, number_of_walks, number_of_steps, walker):
    """Goes through all the trials of a walker"""
    print(f"Walker Report: {walker}")
    for i in range(number_of_walks): #number of trials
        x = 0
        y = 0
        location = x,y
        pen.penup()
        pen.goto(x,y)
        pen.color(shade)
        pen.shape(icon)
        pen.stamp()
        for j in range(number_of_steps): #number of steps
            x_delta, y_delta = obj.step()
            x += x_delta
            y += y_delta
            pen.goto(x * scale(), y * scale())
            pen.stamp()
            location2 = pen.pos()
        distance = euclidean(location,location2)
        manhattan_dist = manhattan(location, location2)
        print(f"\tEuclidean Distance for {walker} on Trial {i+1}:\n\t\t\t\t\t\t {distance}") #can't call the obj.str or obj.name unsure why
        print(f"\tManhattan Distance for {walker} on Trial {i+1}:\n\t\t\t\t\t\t {manhattan_dist}")

def walk(walker, steps, location = (0,0)):
        x,y = location
        if walker.lower() == "pa":
            Pa(name="Pa", icon="arrow", shade="#36ddff")
            pen.penup()
            pen.goto(location)
            pen.color("#36ddff")
            pen.shape("arrow")
            pen.stamp()
            for j in range(steps):
                x_delta, y_delta = Pa.step()
                x += x_delta
                y += y_delta
                pen.goto(x * scale(), y * scale())
                pen.stamp()
                location2 = (x_delta, y_delta)
            distance = euclidean(location, location2)
            print(f"Euclidean Distance for {walker}: {distance}")


def euclidean(location, location2):
    '''Compute the euclidean distance of pos from the origin.'''
    x, y = location
    x_delta, y_delta = location2
    return math.sqrt((x_delta - x)**2 +(y_delta-y)**2)


def manhattan(location, location2):
    '''Compute the Manhattan distance of pos from the origin.'''
    return(sum(abs(val1 - val2)for val1, val2 in zip(location, location2)))


def main(Trial,Pa, MiMa, Reg):
    Info = Screen()
    number_of_steps = int(Info.numinput("Trials", "Enter the number of Steps that will be occuring for each Walk: ", 1, minval=1, maxval=2000))
    number_of_walks = int(Info.numinput("Number of Times they Wonder Off","How many times do they wonder off?", 1, minval=1, maxval=100))
    walker = Info.textinput("Wanderer", "Enter who is wandering <Pa, Ma, Reg, All>: ")
    turtle.title("Random Walk Simulator by Diana Cervantes")
    Trial.run_trial(walker, number_of_walks, number_of_steps)
    #walk(walker, number_of_steps, (0,0)) Didn't see a reason to use walk since you can calculate a single trial and get the same results. Function exists and can be optimized but not necessary for the assignment
    turtle.done()


if __name__ == '__main__':
    main(Trial,Pa, MiMa, Reg)
