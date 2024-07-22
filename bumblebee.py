import pgzrun
import random
WIDTH = 500
HEIGHT = 500

score = 0
game_over = False

bee = Actor("bee")
bee.pos = 100, 100
flower = Actor("flower")
flower.pos = 400, 400

def place_flower():
  flower.x = random.randint(50, 450)
  flower.y = random.randint(50, 450)

def draw():
  screen.blit("grass", (0,0))
  bee.draw()
  flower.draw()
  if game_over:
    screen.fill("blue")
    screen.draw.text("Score: " + str(score), color = "white", topleft = (200, 200), fontsize = (45))

def update():
  if keyboard.left:
    bee.x = bee.x - 5
  if keyboard.right:
    bee.x = bee.x + 5
  if keyboard.up:
    bee.y = bee.y - 5
  if keyboard.down:
    bee.y = bee.y + 5
  
  if bee.colliderect(flower):
    place_flower()
    global score
    score += 1

def time_up():
  global game_over
  game_over = True

clock.schedule(time_up, 60.0)

pgzrun.go()