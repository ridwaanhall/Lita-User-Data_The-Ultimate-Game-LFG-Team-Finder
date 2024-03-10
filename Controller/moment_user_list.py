class MomentUserList:
    '''
    moment User List
    '''
    def __init__(self, authorId):
        '''
        Initializes the player with the given id.
        authorId = id.
        '''
        self.authorId = authorId
        self.momentId = 0
        
    def moment_user_list_func(self):
        '''
        
        '''
        params_moment_user_list = {
            "authorId": self.authorId,
            "momentId": self.momentId
        }
        
        moment_user_list = "moment/user/list?"
        moment_user_list += "&".join([f"{key}={value}" for key, value in params_moment_user_list.items()])
        
        return moment_user_list