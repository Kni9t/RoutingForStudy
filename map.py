import plotly.express as px
import plotly.graph_objects as go
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
            
    def Draw(self, routeList = None, mapHeight = 900, markerSize = 12, mapStyle = "open-street-map"):
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
    
    def DrawNew(self, routeList = None, mapHeight = 900, markerSize = 12, mapStyle = "open-street-map"):
        fig = go.Figure()

        fig.add_trace(go.Scattermapbox(
            lat = self.dataFrame["latitude"],
            lon = self.dataFrame["longitude"],
            mode = "markers",
            marker = dict(size = markerSize),
            hovertext = self.dataFrame["title"],
            hoverinfo="text",
            name="Остановки",
            customdata = self.dataFrame[["yandex_code", "clusterID"]],
            hovertemplate = "<b>%{hovertext}</b><br>Код: %{customdata[0]}<br>Кластер: %{customdata[1]}"
        ))
        
        if routeList:
            colors = [
                    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
                    "#393b79", "#637939", "#8c6d31", "#843c39", "#7b4173",
                    "#3182bd", "#e6550d", "#31a354", "#756bb1", "#636363"
                    ]
            for idx, route in enumerate(routeList):
                lats = [stop["latitude"] for stop in route]
                lons = [stop["longitude"] for stop in route]
                titles = [stop["title"] for stop in route]

                fig.add_trace(go.Scattermapbox(
                    lat=lats,
                    lon=lons,
                    mode="lines+markers",
                    line=dict(width=3, color=colors[idx % len(colors)]),
                    marker=dict(size=6),
                    name=f"Маршрут {idx+1}",
                    text=titles,
                    hovertemplate="<b>%{text}</b><br>Широта: %{lat}<br>Долгота: %{lon}<extra></extra>"
                ))
                    
        fig.update_layout(
            mapbox_style = mapStyle,
            mapbox_zoom = 12,
            mapbox_center = dict(lat = self.dataFrame["latitude"].mean(),
                            lon = self.dataFrame["longitude"].mean()),
            height = mapHeight,
            margin = {"r": 0, "t": 30, "l": 0, "b": 0}
        )
        
        fig.write_html("maps/index.html")