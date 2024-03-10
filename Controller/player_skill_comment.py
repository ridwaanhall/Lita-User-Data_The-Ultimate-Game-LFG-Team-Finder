class PlayerSkillComment:
    '''
    player skill comment
    '''
    def __init__(self, skillId, userId):
        '''
        player skill comment by SkillId and userId
        '''
        self.skillId = skillId
        self.userId = userId
        self.page = 1
        self.rows = 50
        
    def player_skill_comment_func(self):
        '''
        player skill comment
        '''
        params_player_skill_comment = {
            "skillId": self.skillId,
            "userId": self.userId,
            "page": self.page,
            "rows": self.rows
        }
        
        player_skill_comment = "player/skill/comment?"
        player_skill_comment += "&".join([f"{key}={value}" for key, value in params_player_skill_comment.items()])
        
        return player_skill_comment