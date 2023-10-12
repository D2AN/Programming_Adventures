from turtle import Screen
import pygame as pg
import sys
import re
import time
# Initialize Pygame
pg.init()

# Constants
info = pg.display.Info()
eplotis = info.current_w  # Ekrano plotis
eaukstis = info.current_h  # Ekrano aukštis

pelyte = 'pelyte.png'
# Create the screen
screen = pg.display.set_mode((eplotis, eaukstis))
pg.display.set_caption("D2AN")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
veikejes = 'player_frame.png'
alertl = 'alertlangelis.png'
alertl = pg.image.load(alertl)
kunas = ['kunas.png']
kelnės = ['kelnės.png']
veidas = ['veidas.png']
maikė = ['maikė.png']

veikejes = pg.image.load(veikejes)
veikejes_rect = veikejes.get_rect()
alertl = pg.transform.scale(alertl, (eplotis, eaukstis))
# Load background image
background_image = pg.image.load("backgraund.png").convert()
background_image = pg.transform.scale(background_image, (eplotis, eaukstis))
font = pg.font.Font(None, 40)
text = ""  # Pradžioje teksto eilutė yra tuščia
movex = 'To move player in screan write: Player.x = Player.x + `number`; Or Player.x += `number`'
# Initialize mixer
pg.mixer.init()
permatoma_spalva = pg.Surface(screen.get_size(), pg.SRCALPHA)
permatoma_spalva.fill((3, 3, 3, 200))


    
# Load menu music
menu_music = pg.mixer.Sound("Menu.mp3")
menu_music.set_volume(0.3)
tips = 0
# Load game music
game_music = pg.mixer.Sound("Game.mp3")
game_music.set_volume(0.3)
vx =x = 0
numbers = ['0']
xskaicius = 0
tik = tiky = 0
k = km = 0
y = eaukstis - 500
yk = 0
yskaicius = 0
c = 0
alert = False
pg.mouse.set_visible(False)
pelyte = pg.image.load(pelyte)
# Begalinis ciklas
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:  # Jei paspaudžiama backspace, ištriname paskutinį simbolį
                text = text[:-1]
            elif event.key == pg.K_RETURN:  # Jei paspaudžiama enter, galite apdoroti įvestį arba ją atvaizduoti
                def separateNumbersText(text):
                    
                    numbers = re.findall(r'\d+', text)
                    Playerx = re.sub(r'\d+', '', text)
                    return numbers, Playerx.strip()
                numbers, Playerv = separateNumbersText(text)
                if 'numbers' in locals() and len(numbers) > 0:
                    xskaicius = int(numbers[0])
                if Playerv == 'Player.x = Player.x +' or Playerv == 'Player.x +=' or Playerv == 'Player.x =  + Player.x':
                    if tik < xskaicius:
                       xskaicius = int(numbers[0])
                       k = 1
                if Playerv == 'Player.x = Player.x -' or Playerv == 'Player.x -=' or Playerv == 'Player.x =  - Player.x':
                    if tik < xskaicius:
                       xskaicius = int(numbers[0])
                       km = 1
                
                if Playerv == 'jump()':
                    alert = True
                    yk = 1
                    
                
            else:
                text += event.unicode  # Pridedame simbolį į teksto eilutę
    screen.blit(background_image, (0,0))
    # cia tipo gravitacije ir taip taisykles kurios padaro jog is mepo neiseitu
    if x > eplotis:
         x = 0
    if k == 1:
        tik += 1
        x += 1
        if tik == xskaicius:
            xskaicius = 0
            tik = 0
            k = 0 
            text = ''

    if km == 1:
        tik += 1
        x -= 1
        if tik == xskaicius:
            xskaicius = 0
            tik = 0
            km = 0 
            text = ''
    if yk == 1:
        tiky -= 1
        y -= 1
    if y < eaukstis - 800:
        c = 1
    if c == 1:
        y += 2
        tiky = 0
        yk = 0 
        text = ''  
        if y > eaukstis - 500:
            c = 0 
    # screen.fill(WHITE)
    kunas1 = pg.image.load(kunas[0])
    kelnės1 = pg.image.load(kelnės[0])
    maikė1 = pg.image.load(maikė[0])
    veidas1 = pg.image.load(veidas[0])
    movex_blit = font.render(movex, True, BLACK)
    text_blit = font.render(text, True, BLACK)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_blit, (0, 100))  # Sukuriame tekstą
    # screen.blit(movex_blit, (100, 200))
    screen.blit(kunas1, (x,y))
    screen.blit(kelnės1, (x,y))
    red_maike = maikė1.copy()
    red_maike.fill((0, 30, 30), None, pg.BLEND_ADD)
    screen.blit(red_maike, (x,y))
    screen.blit(veidas1, (x,y))
    
    pel = pg.mouse.get_pos()
    if alert == True:
        screen.blit(permatoma_spalva, (0, 0))
        screen.blit(alertl, (0,0))
    screen.blit(pelyte, pel)
    pg.display.update()

# Quit Pygame
pg.quit()
sys.exit()
