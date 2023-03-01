from enum import Enum

class States(Enum):
    INIT, PLAYING, PAUSE, END = range(1, 5)
    
    


class Game:
    def __init__(self, window_height, window_width, n_players):
        self.window_height = window_height
        self.window_width = window_width
        self.players = n_players
        
        
        
        