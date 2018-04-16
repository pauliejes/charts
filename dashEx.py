import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
	html.H1('Dash Practice'),
	dcc.Graph(id='example',
		figure ={
		'data': [
				{'x':[1,2,3,4,5], 'y':[6,7,8,9,2], 'type':'line', 'name':'Grapphin'},
				{'x':[3,4,8,3,4], 'y':[2,1,1,4,8], 'type':'line', 'name':'Numbers'},
				]
		})
	])

if __name__ == '__main__':
    app.run_server(debug=True)