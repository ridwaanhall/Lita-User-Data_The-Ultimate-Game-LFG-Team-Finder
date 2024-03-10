class PlayerReceived:
    '''
    Handles player-related operations such as gifts, ranks, and orders.
    '''
    def __init__(self, id):
        '''
        Initializes the player with the given id.
        '''
        self.id = id
        
    def _construct_url(self, endpoint):
        '''
        Constructs a URL with parameters for the given endpoint.
        '''
        params = {
            "id": self.id
        }
        url = f"player/received/{endpoint}?" + "&".join([f"{key}={value}" for key, value in params.items()])
        return url
    
    def player_received_gift_func(self):
        '''
        Returns the URL for player's received gifts.
        '''
        return self._construct_url("gift")
    
    def player_received_rank_total_func(self):
        '''
        Returns the URL for player's received total rank.
        '''
        return self._construct_url("rank/total")
    
    def player_received_rank_gift_func(self):
        '''
        Returns the URL for player's received rank gifts.
        '''
        return self._construct_url("rank/gift")
    
    def player_received_rank_order_func(self):
        '''
        Returns the URL for player's received rank orders.
        '''
        return self._construct_url("rank/order")
