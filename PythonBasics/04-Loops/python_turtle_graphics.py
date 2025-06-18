import turtle, colorsys

t = turtle.Turtle(); t.speed(0); turtle.bgcolor("Black")
h = 0

for _ in range(100):
    t.color(colorsys.hsv_to_rgb(h,1,1)); t.circle(100); t.left(36); h+= 0.1
t.hideturtle(); turtle.done()