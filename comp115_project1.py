import turtle
import random

# =======================
# Setup 
# =======================
drawing_screen = turtle.Screen()
drawing_screen.title("Majestic Husky Head")
drawing_screen.bgcolor("lightcyan")

alex = turtle.Turtle()
alex.speed(0)
alex.hideturtle()

drawing_screen.bgcolor("midnightblue")

def draw_moon():
    # Big white circle
    draw_filled_circle(-220, 200, 40, "white", "white")

    # Smaller background-colored circle to create crescent effect
    draw_filled_circle(-200, 210, 35, "midnightblue", "midnightblue")


def draw_cloud(x, y, size):
    # Cloud made of overlapping circles
    draw_filled_circle(x, y, size, "white", "white")
    draw_filled_circle(x + size, y + 10, size, "white", "white")
    draw_filled_circle(x - size, y + 5, size, "white", "white")
    draw_filled_circle(x + size * 2, y, size, "white", "white")

def draw_clouds():
    for x in range(-300, 301, 120):
        draw_cloud(x, -220, 30)



def draw_star(x, y, size):
    alex.color("white")
    move_to(x, y)
    alex.begin_fill()
    for _ in range(5):
        alex.forward(size)
        alex.left(144)  # 5-point star angle
    alex.end_fill()

def draw_stars():
    for _ in range(25):   # number of stars
        x = random.randint(-300, 300)
        y = random.randint(-50, 250)
        size = random.randint(5, 15)
        draw_star(x, y, size)


# =======================
# Helper functions
# =======================

def move_to(x, y):
    alex.penup()
    alex.goto(x, y)
    alex.pendown()

def draw_filled_circle(x, y, r, fill_color, outline_color="black"):
    alex.color(outline_color, fill_color)
    move_to(x, y - r)
    alex.begin_fill()
    alex.circle(r)
    alex.end_fill()

def draw_triangle_from_point(x, y, side, fill_color, outline_color="black"):
    # triangle using ONLY forward + left, and for-loop 
    alex.color(outline_color, fill_color)
    move_to(x, y)
    alex.begin_fill()
    for _ in range(3):
        alex.forward(side)
        alex.left(120)
    alex.end_fill()

# =========================
# One center for everything 
# =========================
CX = 0
CY = 40   

# =======================
# Husky face parts
# =======================

def draw_head():
    draw_filled_circle(CX, CY, 120, "lightgray", "black")

def draw_ears():
    # Outer ears
    draw_triangle_from_point(CX - 140, CY + 95, 90, "dimgray", "black")
    draw_triangle_from_point(CX + 50,  CY + 95, 90, "dimgray", "black")

    # Inner ears
    draw_triangle_from_point(CX - 120, CY + 90, 55, "lightpink", "black")
    draw_triangle_from_point(CX + 70,  CY + 90, 55, "lightpink", "black")

def draw_face_mask():
    # White mask (overlapping circles = easy + husky-like)
    draw_filled_circle(CX,      CY - 10, 85, "white", "white")
    draw_filled_circle(CX - 50, CY - 20, 55, "white", "white")
    draw_filled_circle(CX + 50, CY - 20, 55, "white", "white")

    # Gray cap (top marking)
    draw_filled_circle(CX, CY + 35, 80, "gray", "gray")

def draw_eyes():
    for x in [CX - 45, CX + 45]:
        draw_filled_circle(x, CY + 10, 14, "black", "black")          # outer eye
        draw_filled_circle(x, CY + 8, 7, "deepskyblue", "black")      # iris
        draw_filled_circle(x + 5, CY + 26, 3, "white", "white")       # highlight

def draw_brows():
    # Simple majestic brows (short lines)
    alex.color("black")
    alex.pensize(4)

    # Left brow
    move_to(CX - 75, CY + 45)
    alex.setheading(20)
    alex.forward(30)

    # Right brow
    move_to(CX + 45, CY + 45)
    alex.setheading(160)
    alex.forward(30)

    alex.pensize(1)

def draw_nose_and_mouth():
    # Nose
    draw_filled_circle(CX, CY - 35, 10, "black", "black")

    # Mouth lines (use setheading so it doesn't get messed up by earlier turns)
    alex.color("black")
    alex.pensize(3)

    # Left mouth line
    move_to(CX, CY - 45)
    alex.setheading(-60)
    alex.forward(18)

    # Right mouth line
    move_to(CX, CY - 45)
    alex.setheading(-120)
    alex.forward(18)

    alex.pensize(1)

def draw_neck_fur():
    # Row of fur triangles under the head (loop = good marks)
    for x in [CX - 80, CX - 40, CX, CX + 40, CX + 80]:
        draw_triangle_from_point(x - 15, CY - 165, 40, "white", "black")

def draw_blush():
    draw_filled_circle(CX - 70, CY - 35, 12, "lightpink", "lightpink")
    draw_filled_circle(CX + 70, CY - 35, 12, "lightpink", "lightpink")

# =======================
# Draw order (layering)
# =======================
draw_stars()
draw_moon()
draw_clouds()
draw_ears()
draw_head()
draw_face_mask()
draw_eyes()
draw_brows()
draw_nose_and_mouth()
draw_blush()
draw_neck_fur()

drawing_screen.mainloop()


