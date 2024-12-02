import dash
from dash import dcc, html
from sales_dashboard import get_sales_dashboard
from operations_dashboard import get_operations_dashboard
from inventory_dashboard import get_inventory_dashboard

# Initialize Dash App
app = dash.Dash(__name__)

# App Layout with Tabs
app.layout = html.Div([
    html.H1("Business Dashboards", style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Sales Dashboard', children=get_sales_dashboard()),
        dcc.Tab(label='Operations Dashboard', children=get_operations_dashboard()),
        dcc.Tab(label='Inventory Dashboard', children=get_inventory_dashboard()),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
