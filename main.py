#inicio :]
import pygame
from pygame.locals import *
pygame.init()

# creacion de la ventana 
ventana_alto = 800
ventano_ancho = 600
ventana =(ventana_alto, ventano_ancho)

# visualisacion de la ventana
ventana_avansada = pygame.display.set_mode(ventana)

# titulo e icono
pygame.display.set_caption("FiFa car Game aiaia")
icono = pygame.image.load("mesiformer.png")
pygame.display.set_icon(icono)

#color de la ventana
ventana_avansada.fill((235,50,0))

#actualizando la ventana

pygame.display.update()

# iniciando el juego :¡
iniciando = True
while iniciando:
    for event in pygame.event.get():
        if event.type == QUIT:
            iniciando = False

        if event.type == KEYDOWN:
            if event.Key == K_ESCAPE:
                ventana_avansada = False

        if event.type == KEYDOWN:
            if event.Key == K_F4.K_1.K_2.K_3.K_4.K_5.K_6.K_7.K_8.K_9.K_10:
                ventana_avansada = False
           
           