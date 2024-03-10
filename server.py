import os
import json
from datetime import datetime

from FetchURL.fetch_data import DataFetcher
from FetchURL.HandleResponse import HandleResponsePiS
from Controller.Lita import PlayerInSkill, PlayerDetail, PlayerSkillComment, PlayerReceived, MomentUserList, Skills

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
    rows = 50

    for page in range(1, 447):
        json_data = PlayerInSkill(gender, skillId, page, rows).player_inskill_func() # list player in skill

        data_fetcher = DataFetcher(json_data)
        data, status_code = data_fetcher.fetch_data()
        
        handle_response = HandleResponsePiS()
        response = handle_response.handle_data_func(data)
        
        response = json.dumps(response, indent=4)

        response_json = json.loads(response)

        if response_json['status'] != '0':
            print(f"Data not available for page {page}, stopping...")
            break

        folder_name = f'LitaData/Json/{skillId}/{gender}'
        os.makedirs(folder_name, exist_ok=True)

        current_date = datetime.now().strftime('%Y%m%d%H%M%S')

        page_number = f"{page:04}"

        filename = f"{page_number}_{current_date}.json"
        
        file_path = os.path.join(folder_name, filename)

        with open(file_path, 'w') as file:
            file.write(response)

        print(f"Response saved to: {file_path}, Status code: {status_code}")