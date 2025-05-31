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

fileName = 'params/MoscowStationList.json'

YAPI.saveAllStationList(fileName, 'Россия', 'Москва и Московская область', 'Видное')

clusters = routeController.Clustering(10, jsonController.Load(fileName))

map.SetData(clusters)
map.DrawNew(routeController.CreateRoute(clusters))

server.Start()