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
            if person.dest == self.current_floor:
                self.people.remove(person)

    def update(self, floors):
        floors_with_people = []

        # Search for floors with people in the same direction
        for floor in floors:
            if floor.numPeople > 0:
                if self.direction > 0 and floor.floorNum >= self.current_floor:
                    floors_with_people.append(floor.floorNum)
                elif self.direction < 0 and floor.floorNum <= self.current_floor:
                    floors_with_people.append(floor.floorNum)
                elif self.direction == 0:
                    floors_with_people.append(floor.floorNum)
        if len(floors_with_people) == 0 and len(self.people) == 0:
            self.state = 'stopped'

        if self.state == 'stopped':
            if floors_with_people[0] > self.current_floor:
                self.direction = 1;
            elif floors_with_people < self.current_floor:
                self.direction = -1;


        if (self.state == 'moving' or self.state == 'stopping') and self.waitTime < self.mustWait:
            # Dont do anything if the elevator is in motion
            self.waitTime += 1
            return
        # If the elevator is moving and it has moved for 3 ticks
        if self.state == 'moving' and self.waitTime == self.mustWait:
            self.current_floor += self.mustWait * self.direction / 3

        for person in self.people:

        if self.direction == 0:  # Stopped
            for floor in floors_with_people:
                # Get the next floor
                self.arrive()
