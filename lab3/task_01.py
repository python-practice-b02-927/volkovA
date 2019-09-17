
from graphics import *
window = GraphWin("My first picture", 600, 600)

ground = Polygon(Point(600,400), Point(0,400), Point(0,600), Point(600, 600))
sky = Polygon(Point(600,400), Point(0,400), Point(0,0), Point(600, 0))
color_ground = color_rgb(0, 200, 100)
color_sky = color_rgb(150, 150, 235)
ground.setFill(color_ground)
ground.setOutline(color_ground)
sky.setFill(color_sky)
sky.setOutline(color_sky)

moon = Circle(Point(150, 100), 30)
color_moon = color_rgb(255, 255, 170)
moon.setFill(color_moon)
moon.setOutline(color_moon)

cloud_1 = Circle(Point(400, 150), 15)
cloud_2 = Circle(Point(420, 150), 15)
cloud_3 = Circle(Point(440, 150), 15)
cloud_4 = Circle(Point(415, 130), 15)
cloud_5 = Circle(Point(435, 130), 15)
cloud_1.setFill('white')
cloud_2.setFill('white')
cloud_3.setFill('white')
cloud_4.setFill('white')
cloud_5.setFill('white')

cloud_1.setOutline('white')
cloud_2.setOutline('white')
cloud_3.setOutline('white')
cloud_4.setOutline('white')
cloud_5.setOutline('white')

house = Rectangle(Point(200, 350), Point(400, 400))
roof = Polygon(Point(200, 350), Point(240, 320), Point(360, 320), Point(400, 350), Point(200, 350))
house.setFill('black')
roof.setFill(color_rgb(50, 50, 50))

house_window = Rectangle(Point(330, 385), Point(350, 365))
house_window.setFill('yellow')

house_window_2 = Rectangle(Point(250, 385), Point(270, 365))
house_window_2.setFill('yellow')

ground.draw(window)
sky.draw(window)
moon.draw(window)
house.draw(window)
roof.draw(window)
house_window.draw(window)
house_window_2.draw(window)
cloud_1.draw(window)
cloud_2.draw(window)
cloud_3.draw(window)
cloud_4.draw(window)
cloud_5.draw(window)

window.getMouse()

window.close()