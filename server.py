from FetchURL.fetch_data import DataFetcher

from Controller.LitaController import PlayerInSkill, PlayerDetail, PlayerSkillComment, PlayerReceived, MomentUserList, Skills

if __name__ == "__main__":
    skills = Skills.skills_func() # list of skill
    
    player_inskill = PlayerInSkill(2, 1, 1).player_inskill_func() # list player in skill
    player_detail = PlayerDetail(18682745).player_detail_func() # player detail
    player_skill_comment = PlayerSkillComment(1, 2190186).player_skill_comment_func() # list comment of player in skill
    
    player_received = PlayerReceived(11151425).player_received_rank_total_func() # player received
    
    moment_user_list = MomentUserList(2190186).moment_user_list_func() # moment user list (post)

    data_fetcher = DataFetcher(skills)
    data, status_code = data_fetcher.fetch_data()

    print(data, status_code)
