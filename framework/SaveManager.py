import json
from json import JSONEncoder, JSONDecoder
from framework.BlockRandomizer import BlockRandomizer


class SaveData:
    def __init__(self, grid_object=0, player_object=0, object_list=0):
        tmpRandomizer = BlockRandomizer()

        self.grid_dat = grid_object
        self.player_dat = player_object
        self.object_dat = object_list

        if object_list != 0:
            self.blockType_dat = tmpRandomizer.findBlockIndex(
                type(object_list.currentBlock))
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
    dataReturn = SaveData()
    dataReturn.__dict__ = saveDataDict
    return dataReturn.grid_dat, dataReturn.player_dat, dataReturn.object_dat, dataReturn.blockType_dat


def save_on_file(game_data_path, json_string):
    f = open(game_data_path+"/save.json", 'w+')
    f.write(json_string)


def jsonify_game_data(game_data_path, grid_object, player_object, object_list):
    # f = open(game_data_path+"/save2.json", 'w+')
    # json.dump(grid_object.__dict__, f)
    # print(json.dumps(testList))
    saveDat = SaveData(grid_object, player_object, object_list)
    # print(json.dumps(saveDat, cls=DataEncoder, indent=4))
    return json.dumps(saveDat, cls=DataEncoder, indent=4)
