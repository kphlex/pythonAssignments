players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]


class Player:
    
    def __init__(self,KUJO):
        self.name = KUJO["name"]
        self.age = KUJO["age"]
        self.position = KUJO["position"]
        self.team = KUJO["team"]
        
    def __repr__ (self):
        player_info = f"Player: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}"
        return player_info

    @classmethod
    def add_player(cls, data):
        new_team = []
        for new in data:
            new_team.append(cls(new))
        return new_team


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jasons = Player(jason)
player_kyrie = Player(kyrie)


print(player_kevin, player_jasons, player_kyrie)

