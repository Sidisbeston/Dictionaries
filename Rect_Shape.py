import pgzrun
import random

WIDTH = 500
HEIGHT = 500

def draw():
  r = 0
  g = 255
  b = random.randint(120,255)
  width = WIDTH
  height = HEIGHT-400
  for i in range(20):
    shape = Rect((0, 0),(width, height))
    shape.center = 250, 250
    screen.draw.rect(shape, (r,g,b))
    width -= 25
    height += 25
    r += 10
    g -= 10


pgzrun.go()