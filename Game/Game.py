import os


class Game:
    def __init__(self):
        self.setup()

    def setup(self):
        myOS = os.name

        if myOS == 'posix':
            localAppDataPath = os.getenv('HOME')

            if os.path.exists(localAppDataPath + "/.Pytris"):
                gameDataPath = localAppDataPath + "/.Pytris"
            else:
                os.mkdir(localAppDataPath + "/.Pytris")
                gameDataPath = localAppDataPath + "/.Pytris"
                os.mkdir(gameDataPath + '/screenshots')

        elif myOS == 'nt':
            localAppDataPath = os.getenv('LOCALAPPDATA')

            if os.path.exists(localAppDataPath + "/Pytris"):
                gameDataPath = localAppDataPath + "/Pytris"
            else:
                os.mkdir(localAppDataPath + "/Pytris")
                gameDataPath = localAppDataPath + "/Pytris"
                os.mkdir(gameDataPath + '/screenshots')
        else:
            localAppDataPath = '~/Library/Application Support'

            if os.path.exists(localAppDataPath + "/Pytris"):
                gameDataPath = localAppDataPath + "/Pytris"
            else:
                os.mkdir(localAppDataPath + "/Pytris")
                gameDataPath = localAppDataPath + "/Pytris"
                os.mkdir(gameDataPath + '/screenshots')

        self.gameDataPath = gameDataPath
