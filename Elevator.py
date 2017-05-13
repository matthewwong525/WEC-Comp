# Kevin Liu WEC Elevator Code
import Floor
from enum import Enum

class Elevator:
    def __init__(self, max_people, max_floors):
        # Max data
        self.max_people = max_people
        self.max_floors = max_floors;
        # List data
        self.people = [] #People inside hold destination info
        self.floors = []
        # Current data
        self.current_floor = 0
        # Directional Data (-1 = down, 0 = stop, 1 = up)
        self.direction = 0
        # State
        self.state = 'stopped'
        self.mustWait = 0
        self.waitTime = 0

    def addPerson(self, person):
        if len(self.people) == self.max_people:
            return False
        else:
            self.people.append(person)
            return True

    def arrive(self):
        for person in self.people:
            if person.go_floor == self.current_floor:
                self.people.remove(person)
                self.state == 'stopping'
                self.mustWait = 10;
                self.waitTime = 0;

    def update(self, floors):
        print(floors)
        floors_with_people = []

        # Search for floors with people in the same direction
        for floor in floors:
            if len(floor.personList) > 0:
                if self.direction > 0 and floor.floorNum >= self.current_floor:
                    floors_with_people.append(floor.floorNum)
                elif self.direction < 0 and floor.floorNum <= self.current_floor:
                    floors_with_people.append(floor.floorNum)
                elif self.direction == 0:
                    floors_with_people.append(floor.floorNum)
        if len(floors_with_people) == 0 and len(self.people) == 0:
            self.state = 'stopped'
            return floors

        # If it is stopped, just look for the first floor with people, and set direction to that
        if self.state == 'stopped':
            if len(floors_with_people) != 0 and floors_with_people[0] > self.current_floor:
                self.direction = 1
                self.mustWait = 3 * abs(floors_with_people[0] - self.current_floor)
                self.state = 'moving'
            elif len(floors_with_people) != 0 and floors_with_people[0] < self.current_floor:
                self.direction = -1
                self.mustWait = 3 * abs(floors_with_people[0] - self.current_floor)
                self.state = 'moving'

        # Dont do anything if the elevator is moving
        if (self.state == 'moving' or self.state == 'stopping') and self.waitTime < self.mustWait:
            # Dont do anything if the elevator is in motion
            self.waitTime += 1
            return floors

        # If the elevator is moving and it has moved for 3 wait ticks
        if self.state == 'moving' and self.waitTime == self.mustWait:
            self.current_floor += int (self.mustWait * self.direction / 3)
            self.arrive()
            print(self.current_floor)
            self.addPerson(floors[self.current_floor].personList[0])
            self.state = 'stopped'
            floors[self.current_floor].deletePerson(1)
            return floors
        return floors
