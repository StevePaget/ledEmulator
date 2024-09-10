import pygame, random, sys
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

ledSize = 15
screen = pygame.display.set_mode([64*ledSize, 64*ledSize])

grid = [[ [0,0,0] for x in range(64)] for y in range(64)]
changes = []

def parseColour(colour):
    if type(colour) == str:
        # check to see if valid colour
        return pygame.Color(colour)
    else:
        colourRGB = pygame.Color("white")
        colourRGB.r = colour[0]
        colourRGB.g = colour[1]
        colourRGB.b = colour[2]
        return colourRGB
    
def drawGrid():
    for row in range(64):
        for col in range(64):
            thisrect = pygame.draw.rect(screen, parseColour(grid[row][col]),
                                         [row*ledSize, col*ledSize, ledSize, ledSize],0)
            changes.append(thisrect)

def drawPixel(row,col, colour):
    grid[row][col] = colour
    thisrect = pygame.draw.rect(screen, parseColour(colour),
                                         [row*ledSize, col*ledSize, ledSize, ledSize],0)
    changes.append(thisrect)

def refresh():
    global changes
    pygame.display.update(changes)
    changes = []

def endWait():
    print("Press ESC to quit")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                waiting = False
    pygame.quit()
    exit()

def tick(fps):
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(fps)
    return clock.get_fps()


