import time
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *
from plotly import graph_objs as go
import pandas as pd
import plotly.io as pio
import dash_html_components as html
import dash_core_components as dcc
from django_plotly_dash import DjangoDash

app2 = DjangoDash('SimpleExample2')
url = "bubble.csv"
dataset = pd.read_csv(url)

months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12"]

# make list of ModeSerotypes
serotypes = []
for serotype in dataset["ModeSerotype"]:
    if serotype not in serotypes:
        serotypes.append(serotype)
# make figure
fig_dict2 = {
    "data": [],
    "layout": {},
    "frames": []
}

# fill in most of layout
fig_dict2["layout"]["xaxis"] = {
    "range": [0, 100], "title": "Patients Exposed to HIV (%)"}
fig_dict2["layout"]["yaxis"] = {
    "title": "Patients Exposed to Smoking (%)", "range": [0, 100]}
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
    "values": months,
    "visible": True
}
fig_dict2["layout"]["title"] = "Effect of Smoking and HIV Exposure on Serotype Incidence in Clinic Areas"
fig_dict2["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 500, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
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
        "prefix": "Month of Project:",
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
month = 1
for serotype in serotypes:
    dataset_by_month = dataset[dataset["month"] == month]
    dataset_by_month_and_area = dataset_by_month[
        dataset_by_month["ModeSerotype"] == serotype]

    data_dict = {
        "x": list(dataset_by_month_and_area["SmokingExposure"]),
        "y": list(dataset_by_month_and_area["HIVExposure"]),
        "mode": "markers",
        "text": list(dataset_by_month_and_area["area"]),
        "marker": {
            "sizemode": "area",
            "sizeref": 500,
            "size": list(dataset_by_month_and_area["pop"])
        },
        "name": "Mode Serotype in Area: "+serotype
    }
    fig_dict2["data"].append(data_dict)

# make frames, each corresponds to a month
for month in months:
    frame = {"data": [], "name": str(month)}
    for serotype in serotypes:
        dataset_by_month = dataset[dataset["month"] == int(month)]
        dataset_by_month_and_area = dataset_by_month[
            dataset_by_month["ModeSerotype"] == serotype]

        data_dict = {
            "x": list(dataset_by_month_and_area["SmokingExposure"]),
            "y": list(dataset_by_month_and_area["HIVExposure"]),
            "mode": "markers",
            "text": list(dataset_by_month_and_area["area"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 500,
                "size": list(dataset_by_month_and_area["pop"])
            },
            "name": serotype
        }
        frame["data"].append(data_dict)

    fig_dict2["frames"].append(frame)
    slider_step = {"args": [
        [month],
        {"frame": {"duration": 300, "redraw": False},
         "mode": "immediate",
         "transition": {"duration": 300}}
    ],
        "label": month,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)


fig_dict2["layout"]["sliders"] = [sliders_dict]

app2.layout = html.Div(children=[
    html.H1(children=''),
    html.Div(children=''''''),

    dcc.Graph(
        id='example-graph2',
        figure=fig_dict2
    )
])