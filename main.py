import pygame, numpy as np

SCREEN_SIZE = (1200,700)
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()

def init_display():
    global screen, background, matryca
    matryca = matrix()
    screen = pygame.display.set_mode((SCREEN_SIZE))
    background = pygame.Surface(screen.get_size())
    clear()

class matrix:

    def __init__(self):
        self.matrix_num = [[j+i*6+65 for j in range(6)] for i in range(5)]
        self.matrix_bin = [[binarny(x) for x in rows] for rows in self.matrix_num]
        self.matrix_chr = [[chr(x) for x in rows] for rows in self.matrix_num]
        self.matrix_chr[4] = ['Y','Z','?','!','.','spc']
        self.matrix_map = [[[int(x[map_count]) for x in rows] for rows in self.matrix_bin] for map_count in range(5)]

    def numeric_all(self):
        return self.matrix_num
    def binary_all(self):
        return self.matrix_bin
    def character_all(self):
        return self.matrix_chr
    def map_all(self):
        return self.matrix_map

def binarny(liczba):
    return bin(liczba)[4:]

def clear():
    global background,screen
    background.fill(BLACK)
    screen.blit(background,(0,0))
    font = pygame.font.SysFont("Times", 50)
    for row, line in enumerate(matryca.character_all()):
        for column, element in enumerate(line):
            text1 = font.render(element, True, WHITE)
            screen.blit(text1, (column * 200 + 75, row * 140 + 45))

def bordering(C,D,A,B):
    pygame.draw.line(screen,WHITE,(A,C),(A,D))
    pygame.draw.line(screen,WHITE,(A,C),(B,C))
    pygame.draw.line(screen,WHITE,(B,C),(B,D))
    pygame.draw.line(screen,WHITE,(B,D),(A,D))

def webbing(nr):
    global screen
    for row, line in enumerate(matryca.map_all()[nr]):
        for column, element in enumerate(line):
            if element == 1:
                bordering(row*140+10,row*140+130,column*200+10,column*200+190)

def go():
    nr = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if nr>4:
            nr=0
            clear()
            pygame.display.update()
            pygame.time.wait(1000)
        else:
            webbing(nr)
            pygame.display.update()
            pygame.time.wait(500)
            clear()
            pygame.display.update()
            nr+=1



init_display()
go()
pygame.quit()
