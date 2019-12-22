import pygame

def button(msg, rect, inactiveColor, activeColor):
    mouse = pygame.mouse.get_pos()

    if rect.x + rect.width > mouse[0] > rect.x and rect.y + rect.height > mouse[1] > rect.y:
        pygame.draw.rect(screen, activeColor, rect)
    else:
        pygame.draw.rect(screen, inactiveColor, rect)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((rect.x + (rect.width / 2)), (rect.y + (rect.height / 2)))
    screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


pygame.display.set_caption("P25 Scanner")
pygame.display.set_icon(pygame.image.load('antenna-large.png'))
# screen = pygame.display.set_mode((900, 600))
# size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
size = (900, 600)
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.init()
black = (0, 0, 0)
grey = (125, 125, 125)
white = (255, 255, 255)

red = (255, 0, 0)
lightred = (128, 0, 0)
green = (0, 255, 0)
lightgreen = (0, 128, 0)
blue = (0, 0, 255)
lightblue = (0, 0, 128)


i = 0
screen.fill(black)

#button("Enable", 100, 100, 200, 50, red, grey)
#button("Disable", 100, 200, 200, 50, green, grey)
pygame.display.update()


# Loop
running = True
while running:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
            # pygame.quit()
            # quit()

    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects("Frequency", largeText)
    TextRect.center = ((size[0] / 2), (size[1] / 2))
    screen.blit(TextSurf, TextRect)
    i = i + 10
    #pygame.draw.rect(screen, grey, (150, i, 100, 50))
    #pygame.draw.rect(screen, grey, (550, 450, 100, 50))
    #button("Disable", 100, 200, 200, i, green, grey)

    e = pygame.Rect(100, 100, 200, 50)
    button("Enable", e, lightred, red)

    d = e.copy()
    d.x = 300
    button("Disable", d, lightgreen, green)

    # background = pygame.Surface(size)
    # screen.blit(background, (0, 0))
    # screen.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(15)
