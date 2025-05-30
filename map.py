import plotly.express as px
import pandas as pd
import json

import jsonController

class MapController:
    def __init__(self):
        pass
    
    def LoadDateForMap(self, fileName):
        self.dataFrame = pd.DataFrame(jsonController.Load(fileName))
            
    def Draw(self, mapHeight = 900, markerSize = 12, mapStyle = "open-street-map"):
        fig = px.scatter_mapbox(
            self.dataFrame,
            lat = "latitude",
            lon = "longitude",
            hover_name = "title",
            hover_data = ["yandex_code"],
            color = "transport_type", 
            zoom = 10,
            height = mapHeight
            )
        fig.update_traces(marker = dict(size = markerSize))
        fig.update_layout(mapbox_style = mapStyle)
        
        fig.write_html("maps/index.html")