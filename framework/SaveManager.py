import json
from json import JSONEncoder, JSONDecoder
from framework.BlockRandomizer import BlockRandomizer


class SaveData:
    def __init__(self, grid_obj=0, player_obj=0, obj_list=0, started=0):
        tmpRandomizer = BlockRandomizer()

        self.grid_dat = grid_obj
        self.player_dat = player_obj
        self.obj_dat = obj_list
        self.gameStarted = started

        if obj_list != 0:
            self.blockType_dat = tmpRandomizer.findBlockIndex(
                type(obj_list.currentBlock))
        else:
            self.blockType_dat = 0


class DataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class DataDecoder(JSONDecoder):
    pass


def load_file(game_data_file):
    f = open(game_data_file, 'r')
    saveDataDict = json.load(f)
    datRet = SaveData()
    datRet.__dict__ = saveDataDict
    return datRet.grid_dat, datRet.player_dat, datRet.obj_dat, datRet.blockType_dat, datRet.gameStarted


def save_on_file(game_data_path, json_string):
    f = open(game_data_path+"/save.json", 'w+')
    f.write(json_string)


def jsonify_game_data(game_data_path, grid_obj, player_obj, obj_list, started):
    # f = open(game_data_path+"/save2.json", 'w+')
    # json.dump(grid_object.__dict__, f)
    # print(json.dumps(testList))
    saveDat = SaveData(grid_obj, player_obj, obj_list, started)
    # print(json.dumps(saveDat, cls=DataEncoder, indent=4))
    return json.dumps(saveDat, cls=DataEncoder, indent=4)
