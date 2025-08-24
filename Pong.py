import pygame
import sys

pygame.init()
height, width = 480,640
app = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Game')

joueur1 = pygame.Rect(50, height // 2 - 70, 10, 140)
joueur2 = pygame.Rect(width - 60, height // 2 - 70, 10, 140)
balle = pygame.Rect(width // 2 -15, height // 2 - 15,30,30)

balle_vit_y = 5
balle_vit_x = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
      joueur1.y -= 2
    if key[pygame.K_s]:
      joueur1.y += 2

    if key[pygame.K_UP]:
      joueur2.y -= 2
    if key[pygame.K_DOWN]:
      joueur2.y += 2

    balle.x = balle_vit_x
    balle.y = balle_vit_y  

    app.fill("black")

    pygame.draw.rect(app,"white",joueur1)
    pygame.draw.rect(app,"white",joueur2)
    pygame.draw.ellipse(app,"white",balle)

    pygame.display.update()
    pygame.time.Clock().tick(60)

            
    
