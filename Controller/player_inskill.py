class PlayerInSkill:
    def __init__(self):
        '''
        gender: 
            0 = both, 1 = male, 2 = female
        levelIds: not required
            829 = Immortal, 828 = Mythical Honor, 1 = Mythical Glory, 2 = Mythic, 
            3 = Legend, 4 = Epic,5 = Grandmaster, 6 = Master,7 = Elite, 8 = Warrior
        newBie:
            0 = 
        order: 
            asc = from low to high, desc = from high to low, none (not required)
        page: 
            1 to end
        positionIds: 
            1 = Tank, 2 = Assasin, 3 = Marksman, 4 = Fighter, 5 = Mage, 6 = Support, 
            7 = Midlaner, 8 = All Role , 314 = Roamer
        rows:
            1 to 50
        skillId: 
            1 = Mobile Legends, 20 = Teman Curhat, 3 = PUBG, 2 = Free Fire, 100 = Ludo King, 
            139 = Eggy Party, 90 = Stumble Guys, 22 = Magic Chess, 21 = Valorant, 18 = COD: Mobile, 
            69 = Genshin Impact, 23 = Sausage Man, 87 = AoV, 10 = LOL: Wild Rift, 65 = Dota 2, 
            89 = Point Blank, 60 = CS2, 102 =  Black Desert Mobile, 103 = Sky : Children of the light, 
            109 = Supersus, 113 = Let's Get Rich, 122 = Teman Nyanyi
            
        sort:
            auditTime = Recenly Joined, None = Recomended, avgStar = Highest Rating,
            price = Price
        '''
        self.gender = 2
        self.levelIds = ""
        self.newBie = 0
        self.order = "desc"
        self.page = 1
        self.positionIds = ""
        self.rows = 50
        self.skillId = 1
        self.sort = "auditTime"

    def player_inskill_func(self):
        '''
        player inskill - list of players
        '''
        params_player_inskill = {
            "gender": self.gender,
            "levelIds": self.levelIds,
            "newBie": self.newBie,
            "order": self.order,
            "page": self.page,
            "positionIds": self.positionIds,
            "rows": self.rows,
            "skillId": self.skillId,
            "sort": self.sort
        }
        
        player_inskill = "player/inskill/batch?"  # endpoint
        player_inskill += "&".join([f"{key}={value}" for key, value in params_player_inskill.items()])
        
        return player_inskill