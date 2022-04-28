import json


class SaveData:
    def __init__(self, grid_object, player_object, object_list):
        self.grid_dat = grid_object
        self.player_dat = player_object
        self.object_dat = object_list


def save_on_file(game_data_path, json_string):
    f = open(game_data_path+"/save.json", 'w+')
    f.write(json_string)


def jsonify_game_data(game_data_path, grid_object, player_object):
    # f = open(game_data_path+"/save2.json", 'w+')
    # json.dump(grid_object.__dict__, f)
    # print(json.dumps(testList))
    return json.dumps(grid_object.__dict__)
