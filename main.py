import json
import time
from GUI import DrawElevator
from Floor import Floor
from Person import Person
from Elevator import Elevator
        
def main():
    currentIndex = 0
    time_tick = 0
    cumulative_time = 0

    #reads from jsonfile
    with open('testcases/elevator_practice1.json') as json_data:
        jsonFile = json.load(json_data)

    #intializing floor and elevators
    numFloors = jsonFile["floors"]
    numElevators = jsonFile["elevators"]
    floorList = []
    elevatorList = []
    drawGui = DrawElevator(numFloors,numElevators)
    drawGui.initialDraw()

    for i in range(numFloors):
        floorList.append(Floor(i))
    for i in range(numElevators):
        elevatorList.append(Elevator(5,numFloors))


    while time_tick < 1000:
        #stores the data locally from the json object
        if time_tick == jsonFile["events"][currentIndex]["time"]:
            startFloor = jsonFile["events"][currentIndex]["start"]
            endFloor = jsonFile["events"][currentIndex]["end"]

            #populates the floor class
            new_person = Person(time_tick,startFloor,endFloor)
            floorList[startFloor].appendPerson(new_person)
            currentIndex += 1

        #updates the elevator class
        for elevator in elevatorList:
            floorList = elevator.update(floorList)

        drawGui.update(elevatorList,floorList)

        time_tick += 1
        time.sleep(0.1)


main()

