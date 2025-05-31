import plotly.express as px
import pandas as pd

import jsonController

class MapController:
    def __init__(self):
        pass
    
    def SetDataFromFile(self, fileName):
        self.dataFrame = pd.DataFrame(jsonController.Load(fileName))
        
    def SetData(self, Data):
        bufDF = []
        for cluster in Data:
            for station in cluster:
                bufDF.append(station)
                
        self.dataFrame = pd.DataFrame(bufDF)
            
    def Draw(self, mapHeight = 900, markerSize = 12, mapStyle = "open-street-map"):
        fig = px.scatter_mapbox(
            self.dataFrame,
            lat = "latitude",
            lon = "longitude",
            hover_name = "title",
            hover_data = ["yandex_code"],
            color = "clusterID", 
            zoom = 11,
            height = mapHeight
            )
        fig.update_traces(marker = dict(size = markerSize))
        fig.update_layout(mapbox_style = mapStyle)
        
        fig.write_html("maps/index.html")