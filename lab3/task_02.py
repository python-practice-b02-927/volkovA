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

moon = Circle(Point(200, 150), 30)
color_moon = color_rgb(255, 255, 170)
moon.setFill(color_moon)
moon.setOutline(color_moon)

cloud_11 = Circle(Point(400, 250), 15)
cloud_12 = Circle(Point(420, 250), 15)
cloud_13 = Circle(Point(440, 250), 15)
cloud_14 = Circle(Point(415, 230), 15)
cloud_15 = Circle(Point(435, 230), 15)
cloud_11.setFill('white')
cloud_12.setFill('white')
cloud_13.setFill('white')
cloud_14.setFill('white')
cloud_15.setFill('white')

cloud_11.setOutline('white')
cloud_12.setOutline('white')
cloud_13.setOutline('white')
cloud_14.setOutline('white')
cloud_15.setOutline('white')


cloud_21 = Circle(Point(100, 350), 15)
cloud_22 = Circle(Point(120, 350), 15)
cloud_23 = Circle(Point(140, 350), 15)
cloud_24 = Circle(Point(115, 330), 15)
cloud_25 = Circle(Point(135, 330), 15)
cloud_21.setFill('white')
cloud_22.setFill('white')
cloud_23.setFill('white')
cloud_24.setFill('white')
cloud_25.setFill('white')

cloud_11.setOutline('white')
cloud_12.setOutline('white')
cloud_13.setOutline('white')
cloud_14.setOutline('white')
cloud_15.setOutline('white')


cloud_1 = Circle(Point(200, 150), 15)
cloud_2 = Circle(Point(220, 150), 15)
cloud_3 = Circle(Point(240, 150), 15)
cloud_4 = Circle(Point(215, 130), 15)
cloud_5 = Circle(Point(235, 130), 15)
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


cloud_21.setOutline('white')
cloud_22.setOutline('white')
cloud_23.setOutline('white')
cloud_24.setOutline('white')
cloud_25.setOutline('white')



house = Rectangle(Point(200, 400), Point(400, 450))
roof = Polygon(Point(200, 400), Point(240, 370), Point(360, 370), Point(400, 400), Point(200, 400))
house.setFill('black')
roof.setFill(color_rgb(50, 50, 50))

house_window = Rectangle(Point(330, 435), Point(350, 415))
house_window.setFill('yellow')

house_window_2 = Rectangle(Point(250, 435), Point(270, 415))
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

cloud_11.draw(window)
cloud_12.draw(window)
cloud_13.draw(window)
cloud_14.draw(window)
cloud_15.draw(window)

cloud_21.draw(window)
cloud_22.draw(window)
cloud_23.draw(window)
cloud_24.draw(window)
cloud_25.draw(window)

window.getMouse()

window.close()