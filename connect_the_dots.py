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
  global s_time
  for i in range(num_sat):
    sat = Actor("satellite")
    sat.pos = random.randint(30, 570), random.randint(30, 570)
    satellites.append(sat)

  s_time = time.time()

def draw():
  global next, num_sat
  screen.blit("sky",(0,0))
  for i in range(num_sat):
    satellites[i].draw()
    screen.draw.text(str(i+1),(satellites[i].pos[0], satellites[i].pos[1]+20))
  
  for i in lines:
    screen.draw.line(i[0], i[1], (255,255,255))
  if next<num_sat:
    duration = time.time()-s_time
    screen.draw.text(str(round(duration, 1)), (50, 50))
  else:
    screen.draw.text(str(duration), (50, 50))
make()
def update():
  pass

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