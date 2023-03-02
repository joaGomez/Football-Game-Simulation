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
        
        pygame.init()                       # Inits graphic module
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))    # Sets screen size

        os.chdir('Images/')     # Sets current directory folder Images -> Upload images
        self.image = pygame.image.load('soccer-tactic-board.png')
        
        self.initTeams()
        
        
        
        os.chdir('../')         # Goes back to starter directory
        
    def initTeams(self):
        team0 = Team("Barcelona", 0, self.players, BLUE, BARCELONA_BADGE)        
        
        
        
        self.teams = [team0]
        
    def initGame(self):
        self.state = States.RUN.value
        self.window.fill(BLACK)
        self.clock = pygame.time.Clock()
        
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = States.END.value
    
    def renderMap(self):
        self.window.blit(self.image, (0,0))
                    
    def render(self):
        self.window.fill(BLACK)
        
        self.renderMap()
        
        pygame.display.flip()
    
    
        
    def endGame(self):
        pygame.quit()
        
    
        
        
        