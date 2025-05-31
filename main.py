# Нам необходимо построить оптимальные маршруты для заданного набора станций
from yandexAPI import YAAPI
from map import MapController
from routeController import RouteController
from server import MapServer
import jsonController

YAPI = YAAPI()
map = MapController()
routeController = RouteController()
server = MapServer()

fileName = 'params/StationList.json'

YAPI.saveAllStationList(fileName, 'Россия', 'Москва и Московская область', 'Люберцы')

clusters = routeController.Clustering(12, jsonController.Load(fileName))

map.SetData(clusters)
map.SetRouts(routeController.CreateRoute(clusters))
map.Draw()

server.Start()