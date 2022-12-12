import pygame
from random import randint
pygame.font.init()
pygame.init()
window = pygame.display.set_mode((800, 600))
tlo = pygame.image.load("zdj.jpg")

class Fizyka:
    def __init__(self, x, y, width, height,acc, max_szyb):
        self.x_cord = x
        self.y_cord = y
        self.szyb_poziom = 0
        self.szyb_pion = 0
        self.acc = acc
        self.max_szyb = max_szyb
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.cofnij_x = x
        self.cofnij_y = y
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.skakanie = False
        self.prawo = 0
        self.gora = 0
        self.wynik = 0
    def fizyka_tick(self, sciany):
        self.szyb_pion += 0.3
        self.x_cord += self.szyb_poziom
        self.y_cord += self.szyb_pion

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        for sciana in  sciany:
            if sciana.hitbox.colliderect(self.hitbox):
                if self.x_cord + self.width >= sciana.x_cord + 1 > self.cofnij_x  + self.width:
                    self.x_cord = self.cofnij_x
                    self.szyb_poziom = -10
                if self.x_cord <= sciana.x_cord + sciana.width -1 < self.cofnij_x:
                    self.x_cord = self.cofnij_x
                    self.szyb_poziom = 10
                if self.y_cord + self.height >= sciana.y_cord +1 > self.cofnij_y + self.height:
                    self.y_cord = self.cofnij_y
                    self.szyb_pion = -4
                    self.skakanie = False
                if self.y_cord <= sciana.y_cord + sciana.height - 1 < self.cofnij_y:
                    self.y_cord = self.cofnij_y
                    self.szyb_pion = 10


                if self.y_cord <= sciana.x_cord + sciana.width - 1 < self.cofnij_y:
                    self.y_cord = self.cofnij_y
                    self.szyb_pion = 0

        self.cofnij_x = self.x_cord
        self.cofnij_y = self.y_cord



class Punkty:
    def __init__(self):
        self.x_cord = 680
        self.y_cord = 220
        self.image = pygame.image.load("kosz.png")
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height )

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height )


    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Gracz(Fizyka):
    def __init__(self):

        self.image = pygame.image.load("pilka.png")
        width = self.image.get_width()
        height = self.image.get_height()
        super().__init__(30,400,width, height, 0.5, 5)




    def tick(self, ruch, sciany):

        self.fizyka_tick(sciany)

        if ruch[pygame.K_a] and self.szyb_poziom > self.max_szyb * -1:
            self.szyb_poziom -= self.acc
        if ruch[pygame.K_d] and self.szyb_poziom < self.max_szyb:
            self.szyb_poziom += self.acc
        if not (ruch[pygame.K_a] or ruch[pygame.K_d]):
            if self.szyb_poziom > 0:
                self.szyb_poziom -= self.acc
            elif self.szyb_poziom < 0:
                self.szyb_poziom += self.acc

        if ruch[pygame.K_w] and self.skakanie is False:
            self.szyb_pion -=15
            self.skakanie = True


        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height )


        if ruch[pygame.K_SPACE] and self.skakanie is False :
            self.szyb_poziom += self.prawo
            self.szyb_pion -= self.gora
            self.skakanie = True


    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Sciany:

    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (222, 128, 128), self.hitbox)


def main():

    run = True
    gracz = Gracz()
    zegar = 0
    wynik = 0
    trafy = []
    sciany = [

        Sciany(0, 560, 800, 40),
        Sciany(0, 490, 800, 70),
        Sciany(675, 220, 1, 1),
        Sciany(675, 260, 1, 1),
        Sciany(770, 220, 1, 1),
        Sciany(770, 260, 1, 1),
        Sciany(0, 0, 10, 600),
        Sciany(790, 0, 10, 600),
        Sciany(0, 0, 800, 10),
    ]



    while run:

        zegar += pygame.time.Clock().tick(144) /1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        ruch = pygame.key.get_pressed()

        if zegar >= 0.5:
            zegar = 0
            trafy.append(Punkty())
        if len(trafy) > 1 :
            trafy.remove(traf)

        gracz.tick(ruch, sciany)

        for traf in trafy:
            traf.tick()

        for traf in trafy:
            if gracz.hitbox.colliderect(traf.hitbox):
                trafy.remove(traf)
                wynik += 1



        window.fill((230, 116, 46))
        window.blit(tlo,(0,0))
        gracz.draw()
        for sciana in sciany:
            sciana.draw(window)
        for traf in trafy:
            traf.draw()



        #Ustawienia

        if ruch[pygame.K_LEFT]:
            gracz.prawo -= 0.5
        if ruch[pygame.K_RIGHT]:
            gracz.prawo += 0.5
        if ruch[pygame.K_DOWN]:
            gracz.gora -= 0.5
        if ruch[pygame.K_UP]:
            gracz.gora += 0.5
        if ruch[pygame.K_q]:
            run = False
        if ruch[pygame.K_1]:
            gracz.x_cord = 20
            gracz.y_cord = 350
        if ruch[pygame.K_2]:
            gracz.x_cord = 300
            gracz.y_cord = 350
        if ruch[pygame.K_3]:
            gracz.x_cord = 500
            gracz.y_cord = 350
        if ruch[pygame.K_r]:
            wynik = 0
            gracz.prawo = 0
            gracz.gora = 0



        Góra = pygame.font.Font.render(pygame.font.SysFont("arial", 25), f"Siła pionowo ( ↕ ): {gracz.gora}", True, (0, 0, 0))
        Prawo = pygame.font.Font.render(pygame.font.SysFont("arial", 25), f"Siła poziomo ( ↔ ): {gracz.prawo}", True, (0, 0, 0))
        wyjdz = pygame.font.Font.render(pygame.font.SysFont("arial", 17), f"Wyjdz (Q)", True, (0, 0, 0))
        Pozycja_1 = pygame.font.Font.render(pygame.font.SysFont("arial", 17), f"(1)   Pozycja numer 1", True,(0, 0, 0))
        Pozycja_2 = pygame.font.Font.render(pygame.font.SysFont("arial", 17), f"(2)   Pozycja numer 2", True,(0, 0, 0))
        Pozycja_3 = pygame.font.Font.render(pygame.font.SysFont("arial", 17), f"(3)   Pozycja numer 3", True,(0, 0, 0))
        wynik_koncowy = pygame.font.Font.render(pygame.font.SysFont("arial", 25), f"Wynik: {wynik}", True,(0, 0, 0))
        restart = pygame.font.Font.render(pygame.font.SysFont("arial", 15), f"Reset (R)", True,(0, 0, 0))



        window.blit(Góra, (20, 500))
        window.blit(Prawo, (20, 530))
        window.blit(wyjdz, (20, 570))
        window.blit(wynik_koncowy, (12, 10))
        window.blit(Pozycja_1, (300, 540))
        window.blit(Pozycja_2, (450, 540))
        window.blit(Pozycja_3, (600, 540))
        window.blit(restart, (745, 580))


        pygame.display.update()



    print(wynik)

if __name__ == "__main__":
    main()

