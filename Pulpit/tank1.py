import pygame
import time
import random
import math

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Tanki')

firesound= pygame.mixer.Sound("fire.wav")
introsound= pygame.mixer.Sound("syrenaintro.wav")
boomsound= pygame.mixer.Sound("bomb.wav")
musicgame= pygame.mixer.Sound("podczas1.ogx")

yellow = (200,200,0)
yellow1 = (255,255,0)
white = (255,255,255)
black = (0,0,0)
red = (220,0,0)
red1 = (255, 10, 10)
green = (30,200,70)
green1 = (0, 255, 0)
orange= (255,165,0)
clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("arial", 25)
medfont = pygame.font.SysFont("arial", 50)
largefont = pygame.font.SysFont("arial", 85)

#img = pygame.image.load('snakehead.png')
#appleimg = pygame.image.load('apple.png')
tankimg = pygame.image.load('tank1.png').convert_alpha()
tankimg1=pygame.transform.scale(tankimg, (400, 300))
tankwidth=40
tankheight=20

def score(score):

    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])
    

def writescr(msg,color, y_displace = 0, size = "small"):

    if size == "small":
        text = smallfont.render(msg, True, color)
    if size == "medium":
        text = medfont.render(msg, True, color)
    if size == "large":
        text = largefont.render(msg, True, color)

    powierzchnia=text.get_rect()
    powierzchnia.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(text, powierzchnia)

def writebttn(msg,color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):

    if size == "small":
        text = smallfont.render(msg, True, color)
    if size == "medium":
        text = medfont.render(msg, True, color)
    if size == "large":
        text = largefont.render(msg, True, color)

    powierzchnia=text.get_rect()
    powierzchnia.center = (buttonx+(buttonwidth/2),buttony+(buttonheight/2))
    gameDisplay.blit(text, powierzchnia)

def pause():

    paused = True
    writescr("Pauza",black,-100,size="large")
    writescr("Nacisnij spację aby kontynuować i Q aby wyjść",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        

        clock.tick(60)


def game_intro():

    intro = True
    pygame.mixer.Sound.play(introsound)
    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        gameDisplay.blit(tankimg1, (200,200))
        writescr("TANKS",black,-180,size="large")
        writescr("Aby wygrać",black,-80)
        writescr("Musisz zniszczyć czołgi przeciwników!",black,-50)
        pygame.draw.rect(gameDisplay,green,(135,480,130,75))
        pygame.draw.rect(gameDisplay,green,(335,480,130,75))
        pygame.draw.rect(gameDisplay,red,(535,480,130,75))
        mousepos=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 135+130>mousepos[0]>135 and 480+75>mousepos[1]>485:
                    pygame.draw.rect(gameDisplay,green1,(135,480,130,75))
                    if click[0]==1:
                        gameLoop()
                        intro==False
        if 335+130>mousepos[0]>335 and 480+75>mousepos[1]>485:
                    pygame.draw.rect(gameDisplay,green1,(335,480,130,75))
                    if click[0]==1:
                        controls()
                        intro==False
        if 535+130>mousepos[0]>535 and 480+75>mousepos[1]>485:
                    pygame.draw.rect(gameDisplay,red1,(535,480,130,75))
                    if click[0]==1:
                        pygame.quit()
                        quit()
        writebttn("play",black,135,480,130,75)
        writebttn("controls",black,335,480,130,75)
        writebttn("quit",black,535,480,130,75)
        pygame.display.update()

        clock.tick(60)

def controls():

    controls = True

    while controls:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        writescr("STEROWANIE",black,-180,size="large")
        writescr("Poruszanie= strzalki lewo prawo",black,-80)
        writescr("Poruszanie lufą= strzałki góra dół", black, -110)
        writescr("Strzał= spacja",black,-50)
        writescr("Zmiana siły= A i D",black,0)
        pygame.draw.rect(gameDisplay,green,(135,480,130,75))
        pygame.draw.rect(gameDisplay,red,(535,480,130,75))
        mousepos=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 135+130>mousepos[0]>135 and 480+75>mousepos[1]>485:
                    pygame.draw.rect(gameDisplay,green1,(135,480,130,75))
                    if click[0]==1:
                        gameLoop()
                        controls==False
        if 535+130>mousepos[0]>535 and 480+75>mousepos[1]>485:
                    pygame.draw.rect(gameDisplay,red1,(535,480,130,75))
                    if click[0]==1:
                        pygame.quit()
                        quit()
        writebttn("play",black,135,480,130,75)
        writebttn("quit",black,535,480,130,75)
        pygame.display.update()

        clock.tick(60)

def tank(x,y,kat):
    kat_w_radianach=math.radians(kat)
    xturret=20*math.cos(kat_w_radianach)
    yturret=20*math.sin(kat_w_radianach)
    pygame.draw.circle(gameDisplay,black,(int(x),int(y)),int(tankheight/2))
    pygame.draw.rect(gameDisplay,black,(int(x-tankheight),int(y),tankwidth,tankheight))
    pygame.draw.line(gameDisplay,black,(int(x),int(y)),(int(x-xturret),int(y-yturret)),3)
    return (xturret,yturret,kat,x,y)

def tank2(x,y,kat):
    kat_w_radianach=math.radians(kat)
    xturret=-20*math.cos(kat_w_radianach)
    yturret=20*math.sin(kat_w_radianach)
    pygame.draw.circle(gameDisplay,black,(int(x),int(y)),int(tankheight/2))
    pygame.draw.rect(gameDisplay,black,(int(x-tankheight),int(y),tankwidth,tankheight))
    pygame.draw.line(gameDisplay,black,(int(x),int(y)),(int(x-xturret),int(y-yturret)),3)
    return (xturret,yturret,kat,x,y)

def wall(wallx, wall_height,wall_width):
    pygame.draw.rect(gameDisplay,black,(wallx,display_height*0.7-wall_height+tankheight,wall_width,wall_height))

def boom(x, y, wallx, wallh):

    boom1 = True

    while boom1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colors = [red, red1, yellow, yellow1]

        i = 1

        while i < 50:

            boomx = x +random.randrange(-1*i,i)
            boomy = y -random.randrange(-1*i,i)

            pygame.draw.circle(gameDisplay, colors[random.randrange(0,4)], (boomx,boomy),random.randrange(1,5))
            i += 1

            pygame.display.update()
            clock.tick(200)

        boom1 = False

def lifechange(life):
    life[0]-=10

def fire(dane,sila,wallx,wallh,currentplayer,life1,life2,enemytankx,enemytanky):
    pygame.mixer.Sound.play(firesound)
    fire=True
    pygame.draw.rect(gameDisplay,green,(0,display_height*0.7+20,display_width,display_height*0.3))
    pygame.draw.rect(gameDisplay,black,(wallx,display_height*0.7-wallh+20,30,wallh))
    currenttankx=dane[3]
    currenttanky=dane[4]
    baza=(-1*dane[0]+currenttankx,-1*dane[1]+currenttanky,dane[2])
    starting_location=list(baza)
    power=2
    nachylenie=baza[2]/10

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, (int(starting_location[0]),int(starting_location[1])),5)
        
        starting_location[0] -= (9 - nachylenie)*2
        if (9-nachylenie)*2==0:
            starting_location[1] += int((((starting_location[0]-baza[0])*0.019/(sila/50))**2)-(nachylenie+nachylenie/(10-nachylenie+0.01)))
        else:
            starting_location[1] += int((((starting_location[0]-baza[0])*0.019/(sila/50))**2)-(nachylenie+nachylenie/(10-nachylenie)))
       
        print(starting_location[0],starting_location[1])
        print(enemytankx,enemytanky)

        if starting_location[1]>display_height*0.7+20:

            bulletx = int(starting_location[0]*(display_height*0.7+20)/starting_location[1])
            bullety = int(display_height*0.7+20)

            if enemytankx + 20 > bulletx > enemytankx - 20:
                lifechange(life2)
                print(life1,life2)
                print(starting_location[0],starting_location[1])
            boom(bulletx,bullety,wallx,wallh)
            fire = False

        if starting_location[0] <= wallx + 30 and starting_location[0] >= wallx and starting_location[1] <= display_height*0.7 and starting_location[1] >= display_height*0.7 - wallh:
          
            bulletx = int(starting_location[0])
            bullety = int(starting_location[1])

            boom(bulletx,bullety,wallx,wallh)
            fire = False
        pygame.display.update()
        clock.tick(60)

def fire2(dane,sila,wallx,wallh,currentplayer,life1,life2,enemytankx,enemytanky):
    pygame.mixer.Sound.play(firesound)
    fire=True
    pygame.draw.rect(gameDisplay,green,(0,display_height*0.7+20,display_width,display_height*0.3))
    pygame.draw.rect(gameDisplay,black,(wallx,display_height*0.7-wallh+20,30,wallh))    
    currenttankx=dane[3]
    currenttanky=dane[4]
    baza=(-1*dane[0]+currenttankx,-1*dane[1]+currenttanky,dane[2])
    starting_location=list(baza)
    power=2
    nachylenie=baza[2]/10
    print(enemytankx,enemytanky)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, (int(starting_location[0]),int(starting_location[1])),5)

        starting_location[0] += (9 - nachylenie)*2
        if (9-nachylenie)*2==0:
            starting_location[1] += int((((starting_location[0]-baza[0])*0.019/(sila/50))**2)-(nachylenie+nachylenie/(10-nachylenie+0.01)))
        else:
            starting_location[1] += int((((starting_location[0]-baza[0])*0.019/(sila/50))**2)-(nachylenie+nachylenie/(10-nachylenie)))
        print(starting_location[0],starting_location[1])
        print(enemytankx,enemytanky)
        #print(starting_location[0],starting_location[1])
        if starting_location[1]>display_height*0.7+20:

            bulletx = int(starting_location[0]*(display_height*0.7+20)/starting_location[1])
            bullety = int(display_height*0.7+20)
            boom(bulletx,bullety,wallx,wallh)
            fire = False
        if starting_location[0]<=enemytankx+40 and starting_location[0]>=enemytankx and starting_location[1]>=display_height*0.7:

            bulletx = int(starting_location[0])
            bullety = int(starting_location[1])
            boom(bulletx,bullety,wallx,wallh)
            lifechange(life1)
            print(life1,life2)

            fire = False
        if starting_location[0] <= wallx + 30 and starting_location[0] >= wallx and starting_location[1] <= display_height*0.7 and starting_location[1] >= display_height*0.7 - wallh:
          
            bulletx = int(starting_location[0])
            bullety = int(starting_location[1])

            boom(bulletx,bullety,wallx,wallh)
            fire = False
        
        pygame.display.update()
        clock.tick(60)

def power(sila):
    text=smallfont.render("Siła: "+str(sila)+"%",True, black)
    gameDisplay.blit(text,[(display_width/2)-55,0])

def life(zycie1,zycie2):
    zycie1teraz=zycie1[0]/100
    zycie2teraz=zycie2[0]/100
    if zycie1teraz>0.75:
        color1=green
    if zycie1teraz<0.75:
        color1=yellow
    if zycie1teraz<0.5:
        color1=orange
    if zycie1teraz<0.33:
        color1=red
    if zycie2teraz>0.75:
        color2=green
    if zycie2teraz<0.75:
        color2=yellow
    if zycie2teraz<0.5:
        color2=orange
    if zycie2teraz<0.33:
        color2=red
    pygame.draw.rect(gameDisplay,color1,(int(display_width*0.7-75),5,260*zycie1teraz,20))
    pygame.draw.rect(gameDisplay,color2,(int(display_width*0.3-185),5,260*zycie2teraz,20))

def gameLoop():
    pygame.mixer.fadeout(1000)
    pygame.mixer.Sound.play(musicgame)
    gameExit = False
    gameOver = False
    FPS = 60
    tank1x=display_width*0.9
    tank1y=display_height*0.7
    tank2x=display_width*0.1
    tank2y=display_height*0.7
    alfa=45
    alfa2=45
    alfachange=0
    tankchange=0
    wallx=display_width/2+random.randint(-0.3*display_width-30,0.3*display_width)
    wall_height=random.randint(display_height*0.1,display_height*0.6)
    wall_width=30
    firepower=50
    firepower2=50
    powerchange=0
    currentplayer=2
    zycie1=[1]
    zycie2=[1]
    zycie1[0]=100
    zycie2[0]=100
    while not gameExit:
        gameDisplay.fill(white)
        if currentplayer==1:
            alfa+=alfachange
            tank1x+=tankchange
        if currentplayer==2:
            alfa2+=alfachange
            tank2x+=tankchange
        turret_pos=tank(tank1x,tank1y,alfa)
        turret_pos2=tank2(tank2x,tank2y,alfa2)
        firepower+=powerchange
        if firepower<1:
            firepower=1
        if firepower>100:
            firepower=100
        if alfa<0:
            alfa=0
        if alfa>90:
            alfa=90
        if firepower2<1:
            firepower2=1
        if firepower2>100:
            firepower2=100
        if alfa2<0:
            alfa2=0
        if alfa2>90:
            alfa2=90
        if currentplayer==2:
            power(firepower2)
        if currentplayer==1:
            power(firepower)
        if currentplayer==2:
            firepower2+=powerchange
        if currentplayer==1:
            firepower+=powerchange
        life(zycie1,zycie2)
        if gameOver == True:
            #gameDisplay.fill(white)
            writescr("Game Over!!",red,-50,size="large")
            writescr("Naciśnij spację aby zagrać ponownie",black,50)
            writescr("Lub Q aby wyjsc",black,75)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            gameLoop()
                        elif event.key == pygame.K_q:
                            
                            gameExit = True
                            gameOver = False
         


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankchange=-1
                    
                elif event.key == pygame.K_RIGHT:
                    tankchange=1
                    
                elif event.key == pygame.K_UP:
                    alfachange=1

                elif event.key == pygame.K_DOWN:
                    alfachange=-1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    if currentplayer==1:
                        fire(turret_pos, firepower,wallx, wall_height, currentplayer,zycie1,zycie2,tank2x,tank2y)
                        pygame.mixer.Sound.play(boomsound)
                        currentplayer=2
                    elif currentplayer==2:
                        fire2(turret_pos2, firepower2,wallx, wall_height, currentplayer,zycie1,zycie2,tank1x,tank1y)
                        pygame.mixer.Sound.play(boomsound)
                        currentplayer=1
                elif event.key == pygame.K_a:
                        powerchange-=1

                elif event.key == pygame.K_d:
                        powerchange+=1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankchange=0
                    
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    alfachange=0

                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    powerchange=0
                    print(tank1x,tank1y)
                    print(zycie1,zycie2)

                elif event.key == pygame.K_p:
                    pause()

                    

        wall(wallx, wall_height,wall_width)
        pygame.draw.rect(gameDisplay,green,(0,display_height*0.7+tankheight,display_width,display_height*0.3))
        if tank1x-tankwidth/2<wallx+wall_width:
            tank1x+=1
        if tank2x+tankwidth/2>wallx:
            tank2x-=1
        if(zycie1[0]<10 or zycie2[0]<10):
            gameOver=True

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
