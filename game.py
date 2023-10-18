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
maikes = 'm'
# Butonų dydžiai (tuple: (plotis, aukštis))
bdydis = [(eplotis / 10 + 50, eaukstis / 8), (eplotis / 10 + 60, eaukstis / 8 + 10)]

# Pirmojo ir antrojo butonų paveikslai
pirmas = pg.image.load(buton[0])
antras = pg.image.load(buton[0])
game = False
# Kvadrato objektai, susieti su butonų paveikslais
pirmas_rect = pirmas.get_rect()
antras_rect = antras.get_rect()
antras_rect.size = pirmas_rect.size = bdydis[0]
# Pradinės koordinatės pirmajam ir antrajam butonui (x, y)
kordinate1 = [eplotis / 1.5, eaukstis / 1.3]
kordinate2 = [eplotis / 6, eaukstis / 1.3]
aukstis = eplotis / 5
km1 = [eplotis / 2 - (eplotis / 10 + 50) / 2, eaukstis - aukstis - aukstis + 60 - 150]
km2 = [eplotis / 2 - (eplotis / 10 + 50) / 2, eaukstis - aukstis - aukstis / 2 + 30 - 150]
km3 = [eplotis / 2 - (eplotis / 10 + 50) / 2, eaukstis - aukstis - 150]
km4 = [eplotis / 2 - (eplotis / 10 + 50) / 2, eaukstis - eaukstis / 6 - 40 - 150]

# Priskiriamos butonų pradinės pozicijos
pirmas_rect.x = kordinate1[0]
pirmas_rect.y = kordinate1[1]
antras_rect.x = kordinate2[0]
antras_rect.y = kordinate2[1]
m1 = pg.image.load(buton[0])
m2 = pg.image.load(buton[0])
m3 = pg.image.load(buton[0])
m4 = pg.image.load(buton[0])
m1_rect = m1.get_rect()
m2_rect = m2.get_rect()
m3_rect = m3.get_rect()
m4_rect = m4.get_rect()
m1_rect.x = km1[0]
m1_rect.y = km1[1]
m2_rect.x = km2[0]
m2_rect.y = km2[1]
m3_rect.x = km3[0]
m3_rect.y = km3[1]
m4_rect.x = km4[0]
m4_rect.y = km4[1]
# Pelytės paveikslo failo pavadinimas
pelyte = 'pelyte.png'

# Sukuriamas ekranas su nurodytais plotiu ir aukščiu
screen = pg.display.set_mode((eplotis, eaukstis))
pg.display.set_caption("Programing adventures")  # Ekrano pavadinimas

# Spalvų konstantos
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Failų pavadinimai, naudojami veikėjo komponentėms
veikejes = 'Bapkes.png'
siena = 'Siena.png'
alertl = 'alertlangelis.png'
galas = pg.image.load('menu_1.png')
galas = pg.transform.scale(galas,(eplotis,eaukstis))
# Veikėjo komponentės
kunas = ['kunas.png']
kelnės = ['kelnės.png']
veidas = ['veidas.png']
maikė = ['maikė.png']

# Veikėjo paveikslas
veikejes = pg.image.load(veikejes)
siena = pg.image.load(siena)



# Alerto langelio paveikslas
alertl = pg.image.load(alertl)
alertl = pg.transform.scale(alertl, (eplotis / 1.46 , eaukstis / 1.38))

# Fono paveikslas
background_image = pg.image.load("backgraund.png").convert()
background_image = pg.transform.scale(background_image, (eplotis, eaukstis))

# Teksto šriftas
font = pg.font.Font(None, 40)
text = ""  # Pradžioje tekstas yra tuščias
movex = 'To move player in screen write: Player.x += `number`'
moveb = 'To move back in screen write: Player.x -= `number`'
jump = 'To jump write: jump()'
close = 'Exit'
closea = 'Close'
moveb_blit = font.render(moveb, True, BLACK)
movex_blit = font.render(movex, True, BLACK)
jump_blit = font.render(jump, True, BLACK)
close_blit = font.render(close, True, BLACK)
closea_blit = font.render(closea, True, BLACK)
logo = pg.image.load('logo.png')
logo = pg.transform.scale(logo,(eplotis,eaukstis))
# Pygame garso sistemos inicializacija
pg.mixer.init()

# Permatomo kvadrato objektas
permatoma_spalva = pg.Surface(screen.get_size(), pg.SRCALPHA)
permatoma_spalva.fill((3, 3, 3, 200))

# Meniu muzikos garsas
# menu_music = pg.mixer.Sound("Menu.mp3")
# menu_music.set_volume(0.3)

# # Žaidimo muzikos garsas
# game_music = pg.mixer.Sound("Game.mp3")
# game_music.set_volume(0.3)

# Kintamieji žaidimo mechanikai
vx = x = 80
numbers = ['0']
xskaicius = 0
tik = tiky = 0
k = ks = 0
y = eaukstis - 500
yk = 0
yskaicius = 0
c = 0
loading = 0
# Pygame laikrodis
clock = pg.time.Clock()
shop = False
# Alerto langelio būsena
alert = True
meniu = True
# Slėpti pelytės rodyklę
pg.mouse.set_visible(False)
button_font = pg.font.Font(None, 40)
play_text = button_font.render("Play", True, BLACK)
shop_text = button_font.render("Shop", True, BLACK)
setings_text = button_font.render("Setings", True, BLACK)
exit_text = button_font.render("Exit", True, BLACK)
# Pelytės paveikslas
pelyte = pg.image.load(pelyte)
with open('level.txt', 'r') as file:
    if file.read() == '':
        lvl = 0
        with open('level.txt', 'w') as file:
            file.write(str(lvl))            
    else:
        with open('level.txt', 'r') as file:
            lvl = int(file.read())
with open('varibles.txt', 'r') as file:
    if file.read() == '':
        mony = 0
        with open('varibles.txt', 'w') as file:
            file.write(str(mony))            
    else:
        with open('varibles.txt', 'r') as file:
            mony = int(file.read())
# Būsena, ar kažką rodyti ekrane
meni = True
g = 3
show = False
running = True
def separateNumbersText(text):          
    numbers = re.findall(r'\d+', text)
    Playerx = re.sub(r'\d+', '', text)
    return numbers, Playerx.strip()
while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_SPACE:  # Jei paspaudžiama backspace, ištriname paskutinį simbolį
                loading = 1000000
            if event.key == pg.K_BACKSPACE:  # Jei paspaudžiama backspace, ištriname paskutinį simbolį
                text = text[:-1]
            elif event.key == pg.K_RETURN:  # Jei paspaudžiama enter, galite apdoroti įvestį arba ją atvaizduoti
                
                numbers, Playerv = separateNumbersText(text)
                if 'numbers' in locals() and len(numbers) > 0:
                    xskaicius = int(numbers[0])
                if Playerv == 'Player.x = Player.x +' or Playerv == 'Player.x +=' or Playerv == 'Player.x =  + Player.x':
                    if tik < xskaicius:
                       k = 1
                if Playerv == 'Player.x = Player.x -' or Playerv == 'Player.x -=' or Playerv == 'Player.x =  - Player.x' or Playerv == 'Player.x += -':
                    if tik < xskaicius:
                       ks = 1
                
                if Playerv == 'jump()':
                    yk = 1
                text = ''     
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
            
    # cia tipo gravitacije ir taip taisykles kurios padaro jog is mepo neiseitu

    pel = pg.mouse.get_pos()
    if meniu:
        if loading  < eplotis / 1.2:
            loading += 3
            screen.blit(logo,(0,0))
            pg.draw.rect(screen, (255,0,0), pg.Rect(30, eaukstis - 100, int(loading), 50))
            vx = x = 80
            y = eaukstis - 500 

        elif meni:   
            screen.blit(galas,(0,0))
            if m1_rect.collidepoint(pg.mouse.get_pos()):
                m1 = pg.image.load(buton[1])
                screen.blit(pg.transform.scale(m1, bdydis[1]), km1)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if m1_rect.collidepoint(pg.mouse.get_pos()):
                            loading = 0
                            meniu = False
                            game = True
            else:
                m1 = pg.image.load(buton[0])
                screen.blit(pg.transform.scale(m1, bdydis[0]), km1)
            if m2_rect.collidepoint(pg.mouse.get_pos()):
                m2 = pg.image.load(buton[1])
                screen.blit(pg.transform.scale(m2, bdydis[1]), km2)
                if event.type == pg.MOUSEBUTTONDOWN:
                
                    if event.button == 1:
                        x, y = event.pos
                        if m2_rect.collidepoint(pg.mouse.get_pos()):
                            Shop = True
                            meni = False
            else:
                m2 = pg.image.load(buton[0])
                screen.blit(pg.transform.scale(m2, bdydis[0]), km2)
            if m3_rect.collidepoint(pg.mouse.get_pos()):
                m3 = pg.image.load(buton[1])
                screen.blit(pg.transform.scale(m3, bdydis[1]), km3)
                if event.type == pg.MOUSEBUTTONDOWN:
                
                    if event.button == 1:
                        x, y = event.pos
                        if m3_rect.collidepoint(pg.mouse.get_pos()):
                            print('trecias')
            else:
                m3 = pg.image.load(buton[0])
                screen.blit(pg.transform.scale(m3, bdydis[0]), km3)
            if m4_rect.collidepoint(pg.mouse.get_pos()):
                m4 = pg.image.load(buton[1])
                screen.blit(pg.transform.scale(m4, bdydis[1]), km4)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if m4_rect.collidepoint(pg.mouse.get_pos()):
                            pg.quit()
                            sys.exit()
            else:
                m4 = pg.image.load(buton[0])
                screen.blit(pg.transform.scale(m4, bdydis[0]), km4)
            screen.blit(play_text, (km1[0] + 50,km1[1] + 30))
            screen.blit(shop_text, (km2[0] + 50,km2[1] + 30))
            screen.blit(setings_text, (km3[0] + 50,km3[1] + 30))
            screen.blit(exit_text, (km4[0] + 50,km4[1] + 30))
        elif shop:
            show = True
        
    else:
        if loading  < eplotis / 1.2:
            loading += 3
            screen.blit(logo,(0,0))
            pg.draw.rect(screen, (255,0,0), pg.Rect(30, eaukstis - 100, int(loading), 50))
            vx = x = 80
            y = eaukstis - 500
        else:
            screen.blit(background_image, (0,0))
            if alert:
                
                kunas1 = pg.image.load(kunas[0])
                kelnės1 = pg.image.load(kelnės[0])
                maikė1 = pg.image.load(maikė[0])
                veidas1 = pg.image.load(veidas[0])
                veikejes_rect = veikejes.get_rect()
                veikejes_rect.x, veikejes_rect.y = (900, eaukstis / 1.88)

                kunas_rect = kunas1.get_rect()
                kunas_rect.x, kunas_rect.y = x,y
                text_blit = font.render(text, True,(0, 0, 0), (255,255,255))
                text_surface = font.render(text, True, (255,255,255),(0, 0, 0))
                screen.blit(text_blit, (eplotis / 3, 100))  # Sukuriame tekstą
                screen.blit(veikejes, (900, eaukstis / 1.88))
                screen.blit(kunas1, (x,y))
                screen.blit(kelnės1, (x,y))
                red_maike = maikė1.copy()
                red_maike.fill((0, 30, 30), None, pg.BLEND_ADD)
                screen.blit(red_maike, (x,y))
                screen.blit(veidas1, (x,y))        
                siena1_rect = siena_rect = siena.get_rect()
                
                if lvl == 0:
                    if veikejes_rect.colliderect(kunas_rect):
                        x = 80
                        tik = 0
                        xskaicius = 0
                        mony += 1
                        lvl += 1
            
                elif lvl == 1:
                    
                    siena_rect.x, siena_rect.y = (400, eaukstis / 3)
                    screen.blit(siena, (400, eaukstis / 3))     
                    if siena_rect.colliderect(kunas_rect):
                        x -= 3
                    if veikejes_rect.colliderect(kunas_rect):
                        x = 80
                        tik = 0
                        xskaicius = 0
                        mony += 1
                        lvl += 1
                elif lvl == 2:
                    siena1_rect.x, siena1_rect.y = (800, eaukstis / 1.7)
                    screen.blit(siena, (800, eaukstis / 1.7)) 
                    siena_rect.x, siena_rect.y = (0, eaukstis / 3)  
                    screen.blit(siena, (0, eaukstis / 3))   
                    if siena_rect.colliderect(kunas_rect):
                        x += 6 
                    if siena1_rect.colliderect(kunas_rect):
                        x -= 3   
                
                    
                
                    if veikejes_rect.colliderect(kunas_rect):
                        x = 80
                        tik = 0
                        xskaicius = 0
                        mony += 1
                        lvl += 1            
                if x > eplotis - 200:
                    x = 0
                if x < -10:
                    x = eplotis - 201
                if k == 1:
                    tik += 3
                    x += 2
                    if tik > xskaicius:
                        xskaicius = 0
                        tik = 0
                        k = 0 
                        text = ''

                if ks == 1:
                    tik += 1
                    x -= 3
                    if tik > xskaicius:
                        xskaicius = 0
                        tik = 0
                        ks = 0 
                    
                if yk == 1:
                    tiky -= 1
                    y -= 2
                if y < eaukstis / 6:
                    c = 1
                if c == 1:
                    y += 2
                    tiky = 0
                    yk = 0 
                    
                    if y > eaukstis / 3:  
                        c = 0 
                with open('level.txt', 'w') as file:
                    file.write(str(lvl))          
                with open('varibles.txt', 'w') as file:
                    file.write(str(mony)) 
                screen.blit(veikejes, (eplotis - 130, 0))  
                mony_text = font.render(str(mony), True, BLACK)
                screen.blit(mony_text, (eplotis - 100, 25))      
            else:
                screen.blit(permatoma_spalva, (0, 0))
                screen.blit(alertl, (eplotis / 7  , eaukstis / 7))
                if event.type == pg.MOUSEBUTTONDOWN:    
                    if antras_rect.collidepoint(pg.mouse.get_pos()):
                        loading = 0
                        meniu = True
                    if pirmas_rect.collidepoint(pg.mouse.get_pos()):
                        alert = True
                if pirmas_rect.collidepoint(pg.mouse.get_pos()):
                    pirmas = pg.image.load(buton[1])
                    screen.blit(pg.transform.scale(pirmas, bdydis[1]), kordinate1)
                else:
                    pirmas = pg.image.load(buton[0])
                    screen.blit(pg.transform.scale(pirmas, bdydis[0]), kordinate1)
                if antras_rect.collidepoint(pg.mouse.get_pos()):
                    antras = pg.image.load(buton[1])
                    screen.blit(pg.transform.scale(antras, bdydis[1]), kordinate2)
                else:
                    antras = pg.image.load(buton[0])
                    screen.blit(pg.transform.scale(antras, bdydis[0]), kordinate2)
                screen.blit(jump_blit, (300, 300))  
                screen.blit(movex_blit, (300, 200))
                screen.blit(moveb_blit, (300, 250))
                screen.blit(close_blit, (kordinate2[0] + 50 ,  kordinate2[1] + 40))  
                screen.blit(closea_blit, (kordinate1[0] + 50 ,  kordinate1[1] + 40)) 
         
                
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
        clock.tick(100)
    
    screen.blit(pelyte, pel)
    pg.display.update()

# Quit Pygame
pg.quit()
sys.exit()
