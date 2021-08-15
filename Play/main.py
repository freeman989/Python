import pygame
pygame.init()
window=pygame.display.set_mode((281, 500))
pygame.display.set_caption("Игрушка")
x=50
y=50
widht=40
height=60
speed=5
run=True
jump=False
jumpCount=10
zvuk=1
el=pygame.image.load("el.png")
bg=pygame.image.load("bg.jpg")
song = pygame.mixer.Sound('el.ogg')
pygame.mixer.music.load('hello.mp3')
pygame.mixer.music.play()
while run:
	pygame.time.delay(25)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x>5:
		x-=speed
	if keys[pygame.K_RIGHT] and x<281-widht-5:
		x+=speed
	if not(jump):
		if keys[pygame.K_UP] and y>5:
			y-=speed
		if keys[pygame.K_DOWN] and y<500-height-5:
			y+=speed
		if keys[pygame.K_SPACE]:
			jump=True
	else:
		if zvuk==1:
			song.play()
			zvuk=0
		if jumpCount>=-10:
			if jumpCount<0:
				y+=(jumpCount**2)/2	
			else:
				y-=(jumpCount**2)/2
			jumpCount-=1
		else: 
			jump=False
			jumpCount=10
			zvuk=1
	window.blit(bg,(0,0))
	tupler=(int(x), int(y))
	window.blit(el, tupler)
	pygame.display.update()

