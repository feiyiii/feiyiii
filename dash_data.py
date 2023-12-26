import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def generate_plot():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 2, 3]))
    return fig

app = dash.Dash(__name__)
app.layout = html.Div([

        html.Div([], className = 'col-2'), #Same as img width, allowing to have the title centrally aligned

        html.Div([
            html.H1(children='Performance Dashboard',
                    style = {'textAlign' : 'center'}
            )],
            className='col-8',
            style = {'padding-top' : '1%'}
        ),

        html.Div([
            html.Img(
                    src = app.get_asset_url('logo_001c.png'),
                    height = '43 px',
                    width = 'auto')
            ],
            className = 'col-2',
            style = {
                    'align-items': 'center',
                    'padding-top' : '1%',
                    'height' : 'auto'})

        ],
        className = 'row',
        style = {'height' : '4%',
                'background-color' : 'blue'}
        )

app.css.append_css(dict(external_url='index.html'))

if __name__ == '__main__':
    app.run_server(debug=True)