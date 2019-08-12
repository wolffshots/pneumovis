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
# Add of a column areaaining a numbered version of the index
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
url = "bubble.csv"
dataset = pd.read_csv(url)

months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "11","12"]

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
fig_dict2["layout"]["xaxis"] = {"range": [0, 100], "title": "Patients Exposed to HIV (%)"}
fig_dict2["layout"]["yaxis"] = {"title": "Patients Exposed to Smoking (%)", "range": [0, 100]}
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
fig_dict2["layout"]["title"]="Effect of Smoking and HIV Exposure on Serotype Incidence in Clinic Areas"
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

#fig = go.Figure(fig_dict)


# pio.show(fig_dict, validate=False)
app.layout = html.Div(children=[
    html.H1(children=''),
    html.Div(children=''''''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout':layout#go.Layout(title='Order Status by Customer', barmode='stack')
        }),

        dcc.Graph(
            id='example-graph2',
            figure=fig_dict2
        )
])



#fig.show()
