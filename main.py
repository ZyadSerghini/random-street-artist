import street
import ground
import turtle as tt
import random

tt.speed(0)

def main():
    """Draws a street with 4 randomly generated buildings."""
    
    y_ground = random.randint(-375, -50)
    ground.ground(y_ground)
    for i in range(4):
        street.building(-390 + i*240, y_ground)
    
    #moving the cursors aside to avoid it covering the buildings.
    tt.setposition(0, 300)
    
if __name__ == "__main__":
    main()
    tt.done()
    
