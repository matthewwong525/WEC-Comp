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
        self.num_people = 0
        # Directional Data (-1 = down, 0 = stop, 1 = up)
        self.direction = 0
        # State
        self.state = "stopped"

    def update(self, floors):
        floors_with_people = []
        State = Enum('State', 'stopped moving stopping')
        # Search for floors with people in the same direction
        for floor in floors:
            if floor.numPeople > 0:
                if self.direction > 0 and floor.floorNum >= self.current_floor:
                    floors_with_people.append(floor.floorNum)
                elif self.direction < 0 and floor.floorNum <= self.current_floor:
                    floors_with_people.append(floor.floorNum)
        for


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
