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
    bg_flip_img=pg.transform.flip(bg_img,True,False) # 背景の左右反転
    kt1_img=pg.image.load("fig/3.png")
    kt1_img=pg.transform.flip(kt1_img,True,False)
    kt1_rct = kt1_img.get_rect() # 画像の中心を抽出
    kt1_rct .center=300,200 # 中心を300,200に設定

    move_ud=0
    move_rl=0
    speed=1

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # screen.blit(bg_img, [0, 0]) # 背景画像の貼り付け(表示)
        x=tmr%3200
        # x2=tmr%1600
        screen.blit(bg_img, [-x, 0]) # 背景画像の貼り付け(表示)
        screen.blit(bg_flip_img,[-x+1600,0])
        screen.blit(bg_img, [-x+3200, 0]) # 背景画像の貼り付け(表示)
        screen.blit(bg_flip_img,[-x+4800,0])
        
        # 練習問題
        # key_lst = pg.key.get_pressed() # キーの押下状態を取得
        # if key_lst[pg.K_UP]:
        #     kt1_rct.move_ip((0,-1))
        # if key_lst[pg.K_DOWN]:
        #     kt1_rct.move_ip((0,1))
        # if key_lst[pg.K_RIGHT]:
        #     kt1_rct.move_ip((1,0))
        # if key_lst[pg.K_LEFT]:
        #     kt1_rct.move_ip((-1,0))

        # 演習課題1
        # key_lst=pg.key.get_pressed() # 全てのキーの押下状態の取得
        # if key_lst[pg.K_UP]:
        #     kt1_rct.move_ip((0,-1))
        # if key_lst[pg.K_DOWN]:
        #     kt1_rct.move_ip((0,1))
        # if key_lst[pg.K_RIGHT]:
        #     kt1_rct.move_ip((2,0))
        # if key_lst[pg.K_LEFT]:
        #     kt1_rct.move_ip((-2,0))
        # else:
        #     kt1_rct.move_ip((-1,0))


        # 演習課題2
        key_lst=pg.key.get_pressed() # 全てのキーの押下状態の取得
        move_px=(-1,0)
        if (key_lst[pg.K_UP]==True)and(key_lst[pg.K_RIGHT]==True):
            move_px=(speed*2,-1)
        elif (key_lst[pg.K_DOWN]==True)and(key_lst[pg.K_RIGHT]==True):
            move_px=(speed*2,1)
        elif key_lst[pg.K_UP]:
            move_px=(-speed,-speed)           
        elif key_lst[pg.K_DOWN]:
            move_px=(-speed,speed)
        elif key_lst[pg.K_RIGHT]:
            move_px=(speed*2,0)
        elif key_lst[pg.K_LEFT]:
            move_px=(-speed*2,0)

        kt1_rct.move_ip(move_px)           

        screen.blit(kt1_img,kt1_rct) # 画像の表示(kt1_rctの位置にする)

        pg.display.update()
        tmr += 1
                
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()