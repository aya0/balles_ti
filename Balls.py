import random
import math
import matplotlib.colors as mcolors
from Arc import ArcRect  # your ArcRect class

class Balls:
    def __init__(self, arc):
        # If a tuple is passed, convert to ArcRect
        if isinstance(arc, tuple):
            arc = ArcRect(*arc)

        self.arc = arc

        # Arc center and radius
        self.cx = arc.x + arc.width / 2
        self.cy = arc.y + arc.height / 2
        self.R = arc.width / 2  # assuming circle

        # Start ball on arc edge at a random angle
        theta = random.uniform(0, math.pi)  # adjust for your arc span
        self.x = self.cx + (self.R - 10) * math.cos(theta)  # 10 = ball radius
        self.y = self.cy + (self.R - 10) * math.sin(theta)

        # Velocity
        self.vx = random.uniform(-2, 2)
        self.vy = 0

        self.radius = 10

        # Random color
        color_name = random.choice(list(mcolors.CSS4_COLORS.keys()))
        rgb_float = mcolors.to_rgb(mcolors.CSS4_COLORS[color_name])
        self.color = tuple(int(c*255) for c in rgb_float)

    def update(self, ballsList, arc):
        # If a tuple is passed, convert to ArcRect
        if isinstance(arc, tuple):
            arc = ArcRect(*arc)

        self.vy += 0.1  # gravity
        self.x += self.vx
        self.y += self.vy

        # Arc center & radius
        cx = arc.x + arc.width / 2
        cy = arc.y + arc.height / 2
        R = arc.width / 2

        # Collision with arc boundary
        dx = self.x - cx
        dy = self.y - cy
        dist = math.sqrt(dx*dx + dy*dy)

        if dist + self.radius >= R:
            angle = math.atan2(dy, dx)
            if 0 <= angle <= math.pi:  # adjust to your arc span
                nx, ny = dx / dist, dy / dist
                dot = self.vx * nx + self.vy * ny
                self.vx -= 2 * dot * nx
                self.vy -= 2 * dot * ny

        # Horizontal bounds (optional)
        if self.x - self.radius < arc.x:
            self.x = arc.x + self.radius
            self.vx *= -1
        if self.x + self.radius > arc.x + arc.width:
            self.x = arc.x + arc.width - self.radius
            self.vx *= -1

        # If ball falls below arc, spawn a new one
        if self.y - self.radius > arc.y + arc.height:
            ballsList.append(Balls(arc))
            # Reset this ball to top
            theta = random.uniform(0, math.pi)
            self.x = cx + (R - self.radius) * math.cos(theta)
            self.y = cy + (R - self.radius) * math.sin(theta)
            self.vx = random.uniform(-2, 2)
            self.vy = 0.0
