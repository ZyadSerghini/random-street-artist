from . import base

def triangular_roof(x=-150, y=-300, number=4):
    """Draws a triangular roof."""
    
    base.tt.fillcolor("black")
    base.tt.begin_fill()
    base.line(x + 90, y + number * 60, x, y + (number + 1) * 60)
    base.line(x, y + (number + 1) * 60, x - 90, y + number * 60)
    base.line(x - 90, y + number * 60, x + 90, y + number * 60)
    base.tt.end_fill()
    
def flat_roof(x = -150, y = -300, number = 1):
    """Draws a flat roof."""
    
    base.tt.pensize(5)
    base.line(x - 90, y + number * 60, x + 90, y + number * 60)
    base.tt.pensize(1)