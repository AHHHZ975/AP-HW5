from random import uniform
from statistics import mean

xLists = []
yLists = []

def isInCircle(x, y):
	if(x**2 + y**2 <= 0.25):
		return 1
	else:
		return 0

def generateRandomPoints(numberOfRandomPoints):	
	xLists.clear()
	yLists.clear()
	for i in range(numberOfRandomPoints):
		xLists.append(uniform(-0.5, 0.5))
	for i in range(numberOfRandomPoints):
		yLists.append(uniform(-0.5, 0.5))

def caculatePI(numberOfRandomPoints):
	pointsInCircleCount = 0
	generateRandomPoints(numberOfRandomPoints)
	for (index, value) in enumerate(range(numberOfRandomPoints)):		
		if isInCircle(xLists[index], yLists[index]):
			pointsInCircleCount += 1
	return 4*pointsInCircleCount/numberOfRandomPoints

def find():
	desiredCounter = 1
	calculatedPI = 0.0
	while abs(calculatedPI - 3.1) > 0.01:
		generateRandomPoints(desiredCounter)
		calculatedPI = caculatePI(desiredCounter)		
		desiredCounter += 1	
	return desiredCounter		

repeatNumber = int(input("Please enter the number of repeat:"))
counter = 0
caculatePIs = []

while counter < repeatNumber:
	caculatePIs.append(caculatePI(find()))
	counter += 1
print(mean(caculatePIs))
