from enum import Enum
from random import randint

class Rotation(Enum):
    N = 0
    E = 1
    S = 3
    W = 4
    @classmethod
    def __eq__(cls, other):
        return cls.value == other

class Map:
    def __init__(self,filename) -> None:
        self.matriceMap = []
        self.file = open(filename,"r")
        code = self.file.readlines()
        self.file.close()
        for i in code:
            self.matriceMap.append(list(i.strip()))
        self.printMap()
    def printMap(self):
        for i in self.matriceMap:
            print("".join(i))

class RobotAction:
    def __init__(self):
        self.map = Map("map.txt")
        self.actions = []
        self.x = 0
        self.y = 0
        self.InitPositionRotation()
    def InitPositionRotation(self):
        while True:
            self.x = randint(0,len(self.map.matriceMap)-1)
            self.y = randint(0,len(self.map.matriceMap[0])-1)
            if self.map.matriceMap[self.x][self.y] != "X":
                break
        print(f"x = {self.x} ; y = {self.y} ; Case = '{self.map.matriceMap[self.x][self.y]}'")
    def MoveForward(self):
        print("Robot Move Forward")
    def MoveBackward(self):
        print("Robot Move Backward")
    def TurnLeft(self):
        print("Robot Turn Left")
    def TurnRight(self):
        print("Robot Turn Right")
    def AddAction(self,action):
        self.actions.append(action)
    def Run(self):
        for action in self.actions:
            action(self)

Robot = RobotAction()
Robot.AddAction(RobotAction.MoveForward)
Robot.AddAction(RobotAction.MoveBackward)
Robot.AddAction(RobotAction.TurnRight)
Robot.AddAction(RobotAction.TurnLeft)
Robot.Run()