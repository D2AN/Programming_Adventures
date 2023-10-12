import pygame, sys, os
# Initialize Pygame
pygame.init()
screen_info = pygame.display.Info()
eaukstis = screen_info.current_h
eplotis = screen_info.current_w

# Set up the display
screen = pygame.display.set_mode((eplotis, eaukstis))
pygame.display.set_caption("Pradžia")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to run when a button is pressed
def run_game(game_file):
    os.system(f"python {game_file}")
textdydis = 50
font = pygame.font.Font(None, 0)  # specify font and size

# Main text
# ///////////////////////////////////////////////////////////
puse = eplotis / 2
main_text = font.render("Programing adventures", True, BLACK)
main_text_rect = main_text.get_rect()
main_text_x = puse - puse / 2
main_text_y = 50
main_text_rect.topleft = (main_text_x, main_text_y)

aukstis = eplotis / 5
# Button texts
# ////////////////////////////////////////////////
kordinate1 = [puse - eaukstis / 6, eaukstis - aukstis - 150 ]
kordinate2 = [puse - eaukstis / 6, eaukstis - aukstis - aukstis / 2 + 30 - 150 ]
kordinate3 = [puse - eaukstis / 6, eaukstis - aukstis - aukstis + 60 - 150 ]
išeiti = [puse - eaukstis / 6, eaukstis - eaukstis / 6 - 40 - 150]
migtukas = [puse + puse / 6, eaukstis - eaukstis / 4 ]
# ///////////////////////////////////////////////
buton = ['buton.png','butononmause.png']
pelyte = 'pelyte.png'
bdydis = [(aukstis ,eaukstis / 8),(aukstis + 10,eaukstis / 8 +10)]
pirmas = pygame.image.load(buton[0])
antras = pygame.image.load(buton[0])
trecias = pygame.image.load(buton[0])
iseiti = pygame.image.load(buton[0])
migtukas = pygame.image.load(buton[0])
migtukas_rect = migtukas.get_rect()
iseiti_rect = iseiti.get_rect()
pirmas_rect = pirmas.get_rect()
antras_rect = antras.get_rect()
trecias_rect = trecias.get_rect()


pirmas_rect.x = kordinate1[0]
pirmas_rect.y = kordinate1[1]
antras_rect.x = kordinate2[0]
antras_rect.y = kordinate2[1]
trecias_rect.x = kordinate3[0]
trecias_rect.y = kordinate3[1]
iseiti_rect.x = išeiti[0]
iseiti_rect.y = išeiti[1]
iseiti_rect.size = trecias_rect.size = antras_rect.size = pirmas_rect.size = bdydis[0]
# ///////////////////////////////////////////////
button_font = pygame.font.Font(None, 40)
button1_text = button_font.render("Learnig", True, BLACK)
button1_rect = button1_text.get_rect()

button1_rect.topleft = (kordinate1[0] +kordinate1[0] / 7  , kordinate1[1] + kordinate1[1]/14 )
button2_text = button_font.render("Tests", True, BLACK)
button2_rect = button2_text.get_rect()

button2_rect.topleft = (kordinate2[0] +kordinate2[0] / 7  , kordinate2[1] + kordinate2[1]/10 )
button3_text = button_font.render("Play", True, BLACK)
button3_rect = button3_text.get_rect()

button3_rect.topleft = (kordinate3[0] +kordinate3[0] / 7  , kordinate3[1] + kordinate3[1]/6)
galas = pygame.image.load('menu_1.png')
galas = pygame.transform.scale(galas,(eplotis,eaukstis))
pygame.mouse.set_visible(False)

pelyte = pygame.image.load(pelyte)
# pelyte.center = pel
with open('varibles.txt', 'r') as file:
    if file.read() == '':
        mony = 0
        with open('varibles.txt', 'w') as file:
            file.write(str(mony))            
    else:
        with open('varibles.txt', 'r') as file:
            mony = int(file.read())
  
 

# ////////////////////////////////////////////////////////////////
# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the left mouse button is pressed
            if event.button == 1:
                x, y = event.pos

                # Check which button the user pressed and run the corresponding file
                if pirmas_rect.collidepoint(pygame.mouse.get_pos()):
                    run_game("bandomasis.py")
                if antras_rect.collidepoint(pygame.mouse.get_pos()):
                    run_game("paint.py")
                if trecias_rect.collidepoint(pygame.mouse.get_pos()):
                    run_game("game.py")
                if iseiti_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
    # Draw the screen
   
    screen.blit(galas,(0,0))
    if pirmas_rect.collidepoint(pygame.mouse.get_pos()):
       pirmas = pygame.image.load(buton[1])
       screen.blit(pygame.transform.scale(pirmas, bdydis[1]), kordinate1)
    else:
        pirmas = pygame.image.load(buton[0])
        screen.blit(pygame.transform.scale(pirmas, bdydis[0]), kordinate1)
    if antras_rect.collidepoint(pygame.mouse.get_pos()):
       antras = pygame.image.load(buton[1])
       screen.blit(pygame.transform.scale(antras, bdydis[1]), kordinate2)
    else:
        antras = pygame.image.load(buton[0])
        screen.blit(pygame.transform.scale(antras, bdydis[0]), kordinate2)
    if trecias_rect.collidepoint(pygame.mouse.get_pos()):
       trecias = pygame.image.load(buton[1])
       screen.blit(pygame.transform.scale(trecias, bdydis[1]), kordinate3)
       mony = 1 + mony 
    else:
        trecias = pygame.image.load(buton[0])
        screen.blit(pygame.transform.scale(trecias, bdydis[0]), kordinate3)
    if iseiti_rect.collidepoint(pygame.mouse.get_pos()):
       iseiti = pygame.image.load(buton[1])
       screen.blit(pygame.transform.scale(iseiti, bdydis[1]), išeiti)
    else:
        iseiti = pygame.image.load(buton[0])
        screen.blit(pygame.transform.scale(iseiti, bdydis[0]), išeiti)

    mony_text = button_font.render(str(mony), True, BLACK)
    mony_rect = mony_text.get_rect()
    # uzrasai
    # screen.blit(main_text, main_text_rect)
    screen.blit(button1_text, button1_rect)
    screen.blit(button2_text, button2_rect)
    screen.blit(button3_text, button3_rect)
    screen.blit(mony_text, mony_rect)
    pel = pygame.mouse.get_pos()
    screen.blit(pelyte, pel)
    with open('varibles.txt', 'w') as file:
        file.write(str(mony)) 
    with open('varibles.txt', 'r') as file:
        mony = int(file.read())
   
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()