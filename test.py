from pygame_functions import *
import math
import random
import pygame
from math import radians as Rad

# def fire(x,y)


setAutoUpdate(False)

# create Screen
Pushed = 1
screenSize(980, 638)
# add background image

background = setBackgroundImage("Space.png")

# show FPS

FPS = makeLabel("FPS :", 30, 10, 10, "white")
showLabel(FPS)

# Make a ship
Ship = makeSprite("Ship.png")
showSprite(Ship)
moveSprite(Ship, 480, 319, True)
randloc = random.randint(1, 4)
# Make a random meteor
if randloc == 1:
    meteorX = (random.randint(30, 80))
    meteorY = (random.randint(30, 80))

elif randloc == 2:
    meteorX = (random.randint(30, 80))
    meteorY = (random.randint(558, 608))

elif randloc == 3:
    meteorX = (random.randint(900, 950))
    meteorY = (random.randint(48, 590))

else:
    meteorX = (random.randint(900, 950))
    meteorY = (random.randint(558, 608))

# meteor moving to middle


meteorangle = (math.atan2(319 - meteorY, 480 - meteorX)) * 180 / math.pi + 90  # angle of 2 points formula
meteor = makeSprite("meteor.png")
meteoralive = True
showSprite(meteor)
moveSprite(meteor, meteorX, meteorY, True)
rotateSprite(meteor, meteorangle)

# make rocket
rocket = makeSprite("rocket1.gif")
addSpriteImage(rocket, "rocket2.gif")
addSpriteImage(rocket, "rocket3.gif")
addSpriteImage(rocket, "rocket4.gif")
addSpriteImage(rocket, "rocket5.gif")
addSpriteImage(rocket, "rocket6.gif")
showSprite(rocket)
moveSprite(rocket, 480, 319,True)
x = 90  # angle of ship
y = 90  # angle of rocket
z = 90
running = True
launch = False
rocketX = 0
rocketY = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            launch = True

    if keyPressed("esc"):
        running = False
    elif keyPressed("left"):  # rotation left
        rotateSprite(Ship, x)
        rotateSprite(rocket, y)
        y -= 1
        x -= 1
        z += 1
    elif keyPressed("right"):  # rotation right
        rotateSprite(Ship, x)
        rotateSprite(rocket, y)
        y += 1
        x += 1
        z -= 1
    if (410 < meteorX < 542) and (257 < meteorY < 381):
        print("Game Over")
    if meteoralive:
        moveSprite(meteor, meteorX, meteorY, True)
        meteorX = meteorX + math.cos(Rad(meteorangle - 90))
        meteorY = meteorY + math.sin(Rad(meteorangle - 90))
    if launch:
        if math.tan(Rad(z)) > 0:
            rocketX += 1
        else:
            rocketX -= 1

        # if z == 90:
        #     rocketX = 480
        #     rocketY -= 1
        # elif z == 270:
        #     rocketX = 480
        #     rocketY += 1
        # else:
        rocketY = math.tan(Rad(z)) * rocketX
        foo = 480 + rocketX
        bar = 319 - rocketY
        print(foo, bar, math.tan(Rad(z)), z, x, y)
        moveSprite(rocket, foo, bar, True)
        pause(50)
        # rocketrX = rocketrX + math.cos(Rad(meteorangle - 90))
        # rocketrY = rocketrY + math.sin(Rad(meteorangle - 90))
    fps = tick(60)
    updateDisplay()
    changeLabel(FPS, "FPS: {0}".format(str(round(fps, 2))))
