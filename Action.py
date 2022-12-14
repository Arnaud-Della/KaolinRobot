from enum import Enum
from random import randint
from random import choice
import os

class Rotation(Enum):
    N = 0
    E = 1
    S = 2
    W = 3
    def GetRotation(actualrotation,sens):
        if actualrotation == Rotation.N and sens == -1:
            return Rotation.W
        elif actualrotation ==  Rotation.W and sens == 1:
            return Rotation.N
        else:
            return Rotation(actualrotation.value + sens)

class Map:
    def __init__(self,filename) -> None:
        self.matriceMap = []
        self.file = open(filename,"r")
        code = self.file.readlines()
        self.file.close()
        for i in code:
            self.matriceMap.append(list(i.strip()))
    def printMap(self):
        #os.system("clear")
        print()
        for i in self.matriceMap:
            print("".join(i))

class RobotAction:
    def __init__(self):
        self.map = Map("map.txt")
        self.actions = []
        self.__InitPositionRotation()
    def __InitPositionRotation(self):
        self.rotation = choice(list(Rotation))
        while True:
            self.x = randint(0,len(self.map.matriceMap)-1)
            self.y = randint(0,len(self.map.matriceMap[0])-1)
            if self.map.matriceMap[self.x][self.y] != "X":
                break
        print(f"\nRotation = {self.rotation} ; x = {self.x} ; y = {self.y} ; Case = '{self.map.matriceMap[self.x][self.y]}'")
        self.oldCase = self.map.matriceMap[self.x][self.y]
        self.map.matriceMap[self.x][self.y] = "@"
        print("Init Map :")
        self.map.printMap()
    def MoveForward(self):
        if self.rotation == Rotation.E or self.rotation == Rotation.W:
            if (self.rotation == Rotation.E):
                if self.__IsPossibleToMoveHere(self.x,self.y+1):
                    self.__ChangePosition(self.x,self.y+1) 
                else:
                    print("Error")
            else:
                if self.__IsPossibleToMoveHere(self.x,self.y-1):
                    self.__ChangePosition(self.x,self.y-1)
                else:
                    print("Error")
        else:
            if (self.rotation == Rotation.N):
                if self.__IsPossibleToMoveHere(self.x-1,self.y):
                    self.__ChangePosition(self.x-1,self.y)
                else:
                    print("Error")
            else:
                if self.__IsPossibleToMoveHere(self.x+1,self.y):
                    self.__ChangePosition(self.x+1,self.y)
                else:
                    print("Error")
    def MoveBackward(self):
        if self.rotation == Rotation.E or self.rotation == Rotation.W:
            if (self.rotation == Rotation.E):
                if self.__IsPossibleToMoveHere(self.x,self.y-1):
                    self.__ChangePosition(self.x,self.y-1) 
                else:
                    print("Error")
            else:
                if self.__IsPossibleToMoveHere(self.x,self.y+1):
                    self.__ChangePosition(self.x,self.y+1)
                else:
                    print("Error")
        else:
            if (self.rotation == Rotation.N):
                if self.__IsPossibleToMoveHere(self.x+1,self.y):
                    self.__ChangePosition(self.x+1,self.y)
                else:
                    print("Error")
            else:
                if self.__IsPossibleToMoveHere(self.x-1,self.y):
                    self.__ChangePosition(self.x-1,self.y)
                else:
                    print("Error")
    def TurnLeft(self):
        self.rotation = Rotation.GetRotation(self.rotation,-1)
        print(f"\nRotation = {self.rotation}")
    def TurnRight(self):
        self.rotation = Rotation.GetRotation(self.rotation,1)
        print(f"\nRotation = {self.rotation}")
    def __IsPossibleToMoveHere(self,x,y):
        if x>=0 and x < len(self.map.matriceMap) and y>=0 and y < len(self.map.matriceMap[0]):
            if self.map.matriceMap[x][y] != "X":
                return True
        return False
    def AddAction(self,action):
        self.actions.append(action)
    def __ChangePosition(self,x,y):
        self.map.matriceMap[self.x][self.y] = self.oldCase
        self.x = x
        self.y = y
        self.oldCase = self.map.matriceMap[self.x][self.y]
        self.map.matriceMap[self.x][self.y] = "@"
        self.map.printMap()
    def Run(self):
        for action in self.actions:
            print("\n"+action.__name__)
            action(self)
    def Info(self):
        print(f"\nRotation = {self.rotation} ; x = {self.x} ; y = {self.y}")

Robot = RobotAction()
Robot.AddAction(RobotAction.MoveForward)
Robot.AddAction(RobotAction.MoveBackward)
Robot.AddAction(RobotAction.TurnRight)
Robot.AddAction(RobotAction.TurnLeft)
Robot.Run()