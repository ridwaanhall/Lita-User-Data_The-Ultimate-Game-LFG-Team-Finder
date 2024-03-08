from Lita.data_fetcher import DataFetcher
import json

if __name__ == "__main__":
    '''
    gender: 0 = both, 1 = male, 2 = female
    levelIds: 
    newBie:
    order: asc, desc, none (not filled)
    page: 1 to
    '''
    gender      = 2
    levelIds    = ""
    newBie      = 0
    order       = "desc"
    page        = 1
    positionIds = ""
    rows        = 30
    skillId     = 1
    sort        = "auditTime"
    
    params = {
        "gender": gender,
        "levelIds": levelIds,
        "newBie": newBie,
        "order": order,
        "page": page,
        "positionIds": positionIds,
        "rows": rows,
        "skillId": skillId,
        "sort": sort
    }
    
    endpoint = "player/inskill/batch?"
    endpoint += "&".join([f"{key}={value}" for key, value in params.items()])
    data_fetcher = DataFetcher(endpoint)
    data, status_code = data_fetcher.fetch_data()

    if data:
        prettified_data = json.dumps(data, indent=4, sort_keys=True)
        print("Status code:", status_code)
        # print(prettified_data)
        print(data)
