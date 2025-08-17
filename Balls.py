import random 
import matplotlib.colors as mcolors
import Arc 
import math

class Balls :
    arc = Arc.ArcRect(400 ,200 ,200 ,200)
    def __init__(self , arc ):
        self.x = arc.x + arc.width/2
        self.y = arc.y + arc.height/2
        self.vx = random.uniform(-2 ,2)
        self.vy = 0. # To enable Graphity 
        self.radius = 10
        color_name = random.choice(list(mcolors.CSS4_COLORS.keys()))
        rgb_float = mcolors.to_rgb(mcolors.CSS4_COLORS[color_name])
        rgb = tuple(int(c*255) for c in rgb_float)
        self.color = rgb
        
        
    def update (self, ballsList , arc_rect ) :
        self.vy +=0.1 # for Gravity 
        self.x += self.vx
        self.y += self.vy 
        
        # Check vertical boundary of arc (simple box for now)
        if self.y + self.radius > arc_rect[1] + arc_rect[3]:
            # Ball “fell down” → create new ball
            ballsList.append(Balls(self.arc))
            # Reset this ball to top
            self.x = self.arc.x + self.arc.width/2
            self.y = self.arc.y + self.arc.height/2
            self.vx = random.uniform(-2, 2)
            self.vy = 0
        
        # Keep inside horizontal boundaries (optional)
        if self.x - self.radius < arc_rect[0]:
            self.x = arc_rect[0] + self.radius
            self.vx *= -1
        if self.x + self.radius > arc_rect[0] + arc_rect[2]:
            self.x = arc_rect[0] + arc_rect[2] - self.radius
            self.vx *= -1
            
            
        # Distance to circle center
        dx = self.x - cx
        dy = self.y - cy
        dist = math.sqrt(dx*dx + dy*dy)

    # Check collision with circle boundary
        if dist +  self.radius >= R:
        # Compute angle to check if it's inside arc
            angle = math.atan2(dy, dx)
            if  0 <= angle <= 5*math.pi/3:
            # Normal vector
                nx, ny = dx / dist, dy / dist

            # Reflect velocity
            
                dot = vx*nx + vy*ny
                vx -= 2 * dot * nx
                vy -= 2 * dot * ny    
       
            
       
            


    