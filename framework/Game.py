import os


class Game:
    def __init__(self):
        self.setup()

    def setup(self):
        myOS = os.name

        if myOS == 'posix':
            localAppDataPath = os.getenv('HOME')

            # Checks if Pytris folder exists
            if os.path.exists(localAppDataPath + "/.Pytris"):
                gameDataPath = localAppDataPath + "/.Pytris"

                # Checks if the screenshots folder exists
                if os.path.exists(gameDataPath + "/screenshots"):
                    pass
                else:
                    os.mkdir(gameDataPath + '/screenshots')

            else:
                os.mkdir(localAppDataPath + "/.Pytris")
                gameDataPath = localAppDataPath + "/.Pytris"
                os.mkdir(gameDataPath + '/screenshots')

        elif myOS == 'nt':
            localAppDataPath = os.getenv('LOCALAPPDATA')

            if os.path.exists(localAppDataPath + "/Pytris"):
                gameDataPath = localAppDataPath + "/Pytris"

                # Checks if the screenshots folder exists
                if os.path.exists(gameDataPath + "/screenshots"):
                    pass
                else:
                    os.mkdir(gameDataPath + '/screenshots')
            else:
                os.mkdir(localAppDataPath + "/Pytris")
                gameDataPath = localAppDataPath + "/Pytris"
                os.mkdir(gameDataPath + '/screenshots')
        else:
            localAppDataPath = '~/Library/Application Support'

            if os.path.exists(localAppDataPath + "/Pytris"):
                gameDataPath = localAppDataPath + "/Pytris"

                # Checks if the screenshots folder exists
                if os.path.exists(gameDataPath + "/screenshots"):
                    pass
                else:
                    os.mkdir(gameDataPath + '/screenshots')

            else:
                os.mkdir(localAppDataPath + "/Pytris")
                gameDataPath = localAppDataPath + "/Pytris"
                os.mkdir(gameDataPath + '/screenshots')

        self.gameDataPath = gameDataPath
