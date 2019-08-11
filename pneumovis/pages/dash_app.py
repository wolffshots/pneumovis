# #these two lines and the part of the program that distinguishes it as a django-ised version of plotly
from django_plotly_dash import DjangoDash
app = DjangoDash('SimpleExample') # name can be changed but must then also be changed in the templates where it is called

# import dash
import dash_core_components as dcc
import dash_html_components as html
# import plotly.graph_objs as go
# import pandas as pd


# df = pd.read_excel(
#     "https://github.com/chris1610/pbpython/blob/master/data/salesfunnel.xlsx?raw=True")
# pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=[
#                     'Quantity'], aggfunc=sum, fill_value=0)

# trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
# trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
# trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
# trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')

# # app = dash.Dash() - remember to comment this line out so that the app var is correct for the server


# app.layout = html.Div(children=[
#     html.H1(children='Sales Funnel Report'),
#     html.Div(children='''National Sales Funnel Report.'''),
#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [trace1, trace2, trace3, trace4],
#             'layout':
#             go.Layout(title='Order Status by Customer', barmode='stack')
#         })
# ])
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
df.sort_values(['indexNumber'], ascending=[True], inplace=True)

subject = df['Serotype']
score = list(range(len(subject)))

data = [dict(
    type='bar',
    x=subject,
    y=score,
    text="""<a href="https://jadonwolffs.github.io/html-prototypes/strain.html">{}</a>""".format(
        "More Info"),
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
            tickvals=list(range(0, 100)),
            # currently, colorbar is based on no of colours which is at odds with serotype due to there being multiple letters for each number possible therefore values hardcoded
            ticktext=["0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
                      "-", "-", "-", "15", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "30", ]
        ),
        colorscale="Viridis"
    ),
    mode='markers',
    transforms=[dict(
        type='aggregate',
        groups=subject,
        aggregations=[dict(
            target='y', func='count', enabled=True)
        ]
    )]
)]

layout = dict(
    title='Serotype Colonisation Incidence',
    xaxis=go.layout.XAxis(title='Serotype', type='category',
                          rangeslider=dict(
                              visible=True
                          ),

                          ),
    yaxis=dict(title='Incidence', range=[0, 22]),
    updatemenus=[dict(
        x=0.85,
        y=1.15,
        xref='paper',
        yref='paper',
        yanchor='top',
        active=1,
        showactive=False
    )]
)


fig_dict = dict(data=data, layout=layout)

# pio.show(fig_dict, validate=False)
app.layout = html.Div(children=[
    html.H1(children=''),
    html.Div(children=''''''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout':layout#go.Layout(title='Order Status by Customer', barmode='stack')
        })
])
