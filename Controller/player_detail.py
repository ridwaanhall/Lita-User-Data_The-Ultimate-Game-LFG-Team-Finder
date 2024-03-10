class PlayerDetail:
    '''
    player detail
    '''
    def __init__(self, no):
        self.no = no
    
    def player_detail_func(self):
        '''
        player detail by no
        '''
        params_player_detail = {
            "no": self.no
        }
        
        player_detail = "player/detail/g3?"
        player_detail += "&".join([f"{key}={value}" for key, value in params_player_detail.items()])
        
        return player_detail
