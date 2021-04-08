import pygame
from introduction_files.pygame_guidance.agents import Human, Robot
# TODO: Debug following direction for human

pygame.init()
gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

infoObject = pygame.display.Info()
display_height = infoObject.current_h
display_width = infoObject.current_w

pygame.display.set_caption('Guiding task')
clock = pygame.time.Clock()
background = pygame.image.load("images/environment/floor.PNG")
furnitures = pygame.image.load("images/environment/furnitures2.PNG")
# Resize image
bgsize = background.get_rect().size
resizeFactor = 4
background = pygame.transform.scale(background, (int(bgsize[0]/resizeFactor), int(bgsize[1]/resizeFactor)))

#### Colours
black = (0,0,0)
grey = (200, 200, 200)
white = (255,255,255)
red = (255,0,0)

running = True

human1 = Human('grey_man_bold1', 100, 100)
#human2 = Human(100, 200)
pepper = Robot(700, 700)

notice_distance = 400

X = 1.0
Y = 0.0
theta = -1

def drawGameWindow():
    gameDisplay.fill(grey)
    drawBackGround(background, display_height, display_width)
    pygame.draw.rect(gameDisplay, black, [10, 10, display_width - 20, display_height - 20], width=10)
    # Draw environment
    drawEnvironment(furnitures, 300, 300)
    # Draw characters
    human1.update(gameDisplay)
    #human2.update(gameDisplay)
    pepper.update(gameDisplay)

    pygame.display.update()

def drawEnvironment(image, x, y):
    gameDisplay.blit(image, (x, y))

def drawBackGround(image, h, w):
    imagesize = image.get_rect().size                      # Get image size
    for x in range(0, w, imagesize[0]):
        for y in range(0, h, imagesize[1]):
            gameDisplay.blit(image, (x,y))

def checkQuit(event):
    if event.type == pygame.QUIT:
        return False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:return False
    return True

def getMovementEvents(event):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT: pepper.turnLeft = True
        if event.key == pygame.K_RIGHT: pepper.turnRight = True
        if event.key == pygame.K_UP: pepper.moveForward = True
        if event.key == pygame.K_DOWN: pepper.moveBackward = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT: pepper.turnLeft = False
        if event.key == pygame.K_RIGHT: pepper.turnRight = False
        if event.key == pygame.K_UP: pepper.moveForward = False
        if event.key == pygame.K_DOWN: pepper.moveBackward = False

def getDistance(o1, o2):
    return ((o1.x-o2.x)**2 + (o1.y-o2.y)**2)**0.5

def setBoudary():
    pass
    # TODO: Set the boundaty of objects

################################################ M A I N    L O O P ##################################################
while running:
    # Draw the elements
    drawGameWindow()

    for event in pygame.event.get():
        # Looking for quit conditions
        running = checkQuit(event)
        # Checking for movement
        getMovementEvents(event)

    # Following strategy

    if getDistance(pepper, human1) < notice_distance: human1.follow(pepper)
    #if getDistance(pepper, human2) < notice_distance: human2.follow(pepper)
    #human1.follow(pepper)
    #
    human1.move()
    #human2.move()
    pepper.move()

    clock.tick(60)

pygame.quit()
quit()