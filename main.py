import pygame
import random
from pygame import mixer
import asyncio

async def main():
    pygame.init()

    screen = pygame.display.set_mode((600,720))
    pygame.display.set_caption('Rapid Roll')

    mixer.music.load('assets/sounds/bgmusic.ogg')

    #line1
    line1X=300
    line1Y=600
    #line2
    line2X=100
    line2Y=750
    #line3 red line
    line3X=500
    line3Y=850
    border_wire = pygame.image.load('assets/images/borderWire.png')
    #line4
    line4X=480
    line4Y=1100

    #line5 red line
    line5X=50
    line5Y=1050

    def lineXY(x,y):
        pygame.draw.line(screen,(0,0,0),(x,y),(x+100,y),10)

    def line_redXY(x,y):
        pygame.draw.line(screen,(255,0,0),(x,y),(x+100,y),10) #red line
        screen.blit(border_wire,(x,y-7))


    #line_Ychnge
    line_Ychange= 4 #change
    man_xChange = 4 #change
    man_yChange = 4 #change

    rMan = [pygame.image.load(f'assets/images/rman{i}.png') for i in range(9)]
    lMan = [pygame.image.load(f'assets/images/lman-{i}.png') for i in range(9)]

    player_right = True
    player_left = False
    player_count =0
    player_stop = False
    player_run = True
    player_X = 250
    player_Y = 10
    player_Xchange = 0

    def playerXY(x,y,player_right,player_left,player_count):
        frame = int((player_count // 50) % 9)  # cycles 0–8
        if player_right:
            screen.blit(rMan[frame], (x, y))
        if player_left:
            screen.blit(lMan[frame], (x, y))

    #health_lost_variable
    healthLost = 0
    health_value = 3
    healthIcon = pygame.image.load('assets/images/heart.png')
    def healthXY(x,y):
        screen.blit(healthIcon,(x,y))
    healthBrkIcn = pygame.image.load('assets/images/broken-heart.png')
    def healthBrkXY(x,y):
        screen.blit(healthBrkIcn,(x,y))

    h_incrseX = line4X
    h_incrseY = line4Y-24
    def h_incrseXY(x,y):
        screen.blit(healthIcon,(x,y))
    #health_incrse_variable
    hiconHIDE = 0

    #gameover
    loopStop = False
    loopON =0
    gameStart = False
    if gameStart == False: #game start and game intro sound
        gmStartS = mixer.Sound('assets/sounds/rapidintroS.ogg')
        gmStartS.play(-1)

    gameOver = False
    gm0vrSon =0
    gfont=pygame.font.SysFont('freesansbold.ttf',128)
    def gm_overXY(x,y):
        gm=gfont.render('GAME OVER',True,(0,155,0))
        screen.blit(gm,(x,y))

    num_cnt = 0
    def goXY(x,y,num_cnt):
        if 1<=num_cnt<=200:
            num3 = gfont.render('3', True, (255, 0, 0))
            screen.blit(num3,(x,y))
        if 201 <= num_cnt <= 400:
            num2 = gfont.render('2', True, (200, 0, 0))
            screen.blit(num2, (x, y))
        if 401 <= num_cnt <= 600:
            num1 = gfont.render('1', True, (155, 0, 0))
            screen.blit(num1, (x, y))
        if 601 <= num_cnt <= 800:
            go = gfont.render('GO', True, (0, 200, 0))
            screen.blit(go, (x, y))

    #score
    score_value = 0
    sfont = pygame.font.SysFont('freesansbold.ttf',40)
    def scoreXY(x,y):
        score=sfont.render('SCORE:'+str(score_value),True,(0,100,0))
        screen.blit(score,(x,y))

    # user interface
    gameStart_0 = False
    button_start = pygame.Rect(200, 620, 200, 80)
    button_pad = pygame.Rect(0, 600, 600, 120)  # x,y,w,h
    button_left = pygame.Rect(20, 620, 100, 90)
    button_right = pygame.Rect(480, 620, 100, 90)
    button_continue = pygame.Rect(200, 620, 200, 80)

    font_btn= pygame.font.SysFont('freesansbold.ttf', 32)

    def draw_start_button():
        pygame.draw.rect(screen, (10, 200, 10), button_start, border_radius=20)
        text = font_btn.render("START", True, (0, 0, 0))
        screen.blit(text, (button_start.x + 50, button_start.y + 30))
    def draw_button_pad():
        pygame.draw.rect(screen, (200, 150, 200), button_pad)
    def draw_buttons():
        pygame.draw.rect(screen, (100, 100, 100), button_left, border_radius= 20)
        text = font_btn.render("<<", True, (0, 0, 0))
        screen.blit(text, (button_left.x + 30, button_left.y + 30))

        pygame.draw.rect(screen, (100, 100, 100), button_right, border_radius=20)
        text = font_btn.render(">>", True, (0, 0, 0))
        screen.blit(text, (button_right.x + 30, button_right.y + 30))

    def draw_continue_button():
        pygame.draw.rect(screen, (250, 100, 10), button_start, border_radius=30)
        text = font_btn.render("Continue", True, (0, 0, 0))
        screen.blit(text, (button_continue.x + 50, button_continue.y + 30))

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player_run = True
                if event.key == pygame.K_RIGHT :
                    player_Xchange =man_xChange
                    player_left = False
                    player_right = True
                if event.key == pygame.K_LEFT :
                    player_Xchange = -man_xChange
                    player_right = False
                    player_left = True
                if event.key == pygame.K_SPACE and gameOver == True:
                    gameOver = False
                    gameStart = False
                    health_value=4
                    score_value = 0
                    gm0vrSon=0
                    gmStartS.play(-1)
                if event.key == pygame.K_DOWN:
                    gameStart = True
                    gmStartS.stop()
                    mixer.music.play(-1)
                    mixer.music.set_volume(0.5)
            if event.type == pygame.KEYUP:
                player_Xchange = 0
                player_run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                player_run = True
                if button_start.collidepoint(event.pos):
                    gameStart_0 = True
                if button_right.collidepoint(event.pos):
                    player_Xchange = man_xChange
                    player_left = False
                    player_right = True
                if button_left.collidepoint(event.pos):
                    player_Xchange = -man_xChange
                    player_right = False
                    player_left = True
                if button_continue.collidepoint(event.pos) and gameOver == True:
                    gameOver = False
                    gameStart = False
                    health_value = 4
                    score_value = 0
                    gm0vrSon = 0
                    gmStartS.play(-1)
                    line1Y = 600
                    line2Y = 750
                    line3Y = 850
                    line4Y = 1100
                    line5Y = 1050
                    player_Y = 10
                    loopON = 0
            if event.type == pygame.MOUSEBUTTONUP:
                player_Xchange = 0
                player_run = False

        if loopStop == False and gameOver== False and gameStart == True:
            line1Y-=line_Ychange
            if line1Y<=-20:
                line1Y =610
                line1X = 300+random.randrange(0,100,10)
                score_value+=2
            line2Y -= line_Ychange
            if line2Y <= -20:
                line2Y = 610
                line2X = 100+random.randrange(0,100,10)
                score_value += 2
            line3Y -= line_Ychange
            if line3Y <= -20:
                line3Y = 610
                line3X = 400 - random.randrange(0, 200, 10)
                score_value += 5
            line4Y -= line_Ychange
            h_incrseY = line4Y - 24 # health_icon
            if line4Y <= -20:
                line4Y = 610
                line4X = 480 - random.randrange(0, 200, 10)
                # health_icon
                h_incrseX = line4X+random.randrange(0,80,5)
                hiconHIDE = 0
                score_value += 2
            line5Y -= line_Ychange
            if line5Y <= -20:
                line5Y = 610
                line5X = 50 + random.randrange(0, 100, 10)
                score_value += 5

            # player
            player_X += player_Xchange
            if player_X <= 1:
                player_X = 1
            if player_X >= 567:
                player_X = 567
            if player_stop == False:
                player_count += 0.5
                if player_count >= 435:
                    player_count = 0
            if player_run == True:
                player_count += 1
                if player_count >= 435:
                    player_count = 0

            if player_stop == False:
                player_Y += man_yChange

            if player_Y >= 610:
                healthLost = 2
                player_X = 250
                player_Y = 10
            if player_Y <= -10:
                healthLost = 2
                player_Y = 10  # ballRenew

            if line1X - 50 <= player_X <= line1X + 100 and line1Y - 34 <= player_Y <= line1Y - 26:  # line1
                player_Y = line1Y - 32
                player_stop = True
            elif line2X - 50 <= player_X <= line2X + 100 and line2Y - 34 <= player_Y <= line2Y - 26:  # line2
                player_Y = line2Y - 32
                player_stop = True
            elif line3X - 50 <= player_X <= line3X + 100 and line3Y - 34 <= player_Y <= line3Y - 26:  # line3red
                loopStop = True
                hlostS = mixer.Sound('assets/sounds/blmusic.ogg')
                hlostS.play()
            elif line4X - 50 <= player_X <= line4X + 100 and line4Y - 34 <= player_Y <= line4Y - 26:  # line4
                player_Y = line4Y - 32
                player_stop = True
                if h_incrseX - 50 <= player_X <= h_incrseX + 20 and hiconHIDE == 0:  # increase_health_value
                    health_value += 1
                    hincreS = mixer.Sound('assets/sounds/coinS.ogg')
                    hincreS.play()
                    if health_value >= 3:
                        health_value = 3
                    hiconHIDE = 2  # hideHeart
            elif line5X - 50 <= player_X <= line5X + 100 and line5Y - 32 <= player_Y <= line5Y - 28:  # line5red
                loopStop = True
                hlostS = mixer.Sound('assets/sounds/blmusic.ogg')
                hlostS.play()
            else:
                player_stop = False

        # loopstopline

        if healthLost == 2:
            health_value -= 1  # health_value and gameover for drop and up
            hlostS=mixer.Sound('assets/sounds/blmusic.ogg')
            hlostS.play()
            healthLost = 0
        if health_value <= 0:
            gameOver = True

        #loopstop_line and gameover
        if loopStop == True:
            loopON+=10
            if loopON>=500:
                loopStop = False
                healthLost=2
                if healthLost == 2:
                    health_value -= 1  # health_value and gameover for red line
                    healthLost = 0
                if health_value <= 0:
                    gameOver = True
                if gameOver == False:
                    line1Y = 600
                    line2Y = 750
                    line3Y = 850
                    line4Y = 1100
                    line5Y = 1050
                    player_Y = 10
                    loopON = 0

        if hiconHIDE == 0:
            h_incrseXY(h_incrseX,h_incrseY)
        lineXY(line1X, line1Y)
        lineXY(line2X, line2Y)
        line_redXY(line3X, line3Y)
        lineXY(line4X, line4Y)
        line_redXY(line5X, line5Y)
        if player_run== True and gameStart == True:
            player_count +=10
            if player_count >=450:
                player_count = 0
        if gameStart == True:
            playerXY(player_X,player_Y-28,player_right,player_left,player_count)

        if 2<health_value<=4:
            healthXY(5,10)
            healthXY(29, 10)
            healthXY(53, 10)
        elif 1<health_value<=2:
            healthXY(5,10)
            healthXY(29, 10)
            healthBrkXY(53,10)
        elif 0<health_value<=1:
            healthXY(5,10)
            healthBrkXY(29, 10)
            healthBrkXY(53, 10)
        else:
            healthBrkXY(5, 10)
            healthBrkXY(29, 10)
            healthBrkXY(53, 10)

        if gameOver == True:
            gm_overXY(20,200)
            healthBrkXY(5, 10)
            healthBrkXY(29, 10)
            healthBrkXY(53, 10)
            mixer.music.stop()
            if gm0vrSon==0:
                goverS=mixer.Sound('assets/sounds/game-over.ogg')
                goverS.play()
                gm0vrSon=2

        if gameStart == False and gameStart_0 == True:
            num_cnt += 5
            goXY(250,200,num_cnt)
            if num_cnt >= 800:
                gameStart = True
                gmStartS.stop()
                mixer.music.play(-1)
                mixer.music.set_volume(0.5)

        scoreXY(430,10)
        screen.blit(border_wire,(0,0))
        screen.blit(border_wire, (500, 0))
        screen.blit(border_wire, (100, 0))
        screen.blit(border_wire, (200, 0))
        screen.blit(border_wire, (300, 0))
        screen.blit(border_wire, (400, 0))

        draw_button_pad()
        if gameStart_0 == False:
            draw_start_button()
        if gameStart_0 == True and gameOver == False:
            draw_buttons()
        if gameOver == True:
            draw_continue_button()

        clock.tick(60) #change
        pygame.display.flip()
        await asyncio.sleep(0)

# This is the program entry point
asyncio.run(main())

