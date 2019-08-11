import plotly.graph_objects as go

import pandas as pd

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
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}

# fill in most of layout
fig_dict["layout"]["xaxis"] = {"range": [0, 100], "title": "Patients Exposed to HIV (%)"}
fig_dict["layout"]["yaxis"] = {"title": "Patients Exposed to Smoking (%)", "range": [0, 100]}
fig_dict["layout"]["hovermode"] = "closest"
fig_dict["layout"]["sliders"] = {
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
fig_dict["layout"]["title"]="Effect of Smoking and HIV Exposure on Serotype Incidence in Clinic Areas"
fig_dict["layout"]["updatemenus"] = [
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
    dataset_by_year = dataset[dataset["year"] == month]
    dataset_by_year_and_cont = dataset_by_year[
        dataset_by_year["ModeSerotype"] == serotype]

    data_dict = {
        "x": list(dataset_by_year_and_cont["SmokingExposure"]),
        "y": list(dataset_by_year_and_cont["HIVExposure"]),
        "mode": "markers",
        "text": list(dataset_by_year_and_cont["area"]),
        "marker": {
            "sizemode": "area",
            "sizeref": 500,
            "size": list(dataset_by_year_and_cont["pop"])
        },
        "name": "Mode Serotype in Area: "+serotype
    }
    fig_dict["data"].append(data_dict)

# make frames, each corresponds to a month
for month in months:
    frame = {"data": [], "name": str(month)}
    for serotype in serotypes:
        dataset_by_year = dataset[dataset["year"] == int(month)]
        dataset_by_year_and_cont = dataset_by_year[
            dataset_by_year["ModeSerotype"] == serotype]

        data_dict = {
            "x": list(dataset_by_year_and_cont["SmokingExposure"]),
            "y": list(dataset_by_year_and_cont["HIVExposure"]),
            "mode": "markers",
            "text": list(dataset_by_year_and_cont["area"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 500,
                "size": list(dataset_by_year_and_cont["pop"])
            },
            "name": serotype
        }
        frame["data"].append(data_dict)

    fig_dict["frames"].append(frame)
    slider_step = {"args": [
        [month],
        {"frame": {"duration": 300, "redraw": False},
         "mode": "immediate",
         "transition": {"duration": 300}}
    ],
        "label": month,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)


fig_dict["layout"]["sliders"] = [sliders_dict]

fig = go.Figure(fig_dict)

fig.show()