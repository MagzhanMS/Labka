import pygame
def updatePoints(pts):
    
    for q in range(45):
        pts[0]-=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), colors, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for i in range(45):
        pts[0]-=1
        pts[1]+=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), colors, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for k in range(45):
        pts[0]+=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), colors, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for j in range(45):
        pts[0]+=1
        pts[1]+=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), colors, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    

def shear(pts):
    for i in range(100):
        pts[0] += 1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), colors, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for j in range(200):
        pts[0] -= 1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), colors, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for t in range(200):
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), colors, pts, 100+t)
        pygame.display.update()
        pygame.display.flip()
        

surface = pygame.display.set_mode((800, 600))
color = (200, 200, 200)
colors = (200,200,200)
points = [400,300]
pygame.display.init()
img = pygame.draw.circle(surface, color, [200, 150], 50)
pygame.display.flip()
pygame.time.wait(1000)
img = pygame.draw.circle(surface, color, [200, 150], 100)
pygame.time.wait(1000)
updatePoints([200,200]) 
shear(points)
pygame.display.flip()


pygame.draw.rect(surface,(140,168,197),(300,300,40,60))
pygame.display.flip()
