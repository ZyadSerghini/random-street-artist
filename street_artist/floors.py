from . import roofs
from . import facade as face

def ground_floor(x = -150, y_ground = -300, c_facade = "red", c_door = "yellow"):
    """Draws the ground floor."""
    
    face.base.tt.fillcolor(c_facade)
    face.base.tt.begin_fill()
    face.base.rectangle(x, y_ground)
    face.base.tt.end_fill()
    
    face.facade(x, y_ground, c_door, 0)

def regular_floor(x =-150, y_ground=-240, color = "red", level = 1):
    """Draws a non-ground floor."""
    
    face.base.tt.fillcolor(color)
    face.base.tt.begin_fill()
    face.base.rectangle(x,y_ground)
    face.base.tt.end_fill()
    
    face.facade(x, y_ground, color, level)

def roof(x = -150, y_ground = -300, nb_floors = 1):
    """Randomly selects a roof type (equal odds)."""
    
    test = face.base.random.randint(1,2)
    if test == 1:
        roofs.triangular_roof(x, y_ground, nb_floors)
    else:
        roofs.flat_roof(x, y_ground, nb_floors)