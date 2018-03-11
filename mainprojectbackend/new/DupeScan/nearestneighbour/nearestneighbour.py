import operator 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1      #Length of numerical string
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)   #Euclidean distance calculation
		distances.append((trainingSet[x], dist))                         
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])               #Nearest neighbourhood interpolation calculation
	return neighbors


