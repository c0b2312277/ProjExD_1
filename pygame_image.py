import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    # ゲームの初期化
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kt1_img=pg.image.load("fig/3.png")
    kt1_img=pg.transform.flip(kt1_img,True,False)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # screen.blit(bg_img, [0, 0]) # 背景画像の貼り付け(表示)
        x=tmr%800
        screen.blit(bg_img, [-x, 0]) # 背景画像の貼り付け(表示)
        kt1_rct = kt1_img.get_rect() # 画像の中心を抽出
        kt1_rct .center=300,200 # 中心を300,200に設定
        screen.blit(kt1_img,kt1_rct) # 画像の表示(kt1_rctの位置にする)

        pg.display.update()
        tmr += 1
                
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()