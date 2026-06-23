import turtle as tt
import random

tt.colormode(255) #allows setting up RGB values as numbers for colors

def line(a1, o1, a2, o2):
    """Draws a simple line from a coordinate to another."""
    
    tt.penup()
    tt.setposition(a1, o1)
    tt.pendown()
    tt.setposition(a2, o2)
    tt.penup()

def rectangle(x=-150,y=-300,w=180,h=60):
    """Draws a rectangle."""
    
    line(x - w/2, y, x + w/2, y)
    line(x + w/2, y, x + w/2, y + h)
    line(x + w/2, y + h, x - w/2, y + h)
    line(x - w/2, y + h, x - w/2, y)

def random_color():
    """Randomly selects 3 numbers between 0 and 255 as to select an RGB color."""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b