# Pygame bibliotekos importavimas
import pygame as pg
import sys  # Importuojamas modulis programos išėjimui valdyti
import re  # Importuojamas reguliariųjų išraiškų modulis

# Pygame bibliotekos inicializacija
pg.init()

# Ekrano informacija
info = pg.display.Info()
eplotis = info.current_w  # Ekrano plotis
eaukstis = info.current_h  # Ekrano aukštis

# Butonų paveikslų failų pavadinimai
buton = ['buton.png', 'butononmause.png']

# Butonų dydžiai (tuple: (plotis, aukštis))
bdydis = [(eplotis / 10, eaukstis / 8), (eplotis / 10 + 10, eaukstis / 8 + 10)]

# Pirmojo ir antrojo butonų paveikslai
pirmas = pg.image.load(buton[0])
antras = pg.image.load(buton[0])

# Kvadrato objektai, susieti su butonų paveikslais
pirmas_rect = pirmas.get_rect()
antras_rect = antras.get_rect()

# Pradinės koordinatės pirmajam ir antrajam butonui (x, y)
kordinate1 = [eaukstis / 6, eaukstis - 150]
kordinate2 = [eaukstis / 6, eaukstis - 150]

# Priskiriamos butonų pradinės pozicijos
pirmas_rect.x = kordinate1[0]
pirmas_rect.y = kordinate1[1]
antras_rect.x = kordinate2[0]
antras_rect.y = kordinate2[1]

# Pelytės paveikslo failo pavadinimas
pelyte = 'pelyte.png'

# Sukuriamas ekranas su nurodytais plotiu ir aukščiu
screen = pg.display.set_mode((eplotis, eaukstis))
pg.display.set_caption("D2AN")  # Ekrano pavadinimas

# Spalvų konstantos
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Failų pavadinimai, naudojami veikėjo komponentėms
veikejes = 'player_frame.png'
alertl = 'alertlangelis.png'

# Veikėjo komponentės
kunas = ['kunas.png']
kelnės = ['kelnės.png']
veidas = ['veidas.png']
maikė = ['maikė.png']

# Veikėjo paveikslas
veikejes = pg.image.load(veikejes)
veikejes_rect = veikejes.get_rect()

# Alerto langelio paveikslas
alertl = pg.image.load(alertl)
alertl = pg.transform.scale(alertl, (eplotis, eaukstis))

# Fono paveikslas
background_image = pg.image.load("backgraund.png").convert()
background_image = pg.transform.scale(background_image, (eplotis, eaukstis))

# Teksto šriftas
font = pg.font.Font(None, 40)
text = ""  # Pradžioje tekstas yra tuščias
movex = 'To move player in screen write: Player.x = Player.x + `number`; Or Player.x += `number`'

# Pygame garso sistemos inicializacija
pg.mixer.init()

# Permatomo kvadrato objektas
permatoma_spalva = pg.Surface(screen.get_size(), pg.SRCALPHA)
permatoma_spalva.fill((3, 3, 3, 200))

# Meniu muzikos garsas
menu_music = pg.mixer.Sound("Menu.mp3")
menu_music.set_volume(0.3)

# Žaidimo muzikos garsas
game_music = pg.mixer.Sound("Game.mp3")
game_music.set_volume(0.3)

# Kintamieji žaidimo mechanikai
vx = x = 0
numbers = ['0']
xskaicius = 0
tik = tiky = 0
k = km = 0
y = eaukstis - 500
yk = 0
yskaicius = 0
c = 0

# Pygame laikrodis
clock = pg.time.Clock()

# Alerto langelio būsena
alert = True

# Slėpti pelytės rodyklę
pg.mouse.set_visible(False)

# Pelytės paveikslas
pelyte = pg.image.load(pelyte)

# Būsena, ar kažką rodyti ekrane
show = False
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
                    yk = 1
            else:
                text += event.unicode  # Pridedame simbolį į teksto eilutę
            if event.key == pg.K_ESCAPE:
                text = text[:-1]
                if alert == True:
                    alert = False      
                else:
                    alert = True
            if event.key == pg.K_F1:
              
                if show == False:
                    show = True      
                else:
                    show = False
           
    screen.blit(background_image, (0,0))
    
    # cia tipo gravitacije ir taip taisykles kurios padaro jog is mepo neiseitu
    
    # screen.fill(WHITE)
    
    
    pel = pg.mouse.get_pos()
    if alert:
        
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
            y -= 2
        if y < eaukstis / 6:
            c = 1
        if c == 1:
            y += 2
            tiky = 0
            yk = 0 
            text = ''  
            if y > eaukstis / 3:
                c = 0 
    else:
        screen.blit(permatoma_spalva, (0, 0))
        screen.blit(alertl, (0,0))
        if event.type == pg.MOUSEBUTTONDOWN:    
            if antras_rect.collidepoint(pg.mouse.get_pos()):
                        pg.quit()
                        sys.exit()
        if antras_rect.collidepoint(pg.mouse.get_pos()):
            antras = pg.image.load(buton[1])
            screen.blit(pg.transform.scale(antras, bdydis[1]), kordinate2)
        else:
            antras = pg.image.load(buton[0])
            screen.blit(pg.transform.scale(antras, bdydis[0]), kordinate2)
          
                
    if show:        
        fps = str(int(clock.get_fps()))
        fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255), (0, 0, 0))
        x_text = font.render(f"Žaidėjo.x: {x}", True, (255, 255, 255), (0, 0, 0))
        y_text = font.render(f"Žaidėjo.y: {y}", True, (255, 255, 255), (0, 0, 0))
        eplotis_text = font.render(f"Eplotis: {eplotis}", True, (255, 255, 255), (0, 0, 0))
        eaukstis_text = font.render(f"Eaukštis: {eaukstis}", True, (255, 255, 255), (0, 0, 0))
        xskaicius_text = font.render(f"Liko nueiti: {xskaicius - tik}", True, (255, 255, 255), (0, 0, 0))
        screen.blit(fps_text, (10, 10))
        screen.blit(x_text, (10, 40))
        screen.blit(y_text, (10, 70))
        screen.blit(eplotis_text, (10, 100))
        screen.blit(eaukstis_text, (10, 130))
        screen.blit(xskaicius_text, (10, 160))
    clock.tick(60)
    screen.blit(pelyte, pel)
    pg.display.update()

# Quit Pygame
pg.quit()
sys.exit()
