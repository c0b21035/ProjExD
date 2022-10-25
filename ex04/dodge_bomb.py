import pygame as pg
import sys
import random
import time

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) # Surface
    screen_rct = screen_sfc.get_rect() #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #Surface
    bgimg_rct = bgimg_sfc.get_rect()  #Rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)




    kkimg_sfc = pg.image.load("fig/6.png") #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect() #Rect
    kkimg_rct.center = 900,400

    #練習5
    bmimg_sfc = pg.Surface((20, 20)) #Surface
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc, (255,0,0), (10,10), 10)
    bmimg_rct = bmimg_sfc.get_rect() #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)

    bmimg2_sfc = pg.Surface((20, 20)) #Surface
    bmimg2_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg2_sfc, (0,255,0), (10,10), 10)
    bmimg2_rct = bmimg2_sfc.get_rect() #Rect
    bmimg2_rct.centerx = random.randint(0, screen_rct.width)
    bmimg2_rct.centery = random.randint(0, screen_rct.height)

    bmimg3_sfc = pg.Surface((20, 20)) #Surface
    bmimg3_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg3_sfc, (0,0,255), (10,10), 10)
    bmimg3_rct = bmimg3_sfc.get_rect() #Rect
    bmimg3_rct.centerx = random.randint(0, screen_rct.width)
    bmimg3_rct.centery = random.randint(0, screen_rct.height)
    
    vx, vy = +1, +1 #練習6
    vx2, vy2 = +1.5, +1.5
    vx3, vy3 = +2, +2



    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        #練習２
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #練習４
        key_states = pg.key.get_pressed() #辞書
        if key_states[pg.K_UP] == True: #y座標を-1
            kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True: #y座標を+1
            kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True: #x座標を-1
            kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: #x座標を+1
            kkimg_rct.centerx += 1
        #練習7    
        if check_bound(kkimg_rct, screen_rct) != (1, 1): #領域外だったら
            if key_states[pg.K_UP] == True: 
                kkimg_rct.centery += 1
            if key_states[pg.K_DOWN] == True: 
                kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT] == True: 
                kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True:
                kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)


        #練習6
        bmimg_rct.move_ip(vx,vy)
        bmimg2_rct.move_ip(vx2,vy2)
        bmimg3_rct.move_ip(vx3,vy3)
        #練習5
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        screen_sfc.blit(bmimg2_sfc,bmimg2_rct)
        screen_sfc.blit(bmimg3_sfc,bmimg3_rct)
        #練習7
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate  

        yoko2, tate2 = check_bound(bmimg2_rct, screen_rct)
        vx2 *= yoko2
        vy2 *= tate2

        yoko3, tate3 = check_bound(bmimg3_rct, screen_rct)
        vx3 *= yoko3
        vy3 *= tate3
        
        #練習8
        if kkimg_rct.colliderect(bmimg_rct) == True:
            bakuimg_sfc = pg.image.load("fig/bakuha.gif") #爆発エフェクト
            bakuimg_sfc.set_colorkey((255,255,255))  #周りの色を透過
           # bakuimg_sfc = pg.transform.rotozoom(finimg_sfc, 0, )
            bakuimg_rct = bakuimg_sfc.get_rect() # Rect
            bakuimg_rct.center = kkimg_rct.center
            screen_sfc.blit(bakuimg_sfc,bakuimg_rct) #Surface
            pg.display.update()  #画像の更新
            pg.time.wait(100)    #待機時間
            finimg_sfc = pg.image.load("fig/fin.png") #Surface
            #finimg_sfc.set_colorkey((0,0,0))
            finimg_sfc = pg.transform.rotozoom(finimg_sfc, 0, 1.5) #倍率変更
            finimg_rct = finimg_sfc.get_rect()
            
            finimg_rct.center = kkimg_rct.center  
            screen_sfc.blit(finimg_sfc,finimg_rct)
            #pg.Surface.blit("fig/images.jpg",)
            
            pg.display.update()    #画像の更新
            pg.time.wait(1300)   #待機時間

            return 
        
        if kkimg_rct.colliderect(bmimg2_rct) == True:
            bakuimg_sfc = pg.image.load("fig/bakuha.gif") #爆発エフェクト
            bakuimg_sfc.set_colorkey((255,255,255))  #周りの色を透過
           # bakuimg_sfc = pg.transform.rotozoom(finimg_sfc, 0, )
            bakuimg_rct = bakuimg_sfc.get_rect() # Rect
            bakuimg_rct.center = kkimg_rct.center
            screen_sfc.blit(bakuimg_sfc,bakuimg_rct) #Surface
            pg.display.update()  #画像の更新
            pg.time.wait(100)    #待機時間
            finimg_sfc = pg.image.load("fig/fin.png") #Surface
            #finimg_sfc.set_colorkey((0,0,0))
            finimg_sfc = pg.transform.rotozoom(finimg_sfc, 0, 1.5) #倍率変更
            finimg_rct = finimg_sfc.get_rect()
            
            finimg_rct.center = kkimg_rct.center  
            screen_sfc.blit(finimg_sfc,finimg_rct)
            #pg.Surface.blit("fig/images.jpg",)
            
            pg.display.update()    #画像の更新
            pg.time.wait(1300)   #待機時間
            return

        if kkimg_rct.colliderect(bmimg3_rct) == True:
            bakuimg_sfc = pg.image.load("fig/bakuha.gif") #爆発エフェクト
            bakuimg_sfc.set_colorkey((255,255,255))  #周りの色を透過
           # bakuimg_sfc = pg.transform.rotozoom(finimg_sfc, 0, )
            bakuimg_rct = bakuimg_sfc.get_rect() # Rect
            bakuimg_rct.center = kkimg_rct.center
            screen_sfc.blit(bakuimg_sfc,bakuimg_rct) #Surface
            pg.display.update()  #画像の更新
            pg.time.wait(100)    #待機時間
            finimg_sfc = pg.image.load("fig/fin.png") #Surface
            #finimg_sfc.set_colorkey((0,0,0))
            finimg_sfc = pg.transform.rotozoom(finimg_sfc, 0, 1.5) #倍率変更
            finimg_rct = finimg_sfc.get_rect()
            
            finimg_rct.center = kkimg_rct.center  
            screen_sfc.blit(finimg_sfc,finimg_rct)
            #pg.Surface.blit("fig/images.jpg",)
        
            pg.display.update()    #画像の更新
            pg.time.wait(1300)   #待機時間
            return

        pg.display.update()
        clock.tick(1000)

#練習7
def check_bound(rct, scr_rct):
    """
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    """
    yoko, tate = +1, +1 #領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right: #ダメ
        yoko = -1 #領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: #ダメ
        tate = -1 #領域外
    return yoko, tate




if __name__ == "__main__":
    clock2 = pg.time.Clock()
    pg.init()
    main()
    pg.quit()
    sys.exit()