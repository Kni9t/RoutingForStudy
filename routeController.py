import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from haversine import haversine
from python_tsp.exact import solve_tsp_dynamic_programming

class RouteController:
    def __init__(self):
        self.points = None
    
    def SetPointArray(self, stationList):
        stationPoints = []
        
        for station in stationList:
            bufPoint = [station['latitude'], station['longitude']]
            stationPoints.append(bufPoint)
            
        self.points = np.array(stationPoints)

    def Haversine(self, Point1, Point2):
        return haversine((Point1['latitude'], Point1['longitude']), (Point2['latitude'], Point2['longitude']))
    
    def CreateDistMatrix(self, PointList):
        bufMatrix = []
        for i in range(len(PointList)):
            if (i == 0):
                continue
            bufMatrix.append(self.Haversine(PointList[i-1], PointList[i]))
        return bufMatrix