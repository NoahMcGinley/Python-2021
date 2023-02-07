import turtle
def orion():

    turtle.setup(500, 600)
    turtle.penup()
    turtle.hideturtule()

    LEFT_SHOULDER_X = -70
    LEFT_SHOULDER_Y = 200
    
    RIGHT_SHOULDER_X = 80
    RIGHT_SHOULDER_Y = 180
    
    LEFT_BELTSTAR_X = -40
    LEFT_BELTSTAR_Y = -20
    
    MIDDLE_BELTSTAR_X = 0
    MIDDLE_BELTSRAR_Y = 0
    
    RIGHT_BELTSTAR_X = 40
    RIGHT_BELTSTAR_Y = 20
    
    LEFT_KNEE_X = -90
    LEFT_KNEE_Y = -180
    
    RIGHT_KNEE_X = 120
    RIGHT_KNEE_Y = -140

turtle.penup()
turtle.goto(-70, 200)
turtle.dot()
turtle.write("Betelgeuse")
turtle.pendown()
turtle.goto(-40, -20)
turtle.dot()
turtle.write("Alnitak")
turtle.goto(-90, -180)
turtle.dot()
turtle.write("Saiph")
turtle.penup()
turtle.goto(80, 180)
turtle.dot()
turtle.write("Meissa")
turtle.pendown()
turtle.goto(40, 20)
turtle.dot()
turtle.write("Mintaka")
turtle.goto(120, -140)
turtle.dot()
turtle.write("Rigel")
turtle.penup()
turtle.goto(40, 20)
turtle.dot()
turtle.pendown()
turtle.goto(0, 0)
turtle.dot()
turtle.write("Alinitam")
turtle.goto(-40, -20)
turtle.done
