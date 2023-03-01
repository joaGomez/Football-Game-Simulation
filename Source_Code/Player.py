class Player:
    def __init__(self, start_pos):
        self.velocity = 0.0
        self.position = (start_pos.x, start_pos.y)
        self.role = "None"
        
        
    def move(self, direction):
        self.position = (self.position.x + direction.x*self.velocity, self.position.y + direction.y*self.velocity)
        
    def stop(self):
        self.velocity = 0.0
        
