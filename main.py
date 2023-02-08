import pygame
from pygame.locals import *
pygame.init()
import random
# ventana creacion
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

## P2.1 - Road parameters
ROAD_W = 500

## P2.3 - Roadmark width
ROADMARK_W = 10

#carril derecho

carril_derecho = SCREEN_WIDTH/2 + ROAD_W/4
carril_isquierdo = SCREEN_WIDTH/2 - ROAD_W/4

# ventana alta gama
screen = pygame.display.set_mode( SIZE )

# el titulo
pygame.display.set_caption("FIFA car game")

# el icono
ICON = pygame.image.load("mesiformer la destruccion.png")
pygame.display.set_icon(ICON)

#velocidad de mbbappe
velocidad = 10

#texto del fin
texto = pygame.font.Font("TheSnailson-K7glW.otf", 64)
textoX = 400
textoY = 400
# game over texto y funcion
def fin(x, y):
    texto_inicio = texto.render("te dejaron 7-0 jaja nuv", True, (87,87,86))
    screen.blit(texto_inicio, (x, y))
# los colores god 



# pila recargable
pygame.display.update()
#mesi creation
mesi_car = pygame.image.load("car.png")
mesi_car_loc = mesi_car.get_rect()
mesi_car_loc.center = carril_derecho, SCREEN_HEIGHT*0.6
# mbbappe creation
mbbappe_car = pygame.image.load("racing-car.png")
mbbappe_car_loc = mbbappe_car.get_rect()
mbbappe_car_loc.center = carril_isquierdo, SCREEN_HEIGHT*0.2



# juego creation
#contador
contador = 0
running = True
while running:

    contador += 1

    if contador == 5000:
        velocidad += 0.15
    #enemigo vivo!

    mbbappe_car_loc.y += velocidad
   

    #mbbappe vuelve a la carretera
    if mbbappe_car_loc.y > SCREEN_HEIGHT:
        mbbappe_car_loc.y = -250

        #mbbappe loco
        if random.randint(0, 1) == 0:
            mbbappe_car_loc.center = carril_derecho, -200

        else:
            mbbappe_car_loc.center = carril_isquierdo, -200

    # fin del partido 
    if mesi_car_loc[0] == mbbappe_car_loc[0] and mbbappe_car_loc[1] > mesi_car_loc[1] - 64: 
        #fin(textoX, textoY)
        #print("perdiste")
        pygame.display.update()
        break

    for event in pygame.event.get():
        
        
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == KEYDOWN:
            if event.key == K_1:
                running = False

            if event.key in [K_a, K_LEFT]:
                mesi_car_loc = mesi_car_loc.move(-ROAD_W/2, 0)

            if event.key in [K_d, K_RIGHT]:
                mesi_car_loc = mesi_car_loc.move(ROAD_W/2, 0)

    screen.fill((255, 220, 0))

    ## P2.2 - Draw the road
    pygame.draw.rect(screen, (50, 50, 0), (SCREEN_WIDTH/2  - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

    ## p2.4 - Draw the roadmark
    pygame.draw.rect(screen, (255, 240, 60), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

    ## lineas con derechos
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

            


    # dibujando un carrito facha 
    screen.blit(mesi_car, mesi_car_loc)
    screen.blit(mbbappe_car, mbbappe_car_loc)
    # actualisando el app
    pygame.display.update()