import random
from framework.Block import Block


class BlockRandomizer:
    def __init__(self):
        LShapeBlockType = type(LShapedBlock(5, 0))
        SquareBlockType = type(SquareBlock(5, 0))
        FlippedLBlockType = type(FlippedLBlock(5, 0))
        LayedDownBlockType = type(LayedDownBlock(5, 0))
        VerticalBlockType = type(VerticalBlock(5, 0))
        AimDownLShapeType = type(AimDownLShape(5, 0))

        self.BlockTypes = []
        self.BlockTypes.append(LShapeBlockType)
        self.BlockTypes.append(SquareBlockType)
        self.BlockTypes.append(FlippedLBlockType)
        self.BlockTypes.append(LayedDownBlockType)
        self.BlockTypes.append(VerticalBlockType)
        self.BlockTypes.append(AimDownLShapeType)

    def getRandomBlock(self):
        randomBlockIndex = random.randint(0, len(self.BlockTypes) - 1)
        newObjectType = self.BlockTypes[randomBlockIndex]
        newObject = newObjectType(5, 0)
        return newObject

    def findBlockType(self, typeIndex):
        return self.BlockTypes[typeIndex]

    def findBlockIndex(self, BlockType):
        return self.BlockTypes.index(BlockType)


class SquareBlock(Block):
    def __init__(self, *args):
        super().__init__(*args)
        self.shape = [[True, True],
                      [True, True]]


class LShapedBlock(Block):
    def __init__(self, *args):
        super().__init__(*args)
        self.shape = [[True, False, False],
                      [True, True, True]]


class FlippedLBlock(Block):
    def __init__(self, *args):
        super().__init__(*args)
        self.shape = [[False, False, True],
                      [True, True, True]]


class LayedDownBlock(Block):
    def __init__(self, *args):
        super().__init__(*args)
        self.shape = [[True, True, True, True]]


class VerticalBlock(Block):
    def __init__(self, *args):
        super().__init__(*args)
        self.shape = [[True],
                      [True],
                      [True],
                      [True]]


class AimDownLShape(Block):
    def __init__(self, *args):
        super().__init__(*args)
        self.shape = [[True, True],
                      [False, True],
                      [False, True]]
