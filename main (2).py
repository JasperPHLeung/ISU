import pygame#pygame
import random#random
from sys import exit#exit

pygame.init()#start pygame
pygame.mixer.init()#start sound
screen = pygame.display.set_mode((300, 400))#surface
screen.fill('white')#color
pygame.display.set_caption("Ora")#name
clock = pygame.time.Clock()#timer&fps

kobushi1 = pygame.image.load('kobushi.png').convert_alpha()
kobushi2 = pygame.image.load('kobushi.png').convert_alpha()
kobushi3 = pygame.image.load('kobushi.png').convert_alpha()
kobushi4 = pygame.image.load('kobushi.png').convert_alpha()#image
line2 = pygame.Surface((500, 6))
line2.fill('gray')
line1 = pygame.Surface((6, 500))
line1.fill('gray')#line
ora1 = pygame.mixer.Sound("ora1.wav")
ora2 = pygame.mixer.Sound("ora2.wav")
ora3 = pygame.mixer.Sound("ora3.wav")
ora4 = pygame.mixer.Sound("ora4.wav")
ora5 = pygame.mixer.Sound("ora5.wav")
ora6 = pygame.mixer.Sound("ora6.wav")
ora7 = pygame.mixer.Sound("ora7.wav")
ora =[ora1,ora2,ora3,ora4,ora5,ora6,ora7]#sound

kobushi_y1 = 300
kobushi_y2 = 200
kobushi_y3 = 100
kobushi_y4 = 0
kobushi_x = [0, 75, 150, 225]
kobushi_x1 = kobushi_x[random.randint(0, 3)]
kobushi_x2 = kobushi_x[random.randint(0, 3)]
kobushi_x3 = kobushi_x[random.randint(0, 3)]
kobushi_x4 = kobushi_x[random.randint(0, 3)]
inloop = [kobushi_x1, kobushi_x2, kobushi_x3, kobushi_x4]#positions

running = True#run program
started = False#wait for game to start
score = 0
timer = 1800
check = -1
kobushi_x1 = kobushi_x[0]
kobushi_x2 = kobushi_x[3]
kobushi_x3 = kobushi_x[1]
kobushi_x4 = kobushi_x[2]#game variables

text_font = pygame.font.Font(None, 50)
text = text_font.render("ORA", False, 'purple')
start_font = pygame.font.Font(None, 30)
start = start_font.render("press space to start", False, 'black')# Fonts and text


while running:#start
    screen.fill('white')#screen background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()#exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:#start game button(space)
                score = 0#reset score
                started = True#start game
                
                

    if started:#start
        timer -= 1#count down timer
        keys = pygame.key.get_pressed
        if keys[pygame.K_d]:
            input = 0
        elif keys[pygame.K_f]:
            input = 75
        elif keys[pygame.K_j]:
            input = 150
        elif keys[pygame.K_k]:
            input = 225#input
        else:
            input = -1#no input


        if kobushi_y1 >= 300 and input == kobushi_x1:#when it is time to type in
            kobushi_y1 = 0#go back
            kobushi_x1 = kobushi_x[random.randint(0, 3)]#random roll
            while check == kobushi_x1:
                kobushi_x1 = kobushi_x[random.randint(0, 3)]
            check = kobushi_x1#don't repeat
            score += 1#score count
            kobushi_y2 += 100
            kobushi_y3 += 100
            kobushi_y4 += 100#move
            sound = random.randint(0,6)
            ora[sound].play()#sound
        if kobushi_y2 >= 300 and input == kobushi_x2:
            kobushi_y2 = 0
            kobushi_x2 = kobushi_x[random.randint(0, 3)]
            while check == kobushi_x2:
                kobushi_x2 = kobushi_x[random.randint(0, 3)]
            check = kobushi_x2
            score += 1
            kobushi_y1 += 100
            kobushi_y3 += 100
            kobushi_y4 += 100
            sound = random.randint(0,6)
            ora[sound].play()
        if kobushi_y3 >= 300 and input == kobushi_x3:
            kobushi_y3 = 0
            kobushi_x3 = kobushi_x[random.randint(0, 3)]
            while check == kobushi_x3:
                kobushi_x3 = kobushi_x[random.randint(0, 3)]
            check = kobushi_x3
            score += 1
            kobushi_y2 += 100
            kobushi_y1 += 100
            kobushi_y4 += 100
            sound = random.randint(0,6)
            ora[sound].play()
        if kobushi_y4 >= 300 and input == kobushi_x4:
            kobushi_y4 = 0
            kobushi_x4 = kobushi_x[random.randint(0, 3)]
            while check == kobushi_x4:
                kobushi_x4 = kobushi_x[random.randint(0, 3)]
            check = kobushi_x4
            score += 1
            kobushi_y2 += 100
            kobushi_y3 += 100
            kobushi_y1 += 100
            sound = random.randint(0,6)
            ora[sound].play()

        # Display kobushis and score
        screen.blit(line2, (0, 97))
        screen.blit(line2, (0, 197))
        screen.blit(line2, (0, 297))
        screen.blit(line1, (72, 0))
        screen.blit(line1, (147, 0))
        screen.blit(line1, (222, 0))#display(background)
        screen.blit(kobushi1, (kobushi_x1, kobushi_y1))
        screen.blit(kobushi2, (kobushi_x2, kobushi_y2))
        screen.blit(kobushi3, (kobushi_x3, kobushi_y3))
        screen.blit(kobushi4, (kobushi_x4, kobushi_y4))#display(kobushi)
        show_mark = text_font.render(f'Score: {score}', False, 'purple')
        screen.blit(show_mark, (125, 20))#score
        show_timer = text_font.render(f'Time: {timer//18}', False, 'black')  # Display time
        screen.blit(show_timer, (125, 50))#timer

        if timer <= 0:#when time out
            started = False
            timer = 1800  #Reset timer

    else:
        Dio = start_font.render(f"You hitted Dio for {score} times", False, 'black')
        screen.blit(text, (110, 90))
        screen.blit(start, (50, 150))
        screen.blit(Dio,(10,300))#start message

    pygame.display.update()#update
    clock.tick(120)  #fps