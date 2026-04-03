
import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import pygame
import turtle

# 🎵 MUSIC FUNCTION
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("jana_gana_mana.mp3")
    pygame.mixer.music.play()  

# 🎵 CHECK MUSIC END
def check_music():
    if not pygame.mixer.music.get_busy():  
        show_thanks()
    else:
        root.after(1000, check_music)

# 🙏 SHOW THANKS BELOW FLAG
def show_thanks():
    label = tk.Label(root, text="🙏 THANK YOU 🇮🇳",
                     font=("Arial", 20, "bold"),
                     bg="skyblue")
    label.pack(pady=20)   

    root.after(3000, root.destroy)

# 🖥️ GUI SETUP
root = tk.Tk()
root.title("🇮🇳 Deepseek MoneyMind Flag")
play_music() 

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

root.after(500, play_music)     
root.after(1000, check_music)   

# Attach turtle to tkinter canvas
screen = TurtleScreen(canvas)
screen.bgcolor("skyblue")

flag = RawTurtle(screen)
flag.speed(3)

# CODE START 

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

draw_rectangle("#FF7700", 100)
draw_rectangle("#FFFFFF", 0)
draw_rectangle("#42DA01", -100)

writer = RawTurtle(screen)
writer.penup()
writer.goto(0, 180)
writer.color("black")
writer.hideturtle()
writer.write("HAPPY INDEPENDENCE DAY\nWE ARE INDIAN\nJAI HIND🙏🏻",
             align="center", font=("Arial", 24, "bold"))

chakra = RawTurtle(screen)
chakra.hideturtle()
chakra.speed(0)
chakra.color("#000080")

cx, cy = 0, -50
radius_outer = 50
radius_inner = 40

chakra.penup()
chakra.goto(cx, cy - 50)
chakra.pensize(6)
chakra.pendown()
chakra.circle(50)

chakra.penup()
chakra.goto(cx, cy - 40)
chakra.pensize(2)
chakra.pendown()
chakra.circle(40)

chakra.penup()
chakra.goto(cx, cy - 8)
chakra.begin_fill()
chakra.circle(8)
chakra.end_fill()

for i in range(24):
    chakra.penup()
    chakra.goto(cx, cy)
    chakra.setheading(i * 15)
    chakra.pensize(2)
    chakra.pendown()
    chakra.forward(radius_inner - 3)  

flag.hideturtle()
chakra.hideturtle()


# RUN GUI
root.mainloop()

# Keep the window open
turtle.done()



# py -3.11 indian_flage.py    [COP THIS AND RUN IN TERMINAL TO SEE THE FLAG WITH MUSIC]