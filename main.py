# Нам необходимо построить оптимальные маршруты для заданного набора станций
from yandexAPI import YAAPI
from map import MapController
from routeController import RouteController
from server import MapServer
import jsonController

import sys

YAPI = YAAPI()
map = MapController()
routeController = RouteController()
server = MapServer()

fileName = 'params/MoscowStationList.json'

YAPI.saveAllStationList(fileName, 'Россия', 'Москва и Московская область', 'Люберцы')

clusters = routeController.Clustering(7, jsonController.Load(fileName))

print (routeController.CreateRoute(clusters))

sys.exit(0)

map.SetData(clusters)

map.Draw()

server.Start()