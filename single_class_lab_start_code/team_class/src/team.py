class Team:
   
    def __init__(self,name,players,coach):
        self.name = name
        self.players = players
        self.coach = coach 
        self.points = 0
    def add_player(self,new_name):
        self.players.append(new_name)
    
    def has_player(self,player_name):
        if player_name  in self.players:
            return True
        else:
            return False    
    
    #(better way)return player_name in self.players
    
    def player_game(self,did_win):
        if did_win:
            self.point += 3  
            


    
    