from FetchURL.fetch_data import DataFetcher
from Controller.player_inskill import PlayerInSkill
from Controller.player_detail import PlayerDetail
from Controller.player_skill_comment import PlayerSkillComment

if __name__ == "__main__":
    player_inskill = PlayerInSkill().player_inskill_func()
    player_detail  = PlayerDetail(18682745).player_detail_func()
    player_skill_comment = PlayerSkillComment(1, 2190186).player_skill_comment_func()

    data_fetcher = DataFetcher(player_skill_comment)
    data, status_code = data_fetcher.fetch_data()

    print(data)
