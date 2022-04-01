import sys, pygame

pygame.init()

white = 255, 255, 255
black = 0, 0, 0
size = width, height = 1500, 780
screen = pygame.display.set_mode((width, height))
image = pygame.image.load('images\\mickeyclock.jpeg')
image = pygame.transform.scale(image, (750, 750))
clock = pygame.time.Clock()

right_hand = pygame.image.load('images\\r.png')
right_hand.set_colorkey('black')

left_hand = pygame.image.load('images\\l.png')
left_hand.set_colorkey('black')

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key = lambda p: p[0])[0], min(box_rotate, key = lambda p: p[1])[1])
    max_box    = (max(box_rotate, key = lambda p: p[0])[0], max(box_rotate, key = lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image.set_colorkey(black)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

    # draw rectangle around the image
    pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()), 2)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)

w, h = image.get_size()
angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pygame.quit()
            sys.exit()
    pos = (screen.get_width() // 2, screen.get_height() // 2)
    screen.fill(white)
    screen.blit(image, (375, 15))
    blitRotate(screen, left_hand, pos, (w//4.7, h//5.3), -angle)
    #blitRotate2(screen, left_hand, pos, angle)
    blitRotate(screen, right_hand, pos, (w//4.7, h//5.3), -angle)
    #blitRotate(screen, left_hand, pos, (0, 0), -angle)
    #blitRotate(screen, right_hand, pos, (0, 0), -angle)
    angle += 1
    pygame.display.flip()
    clock.tick(60)