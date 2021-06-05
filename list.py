import pgzrun
width=534
height=534
score=0
game_over=False
mario=Actor('mario')
mario.pos=100,200
coin=Actor('coin')
coin.pos=300,300
def draw():
    screen.blit('backgroud',(0,0))
    mario.draw()
    coin.draw()

pgzrun.go()