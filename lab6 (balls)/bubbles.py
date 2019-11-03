import tkinter as tk
from random import randrange as rnd, choice
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('1200x600')
canv = tk.Canvas(root, bg='black')
canv.pack(fill=tk.BOTH, expand=1)


colors = ['yellow', 'green', 'red', 'white', 'orange', 'purple', 'medium orchid']
balls = []
squares = []
points = 0


class Bubble:
    """Пузырьки. Первый тип мишеней. Их много, двигаются с малыми скоростями, только снизу вверх.
    Время жизни ограничено"""

    def __init__(self, x, y, vx, vy, r, color, live):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.color = color
        self.id = ''
        self.live = live

    def move(self):
        """Движение с отражением от боковых стен"""

        if self.x + self.r > 1200 or self.x - self.r < 0:
            self.vx *= -1
        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)
        self.live -= 1

    def check_upper_border(self):
        """Проверка на вылет за предел окна"""

        if self.y + self.r < 0:
            return True
        return False

    def murder(self):
        """Удаление с экрана"""

        canv.delete(self.id)


class Square:
    """Второ тип мишеней. Только одна на экране. Большие скорости, время жизни не ограничено"""

    def __init__(self, x, y, vx, vy, size, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color
        self.id = ''

    def move(self):
        """Движение с отражением от стен"""

        if self.x + self.size > 1200 or self.x < 0:
            self.vx *= -1
        if self.y + self.size > 600 or self.y < 0:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)

    def murder(self):
        """Удаление с экрана"""

        canv.delete(self.id)


def rnd_bubl_creation():
    """Создание пузырька со случайными параметрами"""

    global balls
    r = rnd(8, 30)
    x = rnd(r, 1200 - r)
    y = rnd(580, 600)
    vx = rnd(-4, 4)
    vy = rnd(-8, -4)
    live = rnd(30, 100)
    color_helper = rnd(10, 100, 1)
    color = '#' + '00' + str(color_helper) + 'ff'
    b = Bubble(x, y, vx, vy, r, color, live)
    b.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=color, outline='white')
    balls += [b]


def rnd_square_creation():
    """Создание квадрата со случаными параметрами"""

    global squares
    size = 40
    x = rnd(0, 1200 - size)
    y = rnd(0, 600 - size)
    vx = rnd(-20, 20)
    vy = rnd(-20, 20)
    color = choice(colors)
    s = Square(x, y, vx, vy, size, color)
    s.id = canv.create_rectangle(x, y, x + size, y + size, fill=color)
    squares += [s]


def hit(event):
    """Исчезновение мишени и увеличение очков при попадании. Скорость объекта и его размер влияют"""

    global balls, points, squares
    for b in balls:
        if (event.x - b.x)**2 + (event.y - b.y)**2 < b.r**2:
            points += round(30 / b.r) + round(0.1*(b.vy**2 + b.vx**2)**0.5)
            canv.itemconfig(legend, text=str(points))
            b.murder()
            balls.remove(b)
    for s in squares:
        if s.x < event.x < s.x + s.size and s.y < event.y < s.y + s.size:
            points += round(0.6*(s.vy**2 + s.vx**2)**0.5)
            canv.itemconfig(legend, text=str(points))
            s.murder()
            squares.remove(s)
            rnd_square_creation()


legend = canv.create_text(50, 50, text=str(points), font='28', fill='white')

rnd_square_creation()
canv.bind('<Button-1>', hit)
while True:
    rnd_bubl_creation()
    for s in squares:
        s.move()
    for ball in balls:
        ball.move()
        if ball.live == 0 or ball.check_upper_border():
            ball.murder()
            balls.remove(ball)
    canv.update()
    time.sleep(0.1)


root.mainloop()