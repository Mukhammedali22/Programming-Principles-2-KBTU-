import sys, pygame

pygame.init()

size = width, height = 720, 480
screen = pygame.display.set_mode(size)
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
move = 20
radius = 25
x, y = width // 2, height // 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pygame.quit()
            sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            if y >= 2 * radius: y -= move
        elif pressed[pygame.K_DOWN]: 
            if height - y >= 2 * radius: y += move
        elif pressed[pygame.K_LEFT]: 
            if x >= 2 * radius : x -= move
        elif pressed[pygame.K_RIGHT]: 
            if width - x >= 2 * radius: x += move
    
    screen.fill(white)
    ball = pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)