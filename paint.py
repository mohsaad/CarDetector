""" paint.py 
    a simple paint program"""

import pygame
    
def checkKeys(myData):
    """test for various keyboard inputs"""
    
    #extract the data
    (event, background, drawColor, lineWidth, keepGoing) = myData
    #print myData
    
    if event.key == pygame.K_q:
        #quit    
        keepGoing = False
    elif event.key == pygame.K_c:
        #clear screen
        background.fill((255, 255, 255))
    elif event.key == pygame.K_s:
        #save picture
        pygame.image.save(background, "painting.bmp")
    elif event.key == pygame.K_l:
        #load picture
        background = pygame.image.load("painting.bmp")
    elif event.key == pygame.K_r:
        #red
        drawColor = (255, 0, 0)
    elif event.key == pygame.K_g:
        #green
        drawColor = (0, 255, 0)
    elif event.key == pygame.K_w:
        #white
        drawColor = (255, 255, 255)
    elif event.key == pygame.K_b:
        #blue
        drawColor = (0, 0, 255)
    elif event.key == pygame.K_k:
        #black
        drawColor = (0, 0, 0)

    #line widths
    elif event.key == pygame.K_1:
        lineWidth = 1
    elif event.key == pygame.K_2:
        lineWidth = 2
    elif event.key == pygame.K_3:
        lineWidth = 3
    elif event.key == pygame.K_4:
        lineWidth = 4
    elif event.key == pygame.K_5:
        lineWidth = 5
    elif event.key == pygame.K_6:
        lineWidth = 6
    elif event.key == pygame.K_7:
        lineWidth = 7
    elif event.key == pygame.K_8:
        lineWidth = 8
    elif event.key == pygame.K_9:
        lineWidth = 9

    #return all values 
    myData = (event, background, drawColor, lineWidth, keepGoing)
    return myData

def showStats(drawColor, lineWidth):
    """ shows the current statistics """
    myFont = pygame.font.SysFont("None", 20)
    stats = "color: %s, width: %d" % (drawColor, lineWidth)
    statSurf = myFont.render(stats, 1, (drawColor))
    return statSurf

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint:  (r)ed, (g)reen, (b)lue, (w)hite, blac(k), (1-9) width, (c)lear, (s)ave, (l)oad, (q)uit")
    
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3
    
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                myData = (event, background, drawColor, lineWidth, keepGoing)
                myData = checkKeys(myData)
                (event, background, drawColor, lineWidth, keepGoing) = myData
        screen.blit(background, (0, 0))
        myLabel = showStats(drawColor, lineWidth)
        screen.blit(myLabel, (450, 450))
        pygame.display.flip()

if __name__ == "__main__":
    main()