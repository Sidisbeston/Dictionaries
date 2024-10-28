import pgzrun
import random

HEIGHT = 600 
WIDTH = 1200

score = 0
white = (255, 255, 255)
blue = (0, 0, 255)
ship = Actor("galaga")
bug = Actor("bug")
bullet = Actor("bullet")

ship.pos = (WIDTH // 2, HEIGHT - 60)
speed = 10
bullets = []
enemies = []

for x in range(8):
  for y in range(4):
    enemies.append(Actor("bug"))
    enemies[-1].x = 100+50*x
    enemies[-1].y = 80+50*y
direction = 1
ship.dead = False
ship.countdown = 90
def display_score():
  screen.draw.text(str(score), (50, 30))

def on_key_down(key):
  if ship.dead == False:
      if key == keys.SPACE:
        bullets.append(bullet)
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

  
def update():
  global score
  global direction
  moveDown = False
  if ship.dead == False:
    if keyboard.left:
      ship.x -= speed
      if ship.x <= 0:
        ship.x = 0
    elif keyboard.right:
      ship.x += speed
      if ship.x >= WIDTH:
        ship.x = WIDTH

  for bullet in bullets:
    if bullet.y <= 0:
      bullets.remove(bullet)
    else:
      bullet.y -= 10
  if len(enemies) == 0:
    game_over()
  if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 80):
    moveDown = True
    direction *= -1
  for enemy in enemies:
    enemy.x += direction*5
    if moveDown == True:
      enemy.y += 100
    for bullet in bullets:
      if enemy.colliderect(bullet):
        score += 100
        bullets.remove(bullet)
        enemies.remove(enemy)
        if len(enemies) == 0:
          game_over()
    if enemy.colliderect(ship):
      ship.dead = True
  if ship.dead:
    ship.countdown -= 1
  if ship.countdown == 0:
    ship.dead = False
    ship.countdown = 90
        
def draw():
  screen.clear()
  screen.fill(blue)
  for bullet in bullets:
    bullet.draw()
  for enemy in enemies:
    enemy.draw()
  if ship.dead == False:
    ship.draw()
  display_score()
  if len(enemies) == 0:
    game_over()

def game_over():
  screen.draw.text("game over", (250, 300))








pgzrun.go()

