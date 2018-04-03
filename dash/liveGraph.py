import dash
from dash.dependencies import Output, Event
import dash_core_components as core
import dash_html_components as html
import plotly
import random
from plotly import graph_objs
from collections import deque

# sample data which will be replace by real queueing database like redis or memcache
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        core.Graph(id="live-graph", animate=True),
        core.Interval(id="graph-update", interval=1*1000)
    ]
)

@app.callback(Output("live-graph", "figure"),events=[Event("graph-update", "interval")])
def update_graph_scatter():
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1, 0.1))

    data = graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name="Scatter",
        mode="lines+markers"
    )

    core.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 
                'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )

    return {"data":[data], 
        "layout":graph_objs.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis=dict(range=[min(Y),max(Y)]))
        }

if __name__=="__main__":
    app.run_server(debug=True)
