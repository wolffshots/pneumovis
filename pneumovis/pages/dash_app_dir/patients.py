print("Loading patients") 

from plotly.graph_objs import *
import plotly.io as pio
import pandas as pd
from plotly import graph_objs as go
from plotly.graph_objs import *
import time
import re
import datetime
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

# General notes: I've only checked a few points to see if this works. One issue is that dots in the same year for the same patient overlap each othe
# this can be solved by offsetting them slightly or a better way would be for the Y axis to show the full date rather than just the year
# since every swab will have a diff day and none should overlap
# will upload dataset with full dates soon. If you need help with filtering dataframes or whatever check the other visualisations 
# minor things: more space between patients, order patients numerically 

app = DjangoDash('patients')

def patient_load():
    df = pd.DataFrame(pd.read_csv('static/data/patientData.csv'))
    # another dataframe to keep patient IDs without unicode symbols
    df2 = pd.DataFrame(pd.read_csv('static/data/patientData.csv'))

    for i in range(len(df)):
      if (df.loc[i, "HIVexposed"]==True):
        df.loc[i, "participant_id"]=df.loc[i, "participant_id"]+" "+'\U0001f397'

    for i in range(len(df)):
      if (df.loc[i, "sex"]=="Male"):
        df.loc[i, "participant_id"]=df.loc[i, "participant_id"]+" "+'\u2642'

    for i in range(len(df)):
      if (df.loc[i, "sex"]=="Female"):
        df.loc[i, "participant_id"]=df.loc[i, "participant_id"]+" "+'\u2640'

    for i in range(len(df)):
      if (df.loc[i, "DateVaccinated"]!=" "):
        df.loc[i, "participant_id"]=df.loc[i, "participant_id"]+" "+'\uD83D\uDC89'

    for i in range(len(df)):
      if (df.loc[i, "SmokingExposed"]=="True"):
        df.loc[i, "participant_id"]=df.loc[i, "participant_id"]+" "+'\uD83D\uDEAC'


    def gen_graph(dfName):
      trace1 = {
        "mode": "markers", 
        "type": "scatter", 
        "x": dfName["participant_id"], 
        "y": dfName["swabDate"],
      #   "hoverinfo": "text",
      #   "hovertext": [["participant_id: {}<br>Serotype: {}<br>Date: {}".format(i,j,k)]
      #                                 for i,j,k in zip(df2["participant_id"],df["serotype"],df["swabDate"])],
      #I think the above doesn't show up because the graph space is so small, fix somehow
        "name": "Date of Serotype Colonization",
      
      } #you would need to do this for every serotype present in the file using a loop. Make sure the x and y vals still correspond though 
      trace2 = {
        "mode": "markers", 
        "type": "scatter", 
        "x": dfName["participant_id"], 
        "y": dfName["DateVaccinated"],
        "name": "Vaccination Date"
      }

      return {
        "data" : [trace1, trace2],

        "layout": layout
      }



    layout = dict(
        title = 'Patient Timelines',
        yaxis = go.layout.YAxis(title = 'Year',type='date',range=['2011-01-01','2017-01-01']),
        xaxis = go.layout.XAxis(title = 'Patient',type='category',
        rangeslider=dict(
          visible=True
        )
        ),
        yaxis_range=[datetime.datetime(2012,1,1),
                                    datetime.datetime(2017,1,1)]
      )




    app.layout = html.Div(
        children=[
            html.H1("Filter patients by: "),
            # html.Div(children=''''''),
            dcc.Checklist(
            id='filter',
            options=[
              {'label': 'Male', 'value': 'Male'},
              {'label': 'Female', 'value': 'Female'}
             ],
            value=['Male', 'Female'],
            labelStyle={'display': 'inline-block'}
            ),
            dcc.Graph(
                id='patient-graph',
                figure={
                  
                }),

        ],
        style={'padding-bottom': '45%', 'height': 0},
    )


    @app.callback(
        Output('patient-graph', 'figure'),
        [Input('filter','value')]
    )
    def update_graph(filters):
        """ apply patient filters """
        
        temp_df=df.loc[df['sex'].isin(filters)]

        return gen_graph(temp_df)
    print("Finished loading patients")


import threading
patient_thread = threading.Thread(target=patient_load, args=(), kwargs={})
patient_thread.setDaemon(True)
patient_thread.start()