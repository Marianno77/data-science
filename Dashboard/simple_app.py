from http.cookiejar import debug

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H2(children='hello world!'),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=['A', 'B', 'C'],
                y=[5, 10, 15],
                name='first'
            ),
            go.Bar(
                x=['A', 'B', 'C'],
                y=[10, 20, 30],
                name='second'
            )
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)