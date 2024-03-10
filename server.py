from FetchURL.fetch_data import DataFetcher
from Controller.player_inskill import PlayerInSkill
from Controller.player_detail import PlayerDetail

if __name__ == "__main__":
    player_inskill = PlayerInSkill().player_inskill_func()
    player_detail  = PlayerDetail(18682745).player_detail_func()

    data_fetcher = DataFetcher(player_detail)
    data, status_code = data_fetcher.fetch_data()

    print(data)
