from FetchURL.fetch_data import DataFetcher
from FetchURL.HandleResponse import HandleResponsePlayerInskill
from Controller.LitaController import PlayerInSkill, PlayerDetail, PlayerSkillComment, PlayerReceived, MomentUserList, Skills

'''
no = 18682745
id = 2190186
skills = Skills.skills_func() # list of skill
player_inskill = PlayerInSkill(gender, skillId, page).player_inskill_func() # list player in skill
player_detail = PlayerDetail(no).player_detail_func() # player detail
player_skill_comment = PlayerSkillComment(skillId, id, page).player_skill_comment_func() # list comment of player in skill
player_received = PlayerReceived(id).player_received_rank_total_func() # player received
moment_user_list = MomentUserList(id).moment_user_list_func() # moment user list (post)
'''

if __name__ == "__main__":
    gender = 2
    skillId = 1
    rows = 99
    
    for page in range(1, 2):  # Loop through pages 1 to 10
        player_inskill = PlayerInSkill(gender, skillId, page, rows).player_inskill_func()  # List player in skill

        data_fetcher = DataFetcher(player_inskill)
        data, status_code = data_fetcher.fetch_data()

        handle_response = HandleResponsePlayerInskill()
        response = handle_response.handle_data_func(data)
        print(response, status_code)
        

