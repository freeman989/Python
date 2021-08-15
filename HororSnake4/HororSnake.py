import pygame
import os
from random import randint
import time
from ctypes import POINTER, WINFUNCTYPE, windll
from ctypes.wintypes import BOOL, HWND, RECT
##
## Variables
# Constants:
WIDTH = 1356
HEIGHT = 690
FPS = 100
COL = 24
ROW = 24
##XSIZE = 21
##YSIZE = 20
XSIZE = int(((WIDTH / 2) / COL))## + (((WIDTH / 2) / COL) / 100) * 1
YSIZE = int(HEIGHT / ROW)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (30,30,30)
VIOLET = (40,0,200)
DARK = (15,15,15)

# Variables:
running = True
stop_game = False
x = randint(0,ROW-1)
y = randint(0,COL-1)
ex = 0
ey = 0
d = ''
count = 0
start = 0
sleep = 0
time_sleep = 20
sleep_sw = 0
sw = 0
px = [x]
py = [y]
min_size = 1
max_size = 1
speed = 1
speed_sw = 0
score = 0
mx = 0
my = 0
mcl = False
snd = 0

sound_path = "C:\\Users\\Freeman.Autobot\\Desktop\\PythonExamples\\testHororSnake2\\sounds\\"

# Создаем игру и окно
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (5,30)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
icon = pygame.image.load("C:\\Users\\Freeman.Autobot\\Desktop\\PythonExamples\\HororSnake4\\python_icon.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Horor Snake")
clock = pygame.time.Clock()

hwnd = pygame.display.get_wm_info()["window"]
prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
paramflags = (1, "hwnd"), (2, "lprect")
GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)
rect = GetWindowRect(hwnd)
    #print ("top, left, bottom, right: ", rect.top, rect.left, rect.bottom, rect.right)

### Functions
def playing_field():
    for i in range(COL):
        for j in range(ROW):
            pygame.draw.rect(screen, GRAY, ((XSIZE*i)+3,(YSIZE*j)+3, XSIZE-6, YSIZE-6),1)
    for i in range(COL):
        pygame.draw.line(screen, GRAY,[0-1,(i*YSIZE)-1], [(XSIZE*COL)-1,(i*YSIZE)-1],1)    
    for i in range(ROW):
        pygame.draw.line(screen, GRAY,[(i*XSIZE)-0,0-0], [(i*XSIZE)-0,(YSIZE*COL)-0],1)   
def frame_field():
    pygame.draw.rect(screen, WHITE, (0,0, XSIZE*COL, YSIZE*ROW),2)

def frame_info(canvas,point_x,point_y,size_x,size_y,color=WHITE):
    pygame.draw.rect(canvas, color, (point_x,point_y,size_x,size_y),1)

def screen_fill(canvas,point_x,point_y,size_x,size_y,color=BLACK):
    pygame.draw.rect(canvas, color, (point_x,point_y,size_x,size_y))

def player(canvas,point_x,point_y,color=BLUE):
    pygame.draw.rect(canvas, color, ((point_x*XSIZE)+3,(point_y*YSIZE)+3, XSIZE-6, YSIZE-6))
    if color == BLUE:
        pygame.draw.rect(canvas, color, ((point_x*XSIZE)+1,(point_y*YSIZE)+1, XSIZE-2, YSIZE-2),1)
        pygame.draw.rect(canvas, BLACK, ((point_x*XSIZE)+3,(point_y*YSIZE)+3, XSIZE-6, YSIZE-6),1)
    elif color == VIOLET:
        pygame.draw.rect(canvas, color, (point_x*XSIZE,point_y*YSIZE, XSIZE, YSIZE),1)
        pygame.draw.rect(canvas, BLACK, ((point_x*XSIZE)+1,(point_y*YSIZE)+1, XSIZE-2, YSIZE-2),1)
        
def enemy(canvas,point_x,point_y,color=RED):
    pygame.draw.rect(canvas, color, ((point_x*XSIZE)+4,(point_y*YSIZE)+3, XSIZE-6, YSIZE-6))
    pygame.draw.rect(canvas, color, ((point_x*XSIZE)+1,point_y*YSIZE, XSIZE, YSIZE),1)

def text(sc, txt, x, y, size = 50,color = (200, 000, 000), font_type = None):
    txt = str(txt)
    font_type_2 = 'tahoma.ttf'
    font = pygame.font.Font(font_type, size)
    txt = font.render(txt, True, color)
    sc.blit(txt, (x, y))

class buttons():
    def __init__(self,button_color = BLACK,button_sleep = 5):
        self.button_color = button_color
        self.button_sleep = button_sleep
        self.sound_dir = pygame.mixer.Sound(sound_path+"dirrection.wav")
        self.sound_pause = pygame.mixer.Sound(sound_path+"pause.wav")
        self.sound_start = pygame.mixer.Sound(sound_path+"start_game.wav")
        self.sound_stop = pygame.mixer.Sound(sound_path+"game_over.wav")
        self.sound_sound = pygame.mixer.Sound(sound_path+"pause.wav")
        self.sound_on = pygame.mixer.Sound(sound_path+"sound_on.wav")
        self.sound_off = pygame.mixer.Sound(sound_path+"sound_off.wav")
        self.sn = 0
        self.sg = False
        
    def button(self,canvas,point_x,point_y,size_x,size_y,frame=3,txt = '',txt_indent_x = 6,txt_indent_y = 12,color=WHITE,mouse_x=mx,mouse_y=my,mouse_click=mcl):

        self.button_color = color
        global d
        
        if mouse_x > point_x and mouse_x < point_x+size_x and mouse_y > point_y and mouse_y < point_y+size_y :
##            print("Mouse X: ", mouse_x)
##            print("Mouse Y: ", mouse_y)
            self.button_color = (150,150,150)
        
        if mouse_click == True and mouse_x > point_x and mouse_x < point_x+size_x and mouse_y > point_y and mouse_y < point_y+size_y :
            print("Нажата кнопка "+ str(txt))
            if txt == 'UP':
                self.sound_dir.play()
                d = 'UP'
            if txt == 'DOWN':
                self.sound_dir.play()
                d = 'DOWN'
            if txt == 'LEFT':
                self.sound_dir.play()
                d = 'LEFT'
            if txt == 'RIGHT':
                self.sound_dir.play()
                d = 'RIGHT'
            if txt == 'PAUSE':
                self.sound_pause.play()
                d = ''
            if txt == 'START':
                self.sg = False #Не срабатывает.
                self.sound_start.play()
            if txt == 'STOP':
                self.sg = True #Не срабатывает.
                self.sound_stop.play()
            if txt == 'SOUND':
                self.sn = self.sn + 1
                print("self.sn = "+str(self.sn))
                if self.sn % 2 == 1:
                    self.sound_on.play()
                else:
                    self.sound_off.play()
            self.button_sleep = 0

        if self.button_sleep < 5:
            self.button_color = (DARK)
            self.button_sleep = self.button_sleep + 1

        pygame.draw.rect(canvas, color, (point_x,point_y,size_x,size_y),1)
        pygame.draw.rect(canvas, self.button_color, (point_x+frame,point_y+frame,(size_x)-frame*2,(size_y)-frame*2))

        text(canvas,txt,point_x+txt_indent_x,point_y+txt_indent_y,25,BLACK,None)

## Main

# Create Buttons
button1 = buttons()
button2 = buttons()
button3 = buttons()
button4 = buttons()
button5 = buttons()
button6 = buttons()
button7 = buttons()
button8 = buttons()
# Create SoundPlayer
sound_hallo = pygame.mixer.Sound(sound_path+"Hallo.wav")
sound_goodbye = pygame.mixer.Sound(sound_path+"GoodBye.wav")
sound_music = pygame.mixer.Sound(sound_path+"lunnaya_sonata_bethoven.wav")
sound_dir = pygame.mixer.Sound(sound_path+"dirrection.wav")
sound_pause = pygame.mixer.Sound(sound_path+"pause.wav")
sound_start = pygame.mixer.Sound(sound_path+"start_game.wav")
sound_stop = pygame.mixer.Sound(sound_path+"game_over.wav")
sound_sound = pygame.mixer.Sound(sound_path+"pause.wav")
sound_on = pygame.mixer.Sound(sound_path+"sound_on.wav")
sound_off = pygame.mixer.Sound(sound_path+"sound_off.wav")
sound_explode = pygame.mixer.Sound(sound_path+"explode.wav")

sound_hallo.play()
time.sleep(1)
sound_music.play()

# Цикл игры
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
 
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            sound_goodbye.play()
            time.sleep(1)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('UP')
                button3.button_sleep = 0
                sound_dir.play()
                d = 'UP'
            if event.key == pygame.K_DOWN:
                print('DOWN')
                button4.button_sleep = 0
                sound_dir.play()
                d = 'DOWN'
            if event.key == pygame.K_LEFT:
                print('LEFT')
                button5.button_sleep = 0
                sound_dir.play()
                d = 'LEFT'
            if event.key == pygame.K_RIGHT:
                print('RIGHT')
                button6.button_sleep = 0
                sound_dir.play()
                d = 'RIGHT'
            if event.key == pygame.K_SPACE:
                button7.button_sleep = 0
                print('SPACE')
                sound_pause.play()
                d = ''
            if event.key == pygame.K_RETURN:
                sound_start.play()
                stop_game = False
                sleep_sw = 0
                print('ENTER')
                button1.button_sleep = 0
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT  :
                sound_stop.play()
                stop_game = True
                screen_fill(screen,0,0,COL*XSIZE,ROW*YSIZE,BLACK)
                playing_field()
                frame_field() 
                sleep_sw = 1
                print('SHIFT')
                button2.button_sleep = 0
            if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                snd = snd + 1
                if snd % 2 == 1:
                    sound_on.play()
                else:
                    sound_off.play()
                print('ALT')
                button8.button_sleep = 0
                
        if event.type == pygame.MOUSEMOTION:
##            print("Позиция мыши: ", event.pos)
##            print("Position X: ", event.pos[0])
##            print("Position Y: ", event.pos[1])
            mx = event.pos[0]
            my = event.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            mcl = event.button
##            print("Нажата кнопка: ", event.button)
        else:
            mcl = False

    #Buttons
    button1.button(screen,925,240,65,40,3,'START',6,12,WHITE,mx,my,mcl)
    button2.button(screen,998,240,65,40,3,'STOP',10,12,WHITE,mx,my,mcl)

    button3.button(screen,961,287,65,40,3,'UP',20,12,WHITE,mx,my,mcl)
    button4.button(screen,961,381,65,40,3,'DOWN',5,12,WHITE,mx,my,mcl)

    button5.button(screen,925,334,65,40,3,'LEFT',12,12,WHITE,mx,my,mcl)
    button6.button(screen,998,334,65,40,3,'RIGHT',6,12,WHITE,mx,my,mcl)

    button7.button(screen,925,428,65,40,3,'PAUSE',4,12,WHITE,mx,my,mcl)
    button8.button(screen,998,428,65,40,3,'SOUND',3,12,WHITE,mx,my,mcl)

    frame_info(screen,913,229,160,251,WHITE)

    #Info
    frame_info(screen,913,0,160,220,WHITE)
    screen_fill(screen,916,3,154,214,BLACK)
    text(screen, "STEPS:  "+str(count), 920, 10, 25,WHITE)
    text(screen, "SPEED:  "+str("{:.0f}".format(speed)), 920, 33, 25,WHITE)
    text(screen, "SCORE:  "+str(score), 920, 56, 25,WHITE) 
    text(screen, "X:  "+str(x), 920, 76, 25,WHITE)
    text(screen, "Y:  "+str(y), 920, 96, 25,WHITE)
    text(screen, "DIR:  "+str(d), 920, 116, 25,WHITE)
        
    #Sleep
    if sleep_sw == 0:
        sleep = sleep + 1
    if sleep > time_sleep and stop_game == False:
        
        #Management
        if stop_game == False:
            if d == 'UP':
               y -= 1
            if d == 'DOWN':
               y += 1
            if d == 'LEFT':
               x -= 1
            if d == 'RIGHT':
               x += 1

        #Collision wall
        if x > COL-1:
            x = 0   
        if x < 0:
            x = COL-1    
        if y > ROW-1 :
            y = 0
        if y < 0 :
            y = ROW-1  
   
        #screen.fill(BLACK)
        screen_fill(screen,0,0,COL*XSIZE,ROW*YSIZE,BLACK)
    
        playing_field() #field drawing

        while sw < 1: #switcher
            ex = randint(0,ROW-1)
            ey = randint(0,COL-1)
            sw = sw + 1
            
        if stop_game == False:
            if d != '': #counter
                count += 1
                if count < max_size:
                    min_size = min_size + 1
                #print('counter = '+str(count))
                px.append(x)
                py.append(y)
       
        #snake drawing   
        for i in range(min_size):
            player(screen,px[count-i],py[count-i],BLUE)
        player(screen,px[count],py[count],VIOLET)

        #enemy drawing
        enemy(screen,ex,ey,RED)

        #Conflict snake and enemy
        if px[count] == ex and py[count] == ey:
           enemy(screen,ex,ey,BLUE)
           sound_scream = pygame.mixer.Sound(sound_path+"z"+str(randint(1,65))+".wav")
           sound_scream.play()
           sw = 0
           min_size = min_size + 1
           score = score + 1
           time_sleep = time_sleep - 0.4
           speed_sw = speed_sw + 1
           if speed_sw >= 10:
               speed = speed + 1
               speed_sw = 0

        #Conflict snake and snake
        cs = count - min_size
        while cs < count-1:
            if px[count] == px[cs] and py[count] == py[cs]:
                if stop_game == False:
                    sound_explode.play()
                text(screen, "GAME OVER!", (WIDTH / 12), (HEIGHT/2.5), 100,WHITE)
                stop_game = True
            cs = cs + 1
        
           
        frame_field() # Рамка игрового поля.

        sleep = 0
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()


        
    
