from Person import Person

class Floor():
    def __init__(self,floorNum):
        self.floorNum = floorNum
        self.personList = []

    def appendPerson(self,person):
        self.personList.append(person)

    def deletePerson(self,numPplDel):
        for i in range(numfPplDel):
            self.personList.popleft()