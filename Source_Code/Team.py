from Player import *




# CalculateYStartPos returns the starting position in Y axis for each player in the team
# according to the team distribution
def CalculateYStartPos(players):    
    screenHeight = SURFACE[1]
    startPos = list()
    
    for i in range(1, players+1):
        startPos.append(screenHeight + (i-players-1)*screenHeight/(players+1))
    
    return startPos
    



class Team:
    def __init__(self, name, teamID, teamDistribution, nPlayers, teamColor, badge):
        self.name = name            
        self.id = teamID            # Team´s ID
        self.color = teamColor
        self.badge = pygame.image.load(badge)        # Team´s badge
        self.players = list()       # List of players in the team
        
        
        xPos = 50
        for role in teamDistribution:
            startYPos = CalculateYStartPos(teamDistribution[role])          # List of positions for players with that role on the field
            
            for yPos in startYPos:
                self.players.append(Player((xPos, yPos), role))
            
            xPos += 150                         # Distance in x axis between roles
            