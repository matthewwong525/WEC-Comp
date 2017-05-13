'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import *


class DrawElevator:

	def __init__(self, numFloors, numElevators):
		self.pplElevText = []
		self.pplFloorText = []
		self.elevBox = []
		self.numFloors = numFloors
		self.numElevators = numElevators
		self.floorDist = 460 / self.numFloors
		
	
	def initialDraw(self):
		win = GraphWin('!!!EMMIES ELEVATOR!!!', 960, 550) # give title and dimensions
##		floorDist = 460 / numFloors
		elevDist = 800 / self.numElevators
		pplOnFloor = [0] * self.numFloors
		fontSize = int(300 / self.numFloors)
		if fontSize > 12:
			fontSize = 12
		Text(Point(30, 10), "Floors").draw(win)
		Text(Point(140, 10), "People on Floor").draw(win)
		Text(Point(70, 505), "People on Elevator").draw(win)
		Text(Point(50, 520), "Elevators").draw(win)
		
		for i in range(self.numFloors):
			floorText = Text(Point(10, 480 - i * self.floorDist), i)
			floorText.setSize(fontSize)
			self.pplFloorText.append(Text(Point(80, 480 - i * self.floorDist), pplOnFloor[i]))
			self.pplFloorText[i].setSize(fontSize)

			floorText.draw(win)
			self.pplFloorText[i].draw(win)
			
		for i in range(self.numElevators):
			pt = Point(150 + elevDist * i, 520)
			Text(pt, i).draw(win)
			ptX = pt.getX()
			ptY = pt.getY()
			self.pplElevText.append(Text(Point(ptX, ptY - 15), 0))
			self.elevBox.append(Rectangle(Point(ptX - 35, ptY - 35), Point(ptX + 20, ptY - 35 - self.floorDist / 5)))
			
			self.pplElevText[i].draw(win)
			self.elevBox[i].draw(win)
			
	def update(self, Elevators, Floors):
                elevCount = 0
                floorCount = 0
		for elevator in Elevators:
                        
			self.pplElevText[elevCount].setText(elevator.people.length)

                        pointList = self.elevBox.getPoints()
                        curY = pointList[0].getY()
                        targetY = 480 - elevator.current_floor * self.floorDist
                        dY = curY - targetY
                        self.elevBox[elevCount].move(0,dY)

			elevCount += 1
			

		for floor in Floors:
			self.pplFloorText[floorCount].setText(floor.personList.lengths)
                        floorCount += 1

	    
		
##    initialDraw()

def main():
	Draw = DrawElevator(10,10)
	Draw.initialDraw()
	Draw.update()


	

main()
		
			
