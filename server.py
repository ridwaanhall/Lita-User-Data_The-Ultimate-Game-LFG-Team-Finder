from FetchURL.fetch_data import DataFetcher
from Controller.player_inskill import PlayerInSkill

if __name__ == "__main__":
    player_inskill = PlayerInSkill()
    data_fetcher = DataFetcher(player_inskill.player_inskill_func())
    data, status_code = data_fetcher.fetch_data()

    print(data)
