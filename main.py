# Нам необходимо построить оптимальные маршруты для заданного набора станций
from yandexAPI import YAAPI
from map import MapController
from routeController import RouteController
from haversine import haversine
from server import MapServer
import jsonController

YAPI = YAAPI()
Map = MapController()
routeController = RouteController()
server = MapServer()

fileName = 'params/MoscowStationList.json'

YAPI.saveAllStationList(fileName, 'Россия', 'Москва и Московская область', 'Люберцы')

Map.LoadDateForMap(fileName)
Map.Draw()

server.Start()