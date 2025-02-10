import turtle

def draw_flower():
    turtle.reset()  # Reset the screen to clear any previous drawings
    turtle.speed(10)
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
    turtle.pendown()
    turtle.right(90)

    # Flower base
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    # Petal 1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    # Petal 2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    # Leaves 1
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)

    # Leaves 2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)

    # Add the resized text "tabs to ayien" below the flower
    draw_text("tabs to ayien", -100, -150, font_size=15)  # Resized "tabs to ayien" text

def draw_text(text, x, y, font_size=30):  # Added font_size as a parameter
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("blue")
    
    # Draw each letter one by one, simulating tabs
    letter_spacing = 30  # Adjusted spacing for each letter

    for letter in text:
        if letter == " ":
            turtle.penup()
            turtle.forward(letter_spacing)  # Space between words
            turtle.pendown()
        else:
            turtle.write(letter, font=("Arial", font_size, "bold"))
            turtle.penup()
            turtle.forward(letter_spacing)  # Space between letters
            turtle.pendown()

def on_click(x, y):
    # Check if the click is within the bounds of the "CLICK ME" text area
    if -150 < x < 150 and -50 < y < 50:
        draw_flower()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Draw the "CLICK ME" text starting from the bottom
draw_text("CLICK ME", -150, -50, font_size=30)  # "CLICK ME" with its original size

# Set up the click event to trigger drawing the flower
screen.onclick(on_click)

# Start the turtle graphics loop
turtle.done()
