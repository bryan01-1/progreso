import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ping Pong')

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de las paletas
PALETA_ANCHO = 15
PALETA_ALTO = 90

# Crear paletas
paleta_izq = pygame.Rect(50, ALTO//2 - PALETA_ALTO//2, PALETA_ANCHO, PALETA_ALTO)
paleta_der = pygame.Rect(ANCHO - 50 - PALETA_ANCHO, ALTO//2 - PALETA_ALTO//2, PALETA_ANCHO, PALETA_ALTO)

# Crear pelota
pelota = pygame.Rect(ANCHO//2 - 15//2, ALTO//2 - 15//2, 15, 15)

# Velocidades iniciales
velocidad_paleta = 5
velocidad_x = 7 * random.choice((1, -1))
velocidad_y = 7 * random.choice((1, -1))

# Bucle principal del juego
jugando = True
while jugando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Movimiento de las paletas
    teclas = pygame.key.get_pressed()
    
    # Paleta izquierda (W y S)
    if teclas[pygame.K_w]:
        if paleta_izq.top > 0:
            paleta_izq.y -= velocidad_paleta
    elif teclas[pygame.K_s]:
        if paleta_izq.bottom < ALTO:
            paleta_izq.y += velocidad_paleta

    # Paleta derecha (Flecha Arriba y Abajo)
    if teclas[pygame.K_UP]:
        if paleta_der.top > 0:
            paleta_der.y -= velocidad_paleta
    elif teclas[pygame.K_DOWN]:
        if paleta_der.bottom < ALTO:
            paleta_der.y += velocidad_paleta

    # Movimiento de la pelota
    pelota.x += velocidad_x
    pelota.y += velocidad_y


# Cerrar Pygame
pygame.quit()