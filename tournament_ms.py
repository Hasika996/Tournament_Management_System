class Team :
    def __init__(self, name , players, score):
        self.name=name
        self.players=list(players)
        self.score=score
    def add_player(self,player_name):
        if player_name in self.players:
            return -1

        self.players.append(player_name)
        return 1
    def remove_player(self,player_name):
        if player_name not in self.players:
            return -1
        self.players.remove(player_name)
        return 1
    def get_total_players(self):
        return len(self.players)
class Tournament:
    def __init__(self):
        self.teams={}
    def create_team(self,name,players,score=0):
        if name in self.teams:
            return -1
        self.teams[name]=Team(name,players,score)
        return 1
    def update_score(self,name,match_result,point_per_win=3,points_per_loss=0,points_per_tie=1):
        if name not in self.teams:
            return -1
        res=["win","loss","tie"]
        if match_result not in res:
            return -1

        if match_result == "win":
            self.teams[name].score += 3
        if match_result == "tie":
            self.teams[name].score += 1
        if match_result == "loss":
            self.teams[name].score += 0

        return 1
    def get_leaderboard(self):
        ans=[]
        for name in self.teams:
            return sorted(
            ((t.name, t.score) for t in self.teams.values()),
            key=lambda x: (-x[1], x[0])
            )

    def get_team(self,name):
        return self.teams.get(name, None)
