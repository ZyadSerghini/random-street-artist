import floors
import base
    
def building(x = -150, y_ground = -300):
    """Draws a random building, from ground floor to roof."""
    
    y = y_ground
    nb_floors = base.random.randint(1,5)
    c_facade = base.random_color()
    
    for i in range(nb_floors):
        
        if i == 0:
            c_door = base.random_color()
            floors.ground_floor(x, y, c_facade, c_door)
        else:
            floors.regular_floor(x, y, c_facade, i)
        
        y += 60 #y coordinate increases of 60 per floor (60 being a floor's height)
        
    floors.roof(x, y_ground, nb_floors)