import pygame
from pygame.locals import *
pygame.init()

# ventana creacion
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

## P2.1 - Road parameters
ROAD_W = 500

## P2.3 - Roadmark width
ROADMARK_W = 10


# ventana alta gama
screen = pygame.display.set_mode( SIZE )

# el titulo
pygame.display.set_caption("FIFA car game")

# el icono
ICON = pygame.image.load("mesiformer.png")
pygame.display.set_icon(ICON)

# los colores god 
screen.fill((60, 220, 0))

## P2.2 - Draw the road
pygame.draw.rect(screen, (50, 50, 50), (SCREEN_WIDTH/2  - ROAD_W/2, 0, ROAD_W, SCREEN_HEIGHT))

## p2.4 - Draw the roadmark
pygame.draw.rect(screen, (255, 240, 60), (SCREEN_WIDTH/2 - ROADMARK_W/2, 0, ROADMARK_W, SCREEN_HEIGHT))

## lineas con derechos
pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 - ROAD_W/2 + ROADMARK_W * 2, 0, ROADMARK_W, SCREEN_HEIGHT))

pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH/2 + ROAD_W/2 - ROADMARK_W * 3, 0, ROADMARK_W, SCREEN_HEIGHT))

# pila recargable
pygame.display.update()
#mesi creation
mesi_car = pygame.image.load("mesiformer2 el regreso.png")
mesi_car_loc = mesi_car.get_rect()
mesi_car_loc.center = SCREEN_WIDTH/2 + ROAD_W/4, SCREEN_HEIGHT*0.6
# mbbappe creation
mbbappe_car = pygame.image.load("mbbappesepticon3 la resureccion.png")
mbbappe_car_loc = mbbappe_car.get_rect()
mbbappe_car_loc.center = SCREEN_WIDTH/2 - ROAD_W/4, SCREEN_HEIGHT*0.3


# juego creation
running = True
while running:
    for event in pygame.event.get():
        
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == KEYDOWN:
            if event.key == K_1:
                running = False

    # dibujando un carrito facha 
    screen.blit(mesi_car, mesi_car_loc)
    screen.blit(mbbappe_car, mbbappe_car_loc)
    # actualisando el app
    pygame.display.update()