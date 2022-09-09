from operator import index 
import random

class Player:
    def __init__(self, playerInfo):
        self.name = playerInfo["name"]
        self.age = playerInfo["age"]
        self.position = playerInfo["position"]
        self.team = playerInfo["team"]
    def reportInfo(self):
        print(f"{self.name}, {str(self.age)}, {self.position}, {self.team}")
    @classmethod
    def get_team(cls,teamList=[]):
        newList = []
        for x in teamList:
            newList.append(Player(x))
        return(newList)




pNames = ["Ken Jones", "Marmid Objewa", "Hank Smorm", "Taksashi Inchijo", "Apu Narmmass","Rick SPyder"]
pAges = [56, 44, 9, 23, 10, "old"]
pPositions = ["front", "leg", "hook", "foreman", "bootback"]
pTeams =["Rattlers","hungryjacks","The Fast Foods","Angry Gremblins","Thorny Bushes","Gobblers","Speeds"]
teamCol = [pNames, pAges, pPositions, pTeams]
pKeys = ["name","age","position","team"]


def makePlayer():
    currentPlayer = {}
    def rando(list1):
        randNum = random.randint(0,len(list1)-1)
        return(randNum)
    for x in pKeys:
        currentPlayer[x]=teamCol[pKeys.index(x)][rando(teamCol[pKeys.index(x)])]
    return(currentPlayer)

roster = []
roster.append(makePlayer())
roster.append(makePlayer())
roster.append(makePlayer())
roster.append(makePlayer())
roster.append(makePlayer())
print(roster)

theNewTeam = Player.get_team(roster)
for x in theNewTeam:
    x.reportInfo()


# objectRoster = []
# for x in roster:
#     objectRoster.append(Player(x))

# for x in objectRoster:
#     x.reportInfo()
