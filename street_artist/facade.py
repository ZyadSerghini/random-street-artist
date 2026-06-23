from . import base

def facade(x = -150, y_sol = -300, color = "red", level = 0):
    """Draws doors, windows and balconies."""
    
    #ground floor
    if level == 0: 
        door_drawn = False 
        for i in range(3):
            test = base.random.randint(1, 3 - i)
    
            if test == 1 and not door_drawn: 
                door_drawn = True
                
                #Randomly selects a rounded or squared door (equal odds)
                nb_door = base.random.randint(1,2) 
                
                if i == 0: #left spot
                    door(x - 50 , y_sol, color, nb_door)
                elif i == 1: #middle spot
                    door(x, y_sol, color, nb_door)
                elif i ==2: #right spot
                    door(x + 50, y_sol, color, nb_door)
                    
            else:
                if i == 0: #left spot
                    window(x - 50, y_sol + 20)
                elif i == 1: #middle spot
                    window(x, y_sol + 20)
                elif i ==2: #right spot
                    window(x + 50, y_sol + 20)
    else:
        for i in range(3):
            
            #randomly selects a window/balcony (equal odds)
            test = base.random.randint(1,2)
            
            #window
            if test == 1: 
                if i == 0:
                    window(x - 50, y_sol + 20) #left spot
                elif i == 1:
                    window(x, y_sol + 20) #middle spot
                elif i == 2:
                    window(x + 50, y_sol + 20) #right spot
            
            #balcony
            else:
                if i == 0:
                    balcony(x-50, y_sol) #left spot
                elif i == 1:
                    balcony(x, y_sol) #middle spot
                elif i == 2:
                    balcony(x + 50, y_sol) #right spot

def window(x = -215,y = -280):
    """Draws a window."""
    
    base.tt.fillcolor("white")
    base.tt.begin_fill()
    base.rectangle(x,y,30,30)
    base.tt.end_fill()

def door(x, y, color, nb_door):
    """Draws a door of a given color."""
    
    #Squared door   
    if nb_door == 1: 
        base.tt.fillcolor(color)
        base.tt.begin_fill()
        base.rectangle(x,y,30,50)
        base.tt.end_fill()
    
    #Rounded door 
    else: 
        base.tt.fillcolor(color)
        base.tt.begin_fill()
        
        base.line(x-15, y, x+15, y)
        base.line(x+15, y, x+15, y+40)
        base.tt.pendown()
        base.tt.left(90)
        base.tt.circle(15,180)
        base.tt.left(90)
        base.line(x-15, y+40, x-15, y)
        
        base.tt.end_fill()

def balcony(x,y):
    """Draws a balcony window."""
    
    #The balcony window is drawn the same way as a regular door.
    door(x,y,"white", 1)
    
    #draws balcony outline...
    base.rectangle(x, y, 46, 25)
    base.tt.forward(3)
    base.tt.pendown()
    #...then bars
    
    for i in range(3): 
        base.tt.left(90)
        base.tt.forward(25)
        base.tt.right(90)
        base.tt.forward(10)
        base.tt.right(90)
        base.tt.forward(25)
        base.tt.left(90)
        base.tt.forward(8)
    base.tt.penup()