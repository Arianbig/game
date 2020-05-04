from pygame_functions import *
import math
import random
import pygame
from math import radians as Rad

# def fire(x,y)


setAutoUpdate(False)

# create Screen
Pushed = 2
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
    meteorX = (random.randint(15, 95))
    meteorY = (random.randint(15, 623))

elif randloc == 2:
    meteorX = (random.randint(865, 945))
    meteorY = (random.randint(15, 623))

elif randloc == 3:
    meteorX = (random.randint(15, 945))
    meteorY = (random.randint(15, 95))

elif randloc == 4:
    meteorX = (random.randint(15, 945))
    meteorY = (random.randint(543, 623))

# meteor moving to middle


meteorangle = (math.atan2(319 - meteorY, 480 - meteorX)) * 180 / math.pi + 90  # angle of 2 points formula
meteor = makeSprite("meteor.png")
meteoralive = True
showSprite(meteor)
moveSprite(meteor, meteorX, meteorY, True)
rotateSprite(meteor, meteorangle)

# make rocket
R = -100
rocketrX = 480
rocketrY = 319
rocketangle = (math.atan2(319 - rocketrY, 480 - rocketrX)) * 180 / math.pi + 90
rocket = makeSprite("rocket1.gif")
addSpriteImage(rocket, "rocket2.gif")
addSpriteImage(rocket, "rocket3.gif")
addSpriteImage(rocket, "rocket4.gif")
addSpriteImage(rocket, "rocket5.gif")
addSpriteImage(rocket, "rocket6.gif")
moveSprite(rocket, 480, 319, True)
x = 0  # angle of ship
y = 0  # angle of rocket
z = 0  # angle of rocket temprory
running = True
launch = False
explosion = makeSprite("explosion.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            launch = True
    if keyPressed("esc"):
        running = False
    elif keyPressed("left") and launch == False:  # rotation left with rocket
        rotateSprite(Ship, x)
        y += 1
        x -= 1
        rocketrX = rocketrX + (R * math.sin(math.radians(y)))
        rocketrY = rocketrY - (R * (1 - math.cos(math.radians(y)))) + R
        rocketangle = (math.atan2(rocketrY - 319, rocketrX - 480)) * 180 / math.pi + y + 180
        rocketrX = 480
        rocketrY = 319
    elif keyPressed("left") and launch == True:  # rotation left without rocket
        rotateSprite(Ship, x)
        x -= 1
        z += 1
        print("z", z)
    elif keyPressed("right") and launch == False:  # rotation right with rocket
        rotateSprite(Ship, x)
        y -= 1
        x += 1
        rocketrX = rocketrX + (R * math.sin(math.radians(y)))
        rocketrY = rocketrY - (R * (1 - math.cos(math.radians(y)))) + R
        rocketangle = (math.atan2(rocketrY - 319, rocketrX - 480)) * 180 / math.pi + y + 180
        rocketrX = 480
        rocketrY = 319

        # pause(15)
    elif keyPressed("right") and launch == True:  # rotation right without rocket
        rotateSprite(Ship, x)
        x += 1
        z -= 1
        print("z", z)
    if launch == True:
        changeSpriteImage(rocket, 1)
        pause(6)
        changeSpriteImage(rocket, 2)
        pause(6)
        changeSpriteImage(rocket, 3)
        pause(6)
        changeSpriteImage(rocket, 4)
        pause(6)
        changeSpriteImage(rocket, 5)
        pause(6)
    if (410 < meteorX < 542) and (257 < meteorY < 381):
        print("Game Over")
    if (rocketrX - 50 < meteorX < rocketrX + 50) and (rocketrY - 50 < meteorY < rocketrY + 50):
        killSprite(meteor)
        killSprite(rocket)
        moveSprite(explosion, meteorX, meteorY, True)
        showSprite(explosion)
        moveSprite(rocket, 480, 319, True)
        rocketrX = 480
        rocketrY = 319
        killSprite(rocket)
        y = z + y
        z = 0
        print(y)
        launch = False
    if meteoralive:
        moveSprite(meteor, meteorX, meteorY, True)
        meteorX = meteorX + math.cos(Rad(meteorangle - 90))
        meteorY = meteorY + math.sin(Rad(meteorangle - 90))
    if not (0 < rocketrX < 980 and 0 < rocketrY < 638):
        moveSprite(rocket, 480, 319, True)
        rocketrX = 480
        rocketrY = 319
        killSprite(rocket)
        y = z + y
        z = 0
        print(y)
        launch = False
    elif 0 < rocketrX < 980 and 0 < rocketrY < 638 and launch == True:
        rotateSprite(rocket, -y)
        rocketrX = rocketrX + math.cos(Rad(rocketangle - y + 180))
        rocketrY = rocketrY + math.sin(Rad(rocketangle - y + 180))
        moveSprite(rocket, rocketrX, rocketrY, True)
        showSprite(rocket)
    updateDisplay()
    fps = tick(29)
    changeLabel(FPS, "FPS: {0}".format(str(round(fps, 2))))
