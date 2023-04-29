import pygame
import random
import math
#Initializing pygame
pygame.init()

#screen window size
screen = pygame.display.set_mode((800,600))

#Back ground image loader
back_ground = pygame.image.load('png/bg.jpg')
def display_bg():
    screen.blit(back_ground, (0,0))

#score properties
score = 0
x_pos = 10
y_pos = 10
score_font = pygame.font.Font('freesansbold.ttf', 20)


#ship Properties
ship = pygame.image.load('png/001-rocket.png')
shipX = 370
shipY = 500
change = 0

#Alien Properties
alien_list =[]
alien_x = []
alien_y = []

#Number of Aliens and their properties
for i in range(4):
    alien = pygame.image.load('png/001-alien.png')
    alien_list.append(alien)
    alien_x.append(random.randint(40, 800))
    alien_y.append(random.randint(40, 150))

#Bullet properties
bullet = pygame.image.load('png/001-bullet.png')
bulletX = shipX
bulletY = shipY
bullet_change = 0
state = False

#Display Bullet at x,y 
def bullet_display(x,y):
    stage = True
    screen.blit(bullet, (x,y))

#Display alien at x,y
def alien_display(x,y,alien):
    screen.blit(alien, (x,y))

#Display ship at x,y
def ship_display(x,y):
    screen.blit(ship,(x, y))

#Checking For Collision to increase score
def isCollision(b_x,b_y,a_x,a_y):
    distance = math.sqrt(math.pow((b_x-a_x), 2) + math.pow((b_y-a_y), 2))
    if distance < 27:
        return True
    else: return False

# Display Scores
def scores():
    rendered_score = score_font.render('Score :'+str(score), True, (222, 224, 215))
    screen.blit(rendered_score, (x_pos,y_pos))

# Dispaly Game Over
def gameover():
    font = pygame.font.Font('freesansbold.ttf', 60)
    your_score = pygame.font.Font('freesansbold.ttf', 30)
    game_over = font.render("GAME OVER!!", True, (222, 224, 215))
    continue_font = pygame.font.Font('freesansbold.ttf', 30)
    continue_render = continue_font.render('Please press ENTER to Continue', True, (186, 194, 188))
    your_score_render = your_score.render('Your Score : {}'.format(score), True, (106, 247, 142))
    screen.blit(your_score_render, (260,400))
    screen.blit(continue_render, (170,180))
    screen.blit(game_over, (230,280))

running = True
count = 10000


#Running Game Loop till 10000
while running:

    #Loop break condition
    if count < 1:
        running = False
    count -= 1

    #GET events and taking inputs from keyboard btns
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event.type)
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left key pressed')
                change = -2
            if event.key == pygame.K_RIGHT:
                print('right key pressed')
                change = 2
            if event.key == pygame.K_SPACE:
                state = True
                bullet_change = -10
            if event.key == pygame.K_KP_ENTER or event.key == pygame.KSCAN_KP_ENTER:
                print("pressed enter")
                count= 10000
                score = 0
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                change = 0
                
                #bullet_change = -0.2
                #state = False
                
    
    #Screen fill with background image
    display_bg()

    #Ship Movement for LEFT_KEY and RIGHT_KEY
    shipX += change
    if shipX > 750:
        shipX = 750
    if shipX < 50 :
        shipX = 50


    #Defining alien movement
    for i,alien in enumerate(alien_list):    
        alien_x[i] += 0.5
        if alien_x[i] > 780:
            alien_x[i] = 50
            alien_y[i] += 50

        # Check if Alien crossed the ship and display game over
        if alien_y[i] > 450:
            counter = 2500
            while counter > 0:
                gameover()
                counter -= 1
            running = False

        # increasing score based on collisions
        if isCollision(bulletX, bulletY, alien_x[i], alien_y[i]) :
            score += 1
            alien_x[i] = random.randint(40, 800)
            alien_y[i] = random.randint(40, 150)

        #alien Display on screeen
        alien_display(alien_x[i], alien_y[i], alien)


    #Bullet Mechanics based on state of bullet
    bulletX = shipX
    if state :
        bullet_display(bulletX, bulletY)
        bulletY += bullet_change    
    if bulletY < 1 :
        state =False
        bulletY = 500

    # Display of scores
    scores()   

    #Display Ship on Screen
    ship_display(shipX, shipY)

    #Ending the game for Timeout
    if count < 2000:
        gameover()

    #updating screen every single iteration
    pygame.display.update()