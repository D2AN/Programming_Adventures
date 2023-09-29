import pygame as pg
 
def main():
    pg.init()
    info = pg.display.Info()
    eplotis = info.current_w  # Ekrano plotis
    eaukstis = info.current_h  # Ekrano aukštis
    screen = pg.display.set_mode((eplotis, eaukstis))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(10, 10, 140, 32)
    input_box2 = pg.Rect(10, 50, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    color2 = color_inactive
    active = False
    active2 = False
    text = 0
    text2 = 0
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    active2 = False
                elif input_box2.collidepoint(event.pos):
                    active2 = not active2
                    active = False
                else:
                    active = False
                    active2 = False
                color = color_active if active else color_inactive
                color2 = color_active if active2 else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print("Pirmas laukas:", text)
                        text = 0
                    elif event.key == pg.K_BACKSPACE:
                        text = text // 10  # Naudojame //, kad padalintume skaičių iš 10 (panaikintume paskutinį skaitmenį)
                    else:
                        text = text * 10 + int(event.unicode)  # Konvertuojame naują skaitmenį į int() ir pridedame prie esamo skaičiaus
                if active2:
                    if event.key == pg.K_RETURN:
                        print("Antras laukas:", text2)
                        text2 = 0
                    elif event.key == pg.K_BACKSPACE:
                        text2 = text2 // 10  # Naudojame //, kad padalintume skaičių iš 10 (panaikintume paskutinį skaitmenį)
                    else:
                        text2 = text2 * 10 + int(event.unicode)  # Konvertuojame naują skaitmenį į int() ir pridedame prie esamo skaičiaus

        screen.fill((30, 30, 30))
        pg.draw.line(screen, pg.Color('white'), (300, 0), (300, 900), 2)

        txt_surface = font.render(str(text), True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pg.draw.rect(screen, color, input_box, 2)

        txt_surface2 = font.render(str(text2), True, color2)
        width2 = max(200, txt_surface2.get_width() + 10)
        input_box2.w = width2
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        pg.draw.rect(screen, color2, input_box2, 2)
        
        paveikslas_x = int(text)
        paveikslas_y = int(text2)

        paveikslas = pg.image.load('taip.png')
        screen.blit(paveikslas, (paveikslas_x, paveikslas_y))

        pg.display.flip()
        clock.tick(30)

    pg.quit()

if __name__ == '__main__':
    main()