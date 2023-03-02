from enum import Enum
from Team import *



class States(Enum):
    INIT, RUN, PAUSE, END = range(1, 5)         # INIT = 1, PLAYING = 2, PAUSE = 3, END = 4
    
    


class Game:
    def __init__(self, windowHeight, windowWidth, nPlayers):
        self.windowHeight = windowHeight    # Window size
        self.windowWidth = windowWidth      
        self.players = nPlayers             # Numbers of players in each team
        self.state = States.INIT.value      # Game state
        
    def initGame(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.state = States.RUN.value
        self.window.fill(BLACK)
        self.clock = pygame.time.Clock()
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = States.END.value
                    
    def render(self):
        self.window.fill(BLACK)
        
        pygame.display.flip()
        
    def endGame(self):
        pygame.quit()
        
        
        