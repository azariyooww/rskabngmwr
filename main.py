import turtle
import time
import threading

# Inisialisasi layar
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Klik disini sayangg")

# Membuat turtle untuk menulis teks
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)

# Fungsi untuk membuat teks berkedip
def blink_text():
    while True:
        pen.write("Hallo Riska", align="center", font=("Arial", 24, "bold"))
        time.sleep(0.5)
        pen.clear()
        time.sleep(0.5)

# Membuat turtle untuk menggambar bunga
flower = turtle.Turtle()
flower.hideturtle()
flower.speed(10)

# Fungsi untuk menggambar satu kelopak bunga
def draw_petal():
    flower.color("red")
    flower.begin_fill()
    flower.circle(10, 60)
    flower.left(120)
    flower.circle(10, 60)
    flower.left(120)
    flower.end_fill()

# Fungsi untuk menggambar bunga mawar
def draw_flower(x, y):
    flower.penup()
    flower.goto(x, y)
    flower.pendown()
    
    # Menggambar batang bunga
    flower.color("green")
    flower.left(90)
    flower.forward(100)

    # Menggambar kelopak bunga
    for _ in range(6):
        draw_petal()
        flower.right(60)

# Fungsi untuk memulai animasi teks berkedip
def start_blinking():
    t = threading.Thread(target=blink_text)
    t.daemon = True
    t.start()

# Mulai animasi teks berkedip
start_blinking()

# Menetapkan event handler untuk klik layar
screen.onclick(draw_flower)

# Menjaga layar tetap terbuka
turtle.done()
