import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ProjExD2023/ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ProjExD2023/ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_list = []
    """
    ↓こうかとんのフレームごとの回転に関するリスト作成↓
    """
    for i in range(20):  
        ls = []
        if i < 11:
            kk_imgrtzm = pg.transform.rotozoom(kk_img, i, 1.0)
        else:
            kk_imgrtzm = pg.transform.rotozoom(kk_img, 20-i, 1.0)
        ls.append(kk_imgrtzm)
        kk_list += ls * 5

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kk_list[tmr%100], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()