import pygame
import sys
import time

pygame.init()
height, width = 480,640
app = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Game')

point_j1 = 0
point_j2 = 0
start_time = pygame.time.get_ticks()
last_point_time = pygame.time.get_ticks()  
current_time = pygame.time.get_ticks()

#forme de Base
joueur1 = pygame.Rect(50, height // 2 - 70, 10, 140)
joueur2 = pygame.Rect(width - 60, height // 2 - 70, 10, 140)
balle = pygame.Rect(width // 2 -15, height // 2 - 15,30,30)

police = pygame.font.Font(None, 36)

balle_vit_y = 4
balle_vit_x = 4
Joueur_vit_y = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Key detection
    #Gauche
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and joueur1.top > 0:
      joueur1.y -= Joueur_vit_y
    if key[pygame.K_s] and joueur1.bottom < height:
      joueur1.y += Joueur_vit_y
    #Droite
    if key[pygame.K_UP] and joueur2.top > 0:
      joueur2.y -= Joueur_vit_y
    if key[pygame.K_DOWN] and joueur2.bottom < height:
      joueur2.y += Joueur_vit_y

    #Vitesse de la balle (Mvt)    
    GameStarted = False
    if pygame.time.get_ticks() - start_time > 2000:  
       GameStarted = True
    if GameStarted:
      balle.x += balle_vit_x
      balle.y += balle_vit_y  

    app.fill("black")


    #Collision
    if balle.top <= 0 or balle.bottom >= height:
      balle_vit_y *= -1

    if balle.colliderect(joueur1):
      balle.left = joueur1.right  
      balle_vit_x *= -1
    if balle.colliderect(joueur2):
      balle.right = joueur2.left
      balle_vit_x *= -1

    #Point Système
    if balle.right <0:
       point_j1 += 1
       joueur1 = pygame.Rect(50, height // 2 - 70, 10, 140)
       joueur2 = pygame.Rect(width - 60, height // 2 - 70, 10, 140)
       balle = pygame.Rect(width // 2 -15, height // 2 - 15,30,30)
       balle_vit_x = 4
       balle_vit_y = 4
       last_point_time = pygame.time.get_ticks()  
       print(point_j2,point_j1)
    if balle.left >= width:
       point_j2 += 1
       joueur1 = pygame.Rect(50, height // 2 - 70, 10, 140)
       joueur2 = pygame.Rect(width - 60, height // 2 - 70, 10, 140)
       balle = pygame.Rect(width // 2 -15, height // 2 - 15,30,30)
       balle_vit_x = 4
       balle_vit_y = 4
       last_point_time = pygame.time.get_ticks() 
       print(point_j2,point_j1)

    current_time = pygame.time.get_ticks()
    if current_time - last_point_time >= 10000:  
    # Augmenter la vitesse de la balle
      if balle_vit_x > 0:
        balle_vit_x += 1
      else:
        balle_vit_x -= 1
      if balle_vit_y > 0:
        balle_vit_y += 1
      else:
        balle_vit_y -= 1
      last_point_time = current_time  # reset le chrono pour la prochaine augmentation


    Score1 = police.render(str(point_j1),True,"white")
    Score2 = police.render(str(point_j2),True,"white")
    Temps_without_goal = police.render(str(balle_vit_x),True,"white")
    app.blit(Score1, (width // 4, 20))
    app.blit(Score2, (3 * width // 4 - 20, 20))
    app.blit(Temps_without_goal, (width  -50, 20))

    

    pygame.draw.rect(app,"white",joueur1)
    pygame.draw.rect(app,"white",joueur2)
    pygame.draw.ellipse(app,"white",balle)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

            
    
