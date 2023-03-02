from Game import *

if __name__ == '__main__':
    print("Project: FOOTBALL GAME SIMULATION")

    newGame = Game(800, 1200, 5)
    
    newGame.initTeams()
    
    
    newGame.initGame()
    
    while(newGame.state == States.RUN.value):
        newGame.clock.tick(60)
        newGame.update()
        newGame.render()
        
   
    newGame.endGame()
    
    