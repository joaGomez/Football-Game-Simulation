from Player import *

class Team:
    def __init__(self, name, teamID, nPlayers, teamColor, badge):
        self.name = name
        self.id = teamID
        self.players = nPlayers
        self.color = teamColor
        self.badge = badge
        
        