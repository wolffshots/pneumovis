"""
The chart showing the origin of swab samples and their serotype
"""
print("Loading map")

import time
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *
from plotly import graph_objs as go
import pandas as pd
import plotly.io as pio
import dash_html_components as html
import dash_core_components as dcc
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output
import re
import collections

app = DjangoDash('map')



def map_load():
    
    # define app html layout
    app.layout = html.Div(style={'font-family':'sans-serif'},children=[
        html.H1(children=''),
        html.Div(children=''''''),

            html.P('Serotype:'),
            dcc.Dropdown(
                    id='serotype',
                    options= [{'label': str(item),'value': str(item)} for item in list(dict.fromkeys(newSerotypeList).keys())],
                    multi=True,
                    value=list(dict.fromkeys(newSerotypeList).keys())
                ),
                dcc.Graph(id='map-graph',
                            style={'margin-top': '20'}
                        )
    ])

map_data = pd.read_csv('static/data/mapSwabs.csv')
    #use sorting function by () to sort serotypes into correct "groups" based on numeric part of name, and then further into correct place in group based on suffix letter
def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

newSerotypeList=sorted_nicely(list(map_data["serotype"]))
map_data['serotype'] = pd.Categorical(map_data['serotype'], list(dict.fromkeys(newSerotypeList).keys()))
map_data=map_data.sort_values(by="serotype")

layout_map = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    title='Incidences of Penumococcus Colonisation in Cape Town',
    mapbox=dict(
        accesstoken="pk.eyJ1IjoiYWRvdXQxOTAyIiwiYSI6ImNqeXR1MXBwazA3OWMzbnJyZTk0eDVwNXgifQ.TEDKQZdJPxMTgK6dKGMvgA",
        style="dark",
        center=dict(
            lon=18.9963493347168,
            lat=-33.7013831274414
        ),
        zoom=11
    ),
    uirevision="constant"
)


# generate map with markers and more info on hover
def gen_map(map_data):
    # if map_data.empty:
    #     return {
    #     "data": [],
    #     "layout": layout_map
    # } dummy entry to deal with this case
    numColours=len(map_data.index)
    if map_data.empty:
        raise Exception("Empty dataframe")

    return {
        "data": [{
                "type": "scattermapbox",
                "lat": list(map_data['latitude']),
                "lon": list(map_data['longitude']),
                "hoverinfo": "text",
                "hovertext": [["Swab Barcode: {}<br>Serotype: {}<br>Latitude: {}<br>Longitude: {}".format(i,j,k,l)]
                                for i,j,k,l in zip(map_data['OBJECTID'],map_data["serotype"],map_data['latitude'],map_data['longitude'])],
                "mode": "markers",
                "name": list(map_data['OBJECTID']),
                "marker": {
                    "size": 6,
                    "opacity": 0.7,
                    "cmax":numColours,
                    "cmin":0,
                    "color":list(range(numColours)),
                    "colorscale":"Viridis"
                }
        }],
        "layout": layout_map
    }

# callback to update map based on serotype tags selected

@app.callback(
    Output('map-graph', "figure"),
    [Input('serotype', 'value')])
def updateMap(serotypeVals):

    if len(serotypeVals)==0:
        print("no tags selected")
        temp_df=map_data.loc[map_data['serotype']==" "] 

    else:
        temp_df=map_data.loc[map_data['serotype'].isin(serotypeVals)]    
    return gen_map(temp_df)
print("Finished loading map")

import threading
map_thread = threading.Thread(target=map_load, args=(), kwargs={})
map_thread.setDaemon(True)
map_thread.start()