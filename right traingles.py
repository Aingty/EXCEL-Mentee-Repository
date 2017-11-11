import math, turtle

franklin = turtle.Turtle()
franklin.shape("turtle")
franklin.speed(0)

def draw_triangle(name, color, adjacent_length, angle, x, y):
    name.penup()
    name.color (color)
    name.goto(x, y)
    name.pendown()
        
    hypotenuse = adjacent_length / math.cos(math.radians(angle))
    opposite = math.tan (math.radians(angle)) * adjacent_length
    
    print (hypotenuse, "\n" , adjacent_length)
    
    name.right(180)
    name.right(180 - angle)
    name.forward(hypotenuse)
    name.right(90 + angle)
    name.forward(opposite)
    name.right(90)
    name.forward(adjacent_length)
    name.right(180)
    
def draw_shape (name, color, size, angle, x, y):
    name.color(color)
    name.goto(x, y)
    
    draw_triangle(name, color, size, angle, x, y)
    draw_triangle(name, color, size, angle, x, y)
    draw_triangle(name, color, size, angle, x, y)
    draw_triangle(name, color, size, angle, x, y)
#draw_triangle(franklin, "red", 150, 15, 0, 0)
#draw_triangle(franklin, "pink", 75, 70.25, 65, 200)
#draw_triangle(franklin, "green", 100, 29.8, -250, -250)

draw_shape (franklin, "blue", )
turtle.exitonclick()