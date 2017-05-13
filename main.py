import json
import time
from Floor import Floor
#from Elevator import Elevator
        
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

    for i in range(numFloors):
        floorList.append(Floor(i))
    for i in range(numElevators):
        elevatorList.append("LOL")

    print(floorList[0])

    while time_tick < 1000:
        #stores the data locally from the json object
        if time_tick == jsonFile["events"][currentIndex]["time"]:
            startFloor = jsonFile["events"][currentIndex]["start"]
            endFloor = jsonFile["events"][currentIndex]["end"]

            #adds to floor class
            #floorList[startFloor-1].appendPerson()
            
            #updates the current states in here
            #print(time_tick)


            currentIndex += 1
        time_tick += 1
        #time.sleep(1)


main()

