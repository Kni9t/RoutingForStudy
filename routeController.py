import numpy as np
from haversine import haversine
from sklearn.cluster import KMeans

import jsonController

class RouteController:
    def __init__(self):
        self.points = None

    def Haversine(self, Point1, Point2):
        return haversine((Point1['latitude'], Point1['longitude']), (Point2['latitude'], Point2['longitude']))
    
    def Clustering(self, clusterCount, stationList):
        stationPoints = []
        
        for station in stationList:
            bufPoint = [station['longitude'], station['latitude']]
            stationPoints.append(bufPoint)
            
        pointArray = np.array(stationPoints)
        
        kmeans = KMeans(n_clusters = clusterCount)
        clusters = kmeans.fit_predict(pointArray)
        
        for i in range(len(clusters)):
            stationList[i]['clusterID'] = int(clusters[i])
        
        return stationList
