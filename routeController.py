import numpy as np
from haversine import haversine
from sklearn.cluster import KMeans

class RouteController:
    def __init__(self):
        self.points = None

    def Haversine(self, Point1, Point2):
        return haversine((Point1['latitude'], Point1['longitude']), (Point2['latitude'], Point2['longitude']))
    
    def Clustering(self, clusterCount, stationList):
        clustersList = []
        
        bufPoints = []
        for station in stationList:
            bufPoint = [station['longitude'], station['latitude']]
            bufPoints.append(bufPoint)
            
        pointArray = np.array(bufPoints)
        
        kmeans = KMeans(n_clusters = clusterCount)
        clusters = kmeans.fit_predict(pointArray)
        
        for i in range(len(clusters)):
            stationList[i]['clusterID'] = int(clusters[i])
            
        for clusterID in range(clusterCount):
            bufCluster = []
            
            for station in stationList:
                if(station['clusterID'] == clusterID):
                    bufCluster.append(station)
            
            clustersList.append(bufCluster)
                    
        return clustersList

    def CreateDistanceMatrix(self, stationList):
        matrix = []
        
        for i in range(len(stationList)):
            bufLine = []
            
            for j in range(len(stationList)):
                if (i == j):
                    bufLine.append(0)
                else:
                    bufLine.append(self.Haversine(stationList[i], stationList[j]))
            
            matrix.append(bufLine)
            
        return matrix
    
    def greedy_tsp(self, matrix):
        n = len(matrix)
        visited = [False] * n
        path = [0]
        visited[0] = True

        for _ in range(n - 1):
            last = path[-1]
            min_dist = float('inf')
            next_city = -1

            for j in range(n):
                if not visited[j] and matrix[last][j] < min_dist:
                    min_dist = matrix[last][j]
                    next_city = j

            path.append(next_city)
            visited[next_city] = True

        # path.append(0)  # Вернуться в начало
        return path
            

    def CreateRoute(self, stationList):
        routeList = []
        
        for cluster in stationList:
            routeIDList = self.greedy_tsp(self.CreateDistanceMatrix(cluster))
            
            bufRoute = []
            for i in range(len(routeIDList)):
                # Вернуться в начало
                # if (i == len(cluster)):
                #     bufRoute.append(cluster[routeIDList[0]])
                # else:
                #     bufRoute.append(cluster[routeIDList[i]])
                bufRoute.append(cluster[routeIDList[i]])
            
            routeList.append(bufRoute)
        
        return routeList