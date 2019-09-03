# #these two lines and the part of the program that distinguishes it as a django-ised version of plotly
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
# name can be changed but must then also be changed in the templates where it is called
app = DjangoDash('SimpleExample2')


# x axis variable options - if time, add CO2 exposure, stove type etc
available_xVars=["Patients Exposed to HIV (%)","Patients Exposed to Smoking (%)"]



# define app html layout
app.layout = html.Div(children=[
    html.H1(children=''),
    html.Div(children=''''''),

        dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_xVars],
                value="Patients Exposed to HIV (%)"
            ),

    dcc.Graph(
        id='environmental-factors',
        figure={}
        )

])



# get data for the bubble charts
url = "bubble.csv"
dataset = pd.read_csv(url)

# timeline of project
years = ["2012","2013","2014","2015","2016"]

# make list of ModeSerotypes to colour area according to 
serotypes = []
for serotype in dataset["ModeSerotype"]:
    if serotype not in serotypes:
        serotypes.append(serotype)
# template of dict to return

def makeFigure(xVar):
    fig_dict2 = {
    "data": [],
    "layout": {},
    "frames": []
    }
    #xvar: Smoking or HIV
    fig_dict2["layout"]["xaxis"] = {"range": [0, 100], "title": "Patients Exposed to "+xVar +"(%)"}
    fig_dict2["layout"]["yaxis"] = {"title": "Patients Colonised by Pneumococcus (%)", "range": [0, 100]}
    fig_dict2["layout"]["hovermode"] = "closest"
    fig_dict2["layout"]["sliders"] = {
        "args": [
            "transition", {
                "duration": 400,
                "easing": "cubic-in-out"
            }
        ],
        "initialValue": "1",
        "plotlycommand": "animate",
        "values": years,
        "visible": True
    }
    fig_dict2["layout"]["showlegend"]=True
    fig_dict2["layout"]["title"]="Effect of "+xVar+" Exposure on Serotype Incidence in Clinic Areas Mandalay and Gugulethu"
    fig_dict2["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 1000, "redraw": True},
                                    "fromcurrent": True, "transition": {"duration": 50,
                                                                        "easing": "quadratic-in-out"}}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True},
                                    "mode": "immediate",
                                    "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }
    ]
    # ensure slider has correct values 
    sliders_dict = {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Year of Project:",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": []
    }

    # make data
    year = 2012
    dfVar=xVar.lower()+"exposed"
    colours =  ["#ADCF3D", '#483D7A', '#287E8D', '#447877', '#AFCA3E', '#208D66', '#366B80']
    i=0
    for serotype in serotypes:
        dataset_by_year = dataset[dataset["year"] == year]
        dataset_by_year_and_area = dataset_by_year[
            dataset_by_year["ModeSerotype"] == serotype]

        data_dict = {
            "x": list(dataset_by_year_and_area[dfVar]),
            "y": list(dataset_by_year_and_area["PneumococcusExposed"]),
            "mode": "markers+text",
            "text": list(dataset_by_year_and_area["area"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 0.05,
                 "color":colours[i],
                "size": list(dataset_by_year_and_area["population"])
              
            },
            "name": "Mode Serotype in Area: "+serotype
        }
        fig_dict2["data"].append(data_dict)
        i+=1

    # make frames, each corresponds to a year
    for year in years:
        
        frame = {"data": [], "name": str(year)}
        colours =  ["#ADCF3D", '#483D7A', '#287E8D', '#447877', '#AFCA3E', '#208D66', '#366B80']
        i=0
        for serotype in serotypes:
            dataset_by_year = dataset[dataset["year"] == int(year)]
            dataset_by_year_and_area = dataset_by_year[
                dataset_by_year["ModeSerotype"] == serotype]

            data_dict = {
                "x": list(dataset_by_year_and_area[dfVar]),
                "y": list(dataset_by_year_and_area["PneumococcusExposed"]),
                "mode": "markers+text",
                "text": list(dataset_by_year_and_area["area"]),
                "marker": {
                    "sizemode": "area",
                    "sizeref": 0.05,
                    "color":colours[i],
                    "size": list(dataset_by_year_and_area["population"])
                },
                "name": "Mode Serotype in Area: "+serotype
            }
            frame["data"].append(data_dict)
            i+=1

        fig_dict2["frames"].append(frame)
        slider_step = {"args": [
            [year],
            {"frame": {"duration": 1000, "redraw": True},
            "mode": "immediate",
            "transition": {"duration": 50}}
        ],
            "label": year,
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)


    fig_dict2["layout"]["sliders"] = [sliders_dict]
    return (fig_dict2)   
        


# make figures - one per x variable
fig_dictSmoking = makeFigure("Smoking")
fig_dictHIV = makeFigure("HIV")



# Dropdown for Bubble Chart 

@app.callback(
    Output('environmental-factors', 'figure'),
    [Input('xaxis-column','value')]
)
def update_graph(xaxis_column_name):
    """ Replace x axis variable based on user choice and adjust figure accordingly"""
    
    if xaxis_column_name=="Patients Exposed to HIV (%)":
        returnFig=fig_dictHIV
        print("hiv chosen")
    elif xaxis_column_name=="Patients Exposed to Smoking (%)":
        returnFig=fig_dictSmoking
        print("smoking chosen")

    return(returnFig)

