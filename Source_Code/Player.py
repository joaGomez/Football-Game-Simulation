from Constants import *

class Player:
    def __init__(self, startPos, role):
        self.velocity = 0.0
        self.position = startPos
        self.role = role
        
        
        
        
    def move(self, direction):
        self.position = (self.position.x + direction.x*self.velocity, self.position.y + direction.y*self.velocity)
        
    def stop(self):
        self.velocity = 0.0
        
