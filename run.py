from Lita.data_fetcher import DataFetcher
import json

if __name__ == "__main__":
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
    
    '''
    player inskill
    '''
    gender      = 2
    levelIds    = ""
    newBie      = 0
    order       = "desc"
    page        = 1
    positionIds = ""
    rows        = 50
    skillId     = 1
    sort        = "auditTime"
    
    params_player_inskill = {
        "gender": gender,
        "levelIds": levelIds,
        "newBie": newBie,
        "order": order,
        "page": page,
        "positionIds": positionIds,
        "rows": rows,
        "skillId": skillId,
        "sort": sort
    }
    
    '''
    player detail
    '''
    no = 3582871
    
    '''
    player skill comment
    '''
    skillId = 1
    userId  = 2190186
    page    = 1
    rows    = 50
    
    params_player_skill_comment = {
        "skillId": skillId,
        "userId": userId,
        "page": page,
        "rows": rows
    }
    
    '''
    player received gift and player received rank
    '''
    id = 2190186
    
    '''
    moment user list
    '''
    authorId = id
    momentId = 0
    
    params_moment_user_list = {
        "authorId": authorId,
        "momentId": momentId
    }
    
    skill = "skill/"
    
    player_inskill = "player/inskill/batch?"
    
    player_detail = "player/detail/g3?"
    player_skill_comment = "player/skill/comment?"
    player_received_gift = "player/received/gift?"
    player_received_rank_total = "player/received/rank/total?"
    player_received_rank_gift = "player/received/rank/gift?"
    player_received_rank_order = "player/received/rank/order?"
    moment_user_list = "moment/user/list?"
    
    player_inskill += "&".join([f"{key}={value}" for key, value in params_player_inskill.items()])
    player_detail   = player_detail + "no=" + str(no)
    player_skill_comment += "&".join([f"{key}={value}" for key, value in params_player_skill_comment.items()])
    player_received_gift = player_received_gift + "id=" + str(id)
    player_received_rank_total = player_received_rank_total + "id=" + str(id)
    player_received_rank_gift = player_received_rank_gift + "id=" + str(id)
    player_received_rank_order = player_received_rank_order + "id=" + str(id)
    moment_user_list += "&".join([f"{key}={value}" for key, value in params_moment_user_list.items()])
    
    data_fetcher = DataFetcher(skill)
    
    data, status_code = data_fetcher.fetch_data()

    if data:
        # prettified_data = json.dumps(data, indent=4, sort_keys=True)
        print("Status code:", status_code)
        # print(prettified_data)
        print(data)
