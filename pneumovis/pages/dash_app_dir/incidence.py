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

app = DjangoDash('SimpleExample')

df = pd.DataFrame(pd.read_csv('swabs2.csv'))
df.set_index('serotype', inplace=True)
#use sorting function by () to sort serotypes into correct "groups" based on numeric part of name, and then further into correct place in group based on suffix letter
def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


newSerotypeList=sorted_nicely(list(df.index.values))
print(newSerotypeList)

df=df.loc[newSerotypeList]

numColours=len(df.index)
data = [dict(
  type = 'bar',
  x = df.index,
  y = df['count'],
  text="""<a href="https://jadonwolffs.github.io/html-prototypes/strain.html">{}</a>""".format(
      "More Info"),
  textposition='auto',
  textcolor="white",
  marker=dict(
    line=dict(
    width=2,
    color='black'),
    size=16,
    cmax=numColours,
    cmin=0,
    color=list(range(numColours)),
    colorbar=dict(
        title="Serotypes",
        tickvals=list(range(numColours)),
        # currently, colorbar is based on no of colours which is at odds with serotype due to there being multiple letters for each number possible therefore values hardcoded
        ticktext=["0","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","15","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","30",]
    
    ),
    colorscale="Viridis"
),
  mode = 'markers',
)]

layout = dict(
  title = 'Serotype Colonisation Incidence',
  xaxis = go.layout.XAxis(title = 'Serotype',type='category',
  rangeslider=dict(
    visible=True
   ),

),
  yaxis = dict(title = 'Incidence', range = [0,600]),
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False
  )]
)




fig_dict = dict(data=data, layout=layout)


app.layout = html.Div(
    children=[
        html.H1(children=''),
        # html.Div(children=''''''),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': data,
                'layout': layout
            }),

    ],
    style={'padding-bottom': '45%', 'height': 0},
)