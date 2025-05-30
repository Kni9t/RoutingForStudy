import numpy as np
from haversine import haversine
from sklearn.cluster import KMeans

import jsonController

class RouteController:
    def __init__(self):
        self.points = None
    
    def SetPointArray(self, stationList):
        stationPoints = []
        
        for station in stationList:
            bufPoint = [station['longitude'], station['latitude']]
            stationPoints.append(bufPoint)
            
        self.points = np.array(stationPoints)

    def Haversine(self, Point1, Point2):
        return haversine((Point1['latitude'], Point1['longitude']), (Point2['latitude'], Point2['longitude']))
    
    def getKMeans(self, countRouts):
        if (self.points is None):
            return
        
        kmeans = KMeans(n_clusters = countRouts)
        labels = kmeans.fit_predict(self.points)

        routes = [[] for _ in range(countRouts)]
        for point, label in zip(self.points, labels):
            routes[label].append(point)
        
        return routes