import datetime
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# stock="TSLA"
app = dash.Dash()
app.layout = html.Div(
    children=[
        html.H1("Stock graph"),
        html.Div(
            '''
            Wow a stock graph!
            '''
        ),
        dcc.Input(id="input", value="TSLA", type="text"),
        html.Div(id="output-graph")
    ]
)
# way to add css file to the app
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


@app.callback(
    Output(component_id="output-graph", component_property="children"),
    [Input(component_id="input", component_property="value")]
)
def update_graph(stock):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(stock, "morningstar", start=start, end=end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)
    return dcc.Graph(
                id="example-graph",
                figure={
                    "data":[
                        {"x":df.index, "y":df.Close, "type":"line", "name":stock}
                    ],
                    "layout":{
                        "title":stock
                    }
                }
            )

   



if __name__ == "__main__":
    app.run_server(debug=True)
