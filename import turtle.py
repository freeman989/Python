import turtle

pen = turtle.Turtle()

window = turtle.Screen()
window.title('MyWindowForTurtle')
window.setup(1920,1080,0,0)
window.bgcolor('black')
pen.color('red')
pen.speed(10)
pen.width(2)
angle = 1
start = 50
while True:
    pen.fillcolor('blue')
    pen.begin_fill()
    for j in range(4):
        pen.forward(20)
        pen.right(100)
    pen.end_fill()
    pen.left(angle)
    pen.forward(40)
    if(angle < 20):
        angle += 10
    pen.write(pen.xcor())
    if(pen.xcor() > 960 or pen.xcor() < -960 or pen.ycor() > 540 or pen.ycor() < -540):
        pen.setposition(-950,start)
        start +=5
        
    

pen.hideturtle()
window.exitonclick()
window.mainloop()