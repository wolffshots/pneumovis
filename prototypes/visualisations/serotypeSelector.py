import plotly.io as pio
import pandas as pd
from plotly import graph_objs as go
from plotly.graph_objs import *
from plotly.tools import FigureFactory as FF
import time
df = pd.DataFrame(pd.read_csv('swabs2.csv'))

# code below to order serotypes by group (number) - currently letters are still in wrong order, do additional sort
# Add of a column containing a numbered version of the index
df['indexNumber'] = [int(i[0:len(i)-1]) for i in df.Serotype]
# Perform sort of the rows
df.sort_values(['indexNumber'], ascending = [True], inplace = True)
# Deletion of the added column
#df.drop('indexNumber', 1, inplace = True)
subject=df['Serotype']
score=list(range(len(subject)))

# add more aggregate functions in future
# aggs = ["count"]
# agg = []
# agg_func=[]
# for i in range(0, len(aggs)):
#     agg = dict(
#         args=['transforms[0].aggregations[0].func', aggs[i]],
#         label=aggs[i],
#         method='restyle'
#     )
#     agg_func.append(agg)


    


# create and style individual bars
data = [dict(
  type = 'bar',
  x = subject,
  y = score,
  text="""<a href="https://google.com/">{}</a>""".format("More Info"),
  textposition='auto',
  textcolor="white",
  marker=dict(
    line=dict(
    width=2,
    color='black'),
    size=16,
    cmax=100,
    cmin=0,
    color=list(range(len(df['indexNumber']))),
    colorbar=dict(
        title="Serotype Groups",
        tickvals=list(range(0,100)),
        # currently, colorbar is based on no of colours which is at odds with serotype due to there being multiple letters for each number possible therefore values hardcoded
        ticktext=["0","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","15","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","30",]
    ),
    colorscale="Viridis"
),
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'count', enabled = True)
    ]
  )]
)]

layout = dict(
  title = 'Serotype Colonisation Incidence',
  xaxis = go.layout.XAxis(title = 'Serotype',type='category',
  rangeslider=dict(
    visible=True
   ),

),
  yaxis = dict(title = 'Incidence', range = [0,22]),
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

pio.show(fig_dict, validate=False)