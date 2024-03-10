from FetchURL.fetch_data import DataFetcher

from Controller.PlayerController import PlayerInSkill, PlayerDetail, PlayerSkillComment, PlayerReceived, MomentUserList

if __name__ == "__main__":
    player_inskill = PlayerInSkill(2, 1, 1).player_inskill_func()
    player_detail = PlayerDetail(18682745).player_detail_func()
    player_skill_comment = PlayerSkillComment(1, 2190186).player_skill_comment_func()
    
    player_received = PlayerReceived(11151425).player_received_rank_total_func()
    
    moment_user_list = MomentUserList(2190186).moment_user_list_func()

    data_fetcher = DataFetcher(moment_user_list)
    data, status_code = data_fetcher.fetch_data()

    print(status_code)
