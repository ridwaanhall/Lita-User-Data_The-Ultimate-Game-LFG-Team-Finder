class PlayerReceived:
    '''
    player received
    '''
    def __init__(self, id):
        '''
        player received by id
        '''
        self.id = id
        
    def player_received_gift_func(self):
        '''
        player received gift
        '''
        params_player_received_gift = {
            "id": self.id
        }
        
        player_received_gift = "player/received/gift?"
        player_received_gift += "&".join([f"{key}={value}" for key, value in params_player_received_gift.items()])
        
        return player_received_gift
    
    def player_received_rank_total_func(self):
        '''
        player received rank total
        '''
        params_player_received_rank_total = {
            "id": self.id
        }
        
        player_received_rank_total = "player/received/rank/total?"
        player_received_rank_total += "&".join([f"{key}={value}" for key, value in params_player_received_rank_total.items()])
        
        return player_received_rank_total
    
    def player_received_rank_gift_func(self):
        '''
        player received rank gift
        '''
        params_player_received_rank_gift = {
            "id": self.id
        }
        
        player_received_rank_gift = "player/received/rank/gift?"
        player_received_rank_gift += "&".join([f"{key}={value}" for key, value in params_player_received_rank_gift.items()])
        
        return player_received_rank_gift
    
    def player_received_rank_order_func(self):
        '''
        player received rank order
        '''
        params_player_received_rank_order = {
            "id": self.id
        }
        
        player_received_rank_order = "player/received/rank/order?"
        player_received_rank_order += "&".join([f"{key}={value}" for key, value in params_player_received_rank_order.items()])
        
        return player_received_rank_order