import pygame
import math 
import Balls
import Arc


 #Ruls 
# if the ball go out hor right (300 +200) left(300 -200) then it's out side the arc  ---> make new ball
# also i can cheak if the vert up(200 +200) down (200+200) then it's out side the arc ---> make new ball 
# i just need to cheack the vertical side becuas the ball always will fall down  

#1- i need to bulid ball to move in side the arc 
#2- every time this ball fall donw the number of ball will increase by one 
#3- balles must move bassed on pysicis rulls


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#arc parameters 
arc_rect1 = Arc. ArcRect(400 , 200 , 200 ,200)
arc_rect = (400 , 200 , 200 ,200)
start_angle = 0
end_angle = 5*math.pi/3.     #300 degrees


#Ball Lis 
ballsList =[]
ballsList.append(Balls.Balls(arc_rect1))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill background black
    
    pygame.draw.arc(screen, (250, 250, 250), arc_rect, start_angle, end_angle, 5)
    
    for ball in ballsList:
        ball.update(ballsList , arc_rect)
        pygame.draw.circle(screen , ball.color , (int(ball.x) , int(ball.y)) , ball.radius)
    
    pygame.display.flip()
    clock.tick(60)
        


pygame.quit()
