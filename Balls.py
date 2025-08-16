import random 
import matplotlib.colors as mcolors

class Balls :

    def __init__(self):
        self.x = 200 
        self.y = 200
        self.vx = random.uniform(-2 ,2)
        self.vy = 0. # To enable Graphity 
        self.radius = 10
        self.color = random.choice(list(mcolors.CSS4_COLORS.keys()))
        
        
    def update (self, ballsList , arc_rect ) :
        self.vy +=0.1 # for Gravity 
        self.x += self.vx
        self.y += self.vy 
        
        # Check vertical boundary of arc (simple box for now)
        if self.y + self.radius > arc_rect[1] + arc_rect[3]:
            # Ball “fell down” → create new ball
            ballsList.append(Balls())
            # Reset this ball to top
            self.x = 400
            self.y = 200
            self.vx = random.uniform(-2, 2)
            self.vy = 0
        
        # Keep inside horizontal boundaries (optional)
        if self.x - self.radius < arc_rect[0]:
            self.x = arc_rect[0] + self.radius
            self.vx *= -1
        if self.x + self.radius > arc_rect[0] + arc_rect[2]:
            self.x = arc_rect[0] + arc_rect[2] - self.radius
            self.vx *= -1
   