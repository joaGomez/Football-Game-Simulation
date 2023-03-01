from enum import Enum
from Team import Team



class States(Enum):
    INIT, PLAYING, PAUSE, END = range(1, 5)         # INIT = 1, PLAYING = 2, PAUSE = 3, END = 4
    
    


class Game:
    def __init__(self, windowHeight, windowWidth, nPlayers):
        self.windowHeight = windowHeight    # Window size
        self.windowWidth = windowWidth      
        self.players = nPlayers             # Numbers of players in each team
        self.state = States.INIT.value      # Game state
        
        
        
        