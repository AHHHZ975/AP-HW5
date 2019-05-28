from random import uniform

xLists = []
yLists = []

def isInCircle(x, y):
	if(x**2 + y**2 <= 0.25):
		return 1

	else:
		return 0

def generateRandomPoints(numberOfRandomPoints):	
	for i in range(numberOfRandomPoints):
		xLists.append(uniform(-0.5, 0.5))
	for i in range(numberOfRandomPoints):
		yLists.append(uniform(-0.5, 0.5))

def caculatePI():
	pointsInCircleCount = 0
	for (index, value) in enumerate(range(len(xLists))):		
		if isInCircle(xLists[index], yLists[index]):
			pointsInCircleCount += 1
	return pointsInCircleCount/(len(xLists)-pointsInCircleCount)

generateRandomPoints(10000)
print(caculatePI())