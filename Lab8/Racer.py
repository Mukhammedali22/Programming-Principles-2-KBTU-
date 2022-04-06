#Imports
import pygame, sys, random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (400, 600)
SPEED, USER_SPEED = 5, 5
SCORE, MONEY = 0, 0
PAUSE, END = False, False

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
name = font.render("Street racer", True, BLACK)
restart_button = font_small.render("press \"R\" to restart the game", True, BLACK)
pause_button = font_small.render("press \"P\" to pause the game", True, BLACK) 
exit_button = font_small.render("press \"X\" to exit the game", True, BLACK)

#loading needed images
background = pygame.image.load("images\\AnimatedStreet.png")
coin = pygame.image.load("images\\Money.jpg")
enemy = pygame.image.load("images\\Enemy.png")
player = pygame.image.load("images\\Player.png")
road = pygame.image.load("images\\Road.png")

#Create a green screen and show game splash screen
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
DISPLAYSURF.fill(GREEN)
DISPLAYSURF.blit(name, (15, 150))
DISPLAYSURF.blit(restart_button, (30, 450))
DISPLAYSURF.blit(pause_button, (30, 500))
DISPLAYSURF.blit(exit_button, (30, 550))
pygame.display.set_caption("Street Racer")
pygame.display.update()
time.sleep(2)

class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(15, 385), -15)

    def change_location(self):
        self.rect.center = (random.randint(15, 385), -15)

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > 600:
            self.rect.center = (random.randint(15, 385), -15)

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), -50)
    
    def move(self):
        global SCORE, USER_SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            if SCORE % 10 == 0 and SCORE != 0:
                USER_SPEED += 1
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), -50)

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 5:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-USER_SPEED, 0)
        if self.rect.right < SCREEN_WIDTH - 5:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(USER_SPEED, 0)
        if self.rect.top > 5:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -USER_SPEED)
        if self.rect.bottom < SCREEN_HEIGHT - 5:        
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, USER_SPEED)

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)
              
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
M1 = Money()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)
moneys = pygame.sprite.Group()
moneys.add(M1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2500)

#Starting point of our game time
start_time = time.time()

background_music = pygame.mixer.music.load("sounds\\background.wav")
pygame.mixer.music.play(-1)
#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if PAUSE: PAUSE = False
            else: PAUSE = True
                
        #Restart the game and initialize main variables
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            for entity in all_sprites:
                entity.__init__() 
            M1.change_location()
            SCORE, MONEY = 0, 0
            SPEED, USER_SPEED = 5, 5
            PAUSE, END = False, False
            start_time = time.time()
            #background_music = pygame.mixer.music.load("sounds\\background.wav")
            pygame.mixer.music.play(-1)
            
    #Check game state     
    if END:

        pass

    else:    
        
        #Check game state
        if PAUSE:

            pass

        else:

            DISPLAYSURF.blit(background, (0, 0))
            scores = font_small.render(str(SCORE), True, BLACK)
            money_scores = font_small.render(str(MONEY), True, BLACK)
            current_speed = font_small.render("Your speed: " + str(USER_SPEED), True, BLACK)
            enemy_speed = font_small.render("Enemy speed: " + str(SPEED), True, BLACK)
            DISPLAYSURF.blit(scores, (10, 10))
            DISPLAYSURF.blit(money_scores, (365, 10))
            DISPLAYSURF.blit(current_speed, (10, 50))
            DISPLAYSURF.blit(enemy_speed, (10, 90))

            #Moves and Re-draws all Sprites
            for entity in all_sprites:
                entity.move()
                entity.draw()
            
            #Checks collision and change coordinates of the coin randomly   
            if pygame.sprite.spritecollideany(P1, moneys):
                MONEY += 1
                pygame.mixer.Sound('sounds\\Mario Coin.mp3').play()
                M1.change_location()
            
            #To set end point
            end_time = time.time()
            x = round(end_time - start_time, 2)
            game_time = font_small.render("time: " + str(x), True, BLACK)
            DISPLAYSURF.blit(game_time, (10, 140))

            #To be run if collision occurs between Player and Enemy
            if pygame.sprite.spritecollideany(P1, enemies):
                
                END = True

                pygame.mixer.music.stop()
                pygame.mixer.Sound('sounds\\crash.wav').play()
                time.sleep(1)

                scores = font_small.render("Your Score: " + str(SCORE), True, BLACK)
                money_scores = font_small.render("Your Money: " + str(MONEY), True, BLACK)
                game_time = font_small.render("Seconds: " + str(x), True, BLACK)

                DISPLAYSURF.fill(RED)
                DISPLAYSURF.blit(game_over, (30, 150))
                DISPLAYSURF.blit(game_time, (30, 300))
                DISPLAYSURF.blit(scores, (30, 350))
                DISPLAYSURF.blit(money_scores, (30, 400))
                DISPLAYSURF.blit(restart_button, (30, 450))
                DISPLAYSURF.blit(pause_button, (30, 500))
                DISPLAYSURF.blit(exit_button, (30, 550))
                
                pygame.display.update()
                   
            pygame.display.update()
            FramePerSec.tick(FPS)
