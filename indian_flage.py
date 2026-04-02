import turtle

# Screen setup
screen = turtle.Screen()
screen.title("🇮🇳 Indian Flag")
screen.bgcolor("skyblue")

# Turtle setup for flag
flag = turtle.Turtle()
flag.speed(3)

# Function to draw rectangle
def draw_rectangle(color, y):
    flag.penup()
    flag.goto(-200, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(400)
        flag.right(90)
        flag.forward(100)
        flag.right(90)
    flag.end_fill()

# Draw saffron, white, green stripes
draw_rectangle("#FF7700", 100)   # Saffron
draw_rectangle("#FFFFFF", 0)     # White
draw_rectangle("#42DA01", -100)  # Green

# Write "WE ARE INDIAN" on top
writer = turtle.Turtle()
writer.penup()
writer.goto(0, 180)
writer.color("black")
writer.hideturtle()
writer.write("HAPPY INDEPENDENCE DAY\nWE ARE INDIAN\n\tJAI HIND🙏🏻", align="center", font=("Arial", 24, "bold"))

# Draw Ashoka Chakra in center of white band
chakra = turtle.Turtle()
chakra.penup()
chakra.goto(0, -50)  # ⬅️ Now exactly centered
chakra.pendown()
chakra.color("#0008F4")
chakra.pensize(2)

# Draw outer circle
chakra.circle(0)

# Draw 24 spokes
for i in range(25):
    chakra.penup()
    chakra.goto(0, -45)  # ⬅️ Adjusted to Chakra center
    chakra.setheading(i * 15)
    chakra.pendown()
    chakra.forward(45)

# Hide turtles
flag.hideturtle()
chakra.hideturtle()

# Keep the window open
turtle.done()
