import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 600

satellites = []
lines = []
next = 0

num_sat = 10
s_time = 0
def make():
  for i in range(num_sat):
    sat = Actor("satellite")
    sat.pos = random.randint(30, 570), random.randint(30, 570)
    satellites.append(sat)

  s_time = time.time()

def draw():
  screen.blit("sky",(0,0))
  for i in range(num_sat):
    satellites[i].draw()
    screen.draw.text(str(i+1),(satellites[i].pos[0], satellites[i].pos[1]+20))
  
  for i in lines:
    screen.draw.line(i[0], i[1], (255,255,255))

make()

def on_mouse_down(pos):
  global next
  global satellites
  global lines
  global num_sat
  if next<num_sat:
    if satellites[next].collidepoint(pos):
      if next:
        lines.append((satellites[next-1].pos, satellites[next].pos))
      next += 1
    else:
      lines = []
      next = 0
pgzrun.go()