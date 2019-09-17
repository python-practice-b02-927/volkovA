def house(x, y):              # x, y - coordinates of lower left corner
    house = Rectangle(Point(x, y), Point(x + 200, y - 50))
    roof = Polygon(Point(x, y - 50), Point(x + 30, y - 80), Point(x + 170, y - 80), Point(x + 200, y - 50), Point(x, y - 50))
    house.setFill('black')
    roof.setFill(color_rgb(50, 50, 50))

    house_window_1 = Rectangle(Point(x + 50, y - 15), Point(x + 70, y - 35))
    house_window_2 = Rectangle(Point(x + 150, y - 15), Point(x + 130, y - 35))
    house_window_1.setFill('yellow')
    house_window_2.setFill('yellow')

    house.draw(window)
    roof.draw(window)
    house_window_1.draw(window)
    house_window_2.draw(window)


def moon(x, y):                # x, y - coordinates of center
    moon = Circle(Point(x, y), 30)
    color_moon = color_rgb(255, 255, 170)
    moon.setFill(color_moon)
    moon.setOutline(color_moon)

    moon.draw(window)


from graphics import *
window = GraphWin("My first picture", 600, 600)

house(100, 100)
moon(500, 300)

window.getMouse()

window.close()


