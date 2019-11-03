from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import gravity

root = tk.Tk()
#frame = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
    def __init__(self, x, y, r, vx, vy, color):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'yellow', 'orange'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        '''что происзодит?'''
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        #FIXME: почему шарики проваливаются вниз в конце?
        if self.y > 590:
                self.vy = abs(self.vy)
        if self.y < 10:
            self.vy = -1*abs(self.vy)
        else:
            self.vy *= 0.999
            self.vx *= 0.999
        if self.x > 790:
            self.vx = -1*abs(self.vx)
        if self.x < 10:
            self.vx = abs(self.vx)

        self.vy -= 0.02
        self.y -= self.vy
        self.x += self.vx
        self.set_coords()


    def collision_check(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        dist = math.sqrt( (self.x - obj.x)**2 + (self.y - obj.y)**2)
        if dist > (obj.r + self.r):
            return False
        else:
            return True


class Gun():
    def __init__(self):
        self.power = 10
        self.check_aim = 0
        self.an = 0
        self.id = canv.create_line(20,450,50,420,width=7)

    def aim_start(self, event):
        ''''''
        self.check_aim = 1

    def aim_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, balls_number
        balls_number += 1
        new_ball = Ball(20 + max(self.power, 20) * math.cos(self.an),
                        450 + max(self.power, 20) * math.sin(self.an),
                        5, (0.05*self.power)*math.cos(self.an),
                        (-0.05*self.power)*math.sin(self.an),
                        'yellow'
                        )
        balls += [new_ball]
        self.check_aim = 0
        self.power = 10


    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.check_aim:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.power, 20) * math.cos(self.an),
                    450 + max(self.power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.check_aim:
            if self.power < 100:
                self.power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = id
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        r = self.r = rnd(5, 50)
        x = self.x = rnd(600, 800 - r)
        y = self.y = rnd(300, 600 - r)

        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


def text_ending(n):
    if n//10 == 1 or n//100 ==10 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 or n % 10 == 0:
        return 'выстрелов'
    if n % 10 == 1:
        return 'выстрел'
    if n == 2 or n == 3 or n == 4 or n == 5:
        return 'выстрела'


target1 = Target()
textt = canv.create_text(400, 300, text='', font='28')
gun1 = Gun()
balls_number = 0
balls = []
targets = []
targets += [target1]

def new_game(event=''):
    global target1, textt, balls, balls_number, Gun
    target1.new_target()
    while targets:
        canv.bind('<Button-1>', gun1.aim_start)
        canv.bind('<ButtonRelease-1>', gun1.aim_end)
        canv.bind('<Motion>', gun1.targetting)
        for b in balls:
            b.move()
            for t in targets:
                if b.collision_check(t) and t.live:
                    t.live = 0
                    t.hit()
                    gun1.targetting()
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(textt, text='Вы уничтожили цель за ' + str(balls_number) + ' ' + text_ending(balls_number) + '!')
                    target1.new_target()
            gun1.targetting()
            gun1.power_up()
        canv.update()
        time.sleep(0.005)
    canv.itemconfig(textt, text='')
    canv.delete(Gun)
    root.after(500, new_game)
    
    
new_game()
root.mainloop()
