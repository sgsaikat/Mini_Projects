import turtle
turtle.speed(5)
turtle.pensize(2)
turtle.color("blue")

def draw_star():
    for i in range(10): 
        turtle.forward(50) 
        turtle.right(144) 

def draw_square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_concentric_squares(n):
    incr = 0
    for i in range(50):
        turtle.forward(10 + incr)
        turtle.right(90)
        incr += n

def draw_circles():
    for i in range(1, 11):
        turtle.color("blue")
        turtle.circle(5*i)
        turtle.color("red")
        turtle.circle(-5*i)
        turtle.left(i*5)

def draw_alphabets():
    ## ---> Make “ABCDE”
    scale = 10
    print(turtle.pos())
    turtle.penup()
    turtle.setpos((-180.0, 0.0))

    ## Letter A
    turtle.pendown()
    # Point upwards to begin
    turtle.left ( turtle.heading ( ) + 90 )
    turtle.right ( 20 )
    turtle.forward ( 10 * scale )
    turtle.right ( 70 )
    turtle.forward ( 1 * scale )
    turtle.right ( 70 )
    turtle.forward ( 10 * scale )
    turtle.backward ( 5 * scale )
    turtle.right ( 90 + 20 )
    turtle.forward ( 4.5 * scale )
    #Move to right of letter and over 1 * scale turtle.up ( )
    turtle.backward ( 4.5 * scale )
    turtle.left ( 110 )
    turtle.forward ( 5 * scale )
    turtle.left ( 70 )
    # Shift position
    turtle.penup()
    turtle.forward ( 2 * scale )
    turtle.pendown()

    ## Letter B
    # Point upwards to begin
    turtle.left ( turtle.heading ( ) + 90 )
    turtle.forward ( 10 * scale )
    turtle.right ( 90 )
    turtle.forward ( 4 * scale )
    turtle.right ( 90 )
    turtle.forward ( 4 * scale )
    turtle.left ( 90 )
    turtle.backward ( 1 * scale )
    turtle.forward ( 3 * scale )
    turtle.right ( 90 )
    turtle.forward ( 6 * scale )
    turtle.right ( 90 )
    turtle.forward ( 6 * scale )
    # Move to right of letter turtle.up ( )
    turtle.right ( 180 )
    turtle.forward ( 6 * scale )
    # Shift position
    turtle.penup()
    turtle.forward ( 2 * scale )
    turtle.pendown()

    ## Letter C
    # Point upwards to begin
    turtle.left ( turtle.heading ( ) + 90 )
    turtle.forward ( 10 * scale )
    turtle.right ( 90 )
    turtle.forward ( 4 * scale )
    turtle.backward ( 4 * scale )
    turtle.right ( 90 )
    ## Start
    turtle.forward( 10 * scale )
    turtle.left( 90 )
    turtle.forward ( 4 * scale )
    # Shift position
    turtle.penup()
    turtle.forward ( 2 * scale )
    turtle.pendown()

    # Letter D
    turtle.left( 90 )
    turtle.forward ( 10 * scale )
    turtle.right ( 90 )
    turtle.forward ( 4 * scale )
    turtle.right ( 30 )
    turtle.forward ( 1 * scale )
    turtle.right ( 60 )
    turtle.forward ( 8.5 * scale )
    turtle.right ( 30 )
    turtle.forward ( 1.15 * scale )
    turtle.right ( 60 )
    turtle.forward ( 4.4 * scale )
    turtle.backward ( 4.4 * scale )
    turtle.right( 180 )
    # Shift position
    turtle.penup()
    turtle.forward ( 2 * scale )
    turtle.pendown()

    # Letter E
    turtle.left( 90 )
    turtle.forward( 10 * scale )
    turtle.right ( 90 )
    turtle.forward ( 5 * scale )
    turtle.backward ( 5 * scale )
    turtle.right( 90 )
    turtle.forward( 5 * scale )
    turtle.left( 90 )
    turtle.forward( 5 * scale )
    turtle.backward( 5 * scale )
    turtle.right( 90 )
    turtle.forward( 5 * scale )
    turtle.left( 90 )
    turtle.forward( 5 * scale )
    turtle.forward( 1 * scale )

    turtle.penup()
    print(turtle.pos())

# draw_star()
# draw_square()
# draw_concentric_squares(5)
# draw_circles()
draw_alphabets()
turtle.exitonclick()