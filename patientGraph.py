from plotly.graph_objs import *
import plotly.io as pio
import pandas as pd
from plotly import graph_objs as go
from plotly.graph_objs import *
import time
import re
import datetime

# General notes: I've only checked a few points to see if this works. One issue is that dots in the same year for the same patient overlap each othe
# this can be solved by offsetting them slightly or a better way would be for the Y axis to show the full date rather than just the year
# since every swab will have a diff day and none should overlap
# will upload dataset with full dates soon. If you need help with filtering dataframes or whatever check the other visualisations 
# minor things: more space between patients, order patients numerically 


df = pd.DataFrame(pd.read_csv('patientData.csv'))


trace1 = {
  "mode": "markers", 
  "type": "scatter", 
  "x": df["participant_id"], 
  "y": df["swabDate"],
  "hoverinfo": "text",
  "hovertext": [["partcipant_id: {}<br>Serotype: {}".format(i,j)]
                                for i,j in zip(df['participant_id'],df["serotype"])],
  "name": "Date of Serotype Colonization"
} #you would need to do this for every serotype present in the file using a loop. Make sure the x and y vals still correspond though 
trace2 = {
  "mode": "markers", 
  "type": "scatter", 
  "x": df["participant_id"], 
  "y": df["DateVaccinated"],
  "name": "Vaccination Date"
}
data = Data([trace1, trace2])
layout = dict(
  title = 'Patient Timelines',
  yaxis = go.layout.YAxis(title = 'Year',type='date',range=(2011,2017)),
  xaxis = go.layout.XAxis(title = 'Patient',type='category',
  rangeslider=dict(
    visible=True
   )
  ),
  yaxis_range=[datetime.datetime(2012,1,1),
                               datetime.datetime(2017,1,1)]
)
fig = Figure(data=data, layout=layout)


pio.show(fig, validate=False)