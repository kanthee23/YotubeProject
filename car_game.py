import random
from time import sleep

import pygame

class Carrace:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.black = (0,0,0)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        self.initialize()


    def initialize(self):

        self.crashed = False

        #background
        self.bgImg = pygame.image.load('image/back_ground.png')
        self.bg_x1 = (self.width / 2) - (360 / 2)
        self.bg_x2= (self.width / 2) - (360 / 2)

        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 5
        self.count = 0

        # player
        self.car_img = pygame.image.load('image/car.png')
        self.car_x = (self.width / 2) - (360 / 2) + 80
        self.car_y = self.height - 120

        # fule can
        self.fule_img = pygame.image.load('image/fule.png')
        self.fule_x = (self.width / 2) - (360 / 2) + 60
        self.fule_y = 0
        self.fule_available = False


        # Enemey
        self.enemy1_img = pygame.image.load('image/enemy1.png')
        self.enemy1_x = 0
        self.enemy1_y = 0
        self.enemy1_available = False

        self.enemy2_img = pygame.image.load('image/enemy2.png')
        self.enemy2_x = 0
        self.enemy2_y = 0
        self.enemy2_available = False



        # message text
        self.score = 0
        self.height_score = 0
        self.fule = 20
        # self.speed = 0
        self.distance = 0
        self.level = 1
        self.max_speed = 100
        self.freez = True


    def back_groud(self):
        self.gameDisplay.blit(self.bgImg,(self.bg_x1,self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.height :
            self.bg_y1 = -600 + self.bg_y2

        if self.bg_y2 >= self.height:
            self.bg_y2 = -600 + self.bg_y1


    def payer(self):
        self.gameDisplay.blit(self.car_img,(self.car_x,self.car_y))


    def fule_can(self):
        if self.fule_available:
            self.gameDisplay.blit(self.fule_img, (self.fule_x, self.fule_y ))
            self.fule_y += self.bg_speed
            if self.fule_y > 600:
                self.fule_available = False

        else:
            if self.fule_y > 1000:
                self.fule_y = 0
                self.fule_x = ((self.width / 2) - (360 / 2) + 70) + ( 75 * (random.randrange(1,10) % 3 ))
                self.fule_available = True
                self.gameDisplay.blit(self.fule_img, (self.fule_x, self.fule_y))
            self.fule_y += self.bg_speed

    def enemy_update(self):
        if self.enemy1_available:
            self.gameDisplay.blit(self.enemy1_img, (self.enemy1_x, self.enemy1_y))
            if self.enemy1_y >= 0:
                self.enemy1_y += (self.bg_speed - 3)
            else:
                self.enemy1_y += self.bg_speed + 1
            if self.enemy1_y > 600:

                self.enemy1_available = False

        else:
            if self.enemy1_y > 600:
                self.enemy1_y = -150
                self.enemy1_x = ((self.width / 2) - (360 / 2) + 75) + ( 75 * (random.randrange(1,10) % 3 ))
                self.enemy1_available = True
                self.gameDisplay.blit(self.enemy1_img, (self.enemy1_x, self.enemy1_y))

            self.enemy1_y += self.bg_speed

        if self.enemy2_available:
            self.gameDisplay.blit(self.enemy2_img, (self.enemy2_x, self.enemy2_y))
            if self.enemy2_y >= 0:
                self.enemy2_y += (self.bg_speed - 3)
            else:
                self.enemy2_y += self.bg_speed + 1
            if self.enemy2_y > 600:
                self.enemy2_available = False

        else:
            if self.level > 1:
                if self.enemy2_y > 600:
                    self.enemy2_y = - ((random.randrange(1, 10) % 3) * 100 + 150)
                    k = False
                    if self.enemy1_available:
                        # while not k:
                        self.enemy2_x = ((self.width / 2) - (360 / 2) + 75) + (75 * (random.randrange(1, 10) % 3))
                            # K =  abs(self.enemy1_y - self.enemy2_y) > 5 or self.enemy1_x != self.enemy2_x

                    else:
                        self.enemy2_x = ((self.width / 2) - (360 / 2) + 75) + (75 * (random.randrange(1, 10) % 3))


                    self.enemy2_available = True
                    self.gameDisplay.blit(self.enemy2_img, (self.enemy2_x, self.enemy2_y))

                self.enemy2_y += self.bg_speed


    def run_car(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.car_x += 75
                    elif event.key == pygame.K_LEFT:
                        self.car_x -= 75

                    # elif event.key == pygame.K_UP:
                    #     self.bg_speed += 1
                    # elif event.key == pygame.K_DOWN:
                    #     self.bg_speed -= 1


            self.score += 1
            self.level_update()
            self.gameDisplay.fill(self.black)
            self.back_groud()
            self.payer()
            self.enemy_update()
            self.fule_can()

            self.fule_update()
            self.show_msg()
            pygame.display.update()
            self.clock.tick(60)


        pygame.quit()

    def level_update(self):
        x = (self.score// 500) + 1
        if x != self.level:
            self.level = x
            self.bg_speed += 1

    def fule_update(self):
        self.distance =  (self.bg_speed * 1 /(10))
        self.fule -=  (self.distance / 15)
        if self.fule <= 0:
            self.crashed = True

        if self.car_x - self.fule_x == 10 and self.car_y - self.fule_y <= 50 and self.fule_x != 0:
            self.fule += 10
            self.fule_available = False
            self.fule_x = 0


    def game_window(self):
        self.gameDisplay = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Car Race')
        self.run_car()

    def show_msg(self):
        font = pygame.font.SysFont("comicsansms", 30, True)
        text = font.render(str('SPEED'), True, (0, 255, 255))
        self.gameDisplay.blit(text, (0, 0))
        text = font.render(str(self.bg_speed * 5), True, (255, 255, 255))
        self.gameDisplay.blit(text, (0, 30))

        text = font.render(str('SCORE'), True, (0, 255, 255))
        self.gameDisplay.blit(text, (0, 100))
        text = font.render(str(self.score), True, (255, 255, 255))
        self.gameDisplay.blit(text, (0, 130))

        text = font.render(str('FULE'), True, (0, 255, 255))
        self.gameDisplay.blit(text, (0, 200))
        text = font.render(str('{f:.2f} L'.format(f =self.fule)), True, (255, 255, 255))
        self.gameDisplay.blit(text, (0, 230))

        text = font.render(str('LEVEL'), True, (0, 255, 255))
        self.gameDisplay.blit(text, (0, 300))
        text = font.render(str(self.level), True, (255, 255, 255))
        self.gameDisplay.blit(text, (0, 330))


car = Carrace()
car.game_window()

