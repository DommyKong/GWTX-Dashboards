from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Example Data for Sales
sales_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "HL_Sales_Volume": [500, 600, 550, 700, 750, 800],
    "SL_Sales_Volume": [400, 450, 480, 600, 650, 700],
    "HL_Revenue": [5000, 6000, 5500, 7000, 7500, 8000],
    "SL_Revenue": [4000, 4500, 4800, 6000, 6500, 7000],
    "HL_Inventory_Available": [1000, 1100, 1050, 1200, 1250, 1300],
    "SL_Inventory_Available": [900, 950, 970, 1100, 1150, 1200],
    "Best_Selling_Items": {"HL": "Kitchenware", "SL": "Winter Jackets"},
    "Revenue_Growth_Rate": {"HL": 10, "SL": 12},  # Monthly Growth Rate (%)
    "Avg_Revenue_Per_Item": {"HL": 12, "SL": 10},  # Revenue / Items Sold
    "Gross_Margin": {"HL": 3000, "SL": 2500},  # Revenue - COGS
    "ATV": {"HL": 35, "SL": 30},  # Revenue / Transactions
    "Channel_Revenue": {"In-Store": 10000, "Online": 5000},  # Split by Channel
    "Revenue_Per_Employee": {"HL": 2000, "SL": 1800},  # Revenue / Employees
}

# Calculate Sell-Through Rate (STR) for HL and SL
sales_data["HL_STR"] = [(sales_data["HL_Sales_Volume"][i] / sales_data["HL_Inventory_Available"][i]) * 100 for i in range(len(sales_data["Month"]))]
sales_data["SL_STR"] = [(sales_data["SL_Sales_Volume"][i] / sales_data["SL_Inventory_Available"][i]) * 100 for i in range(len(sales_data["Month"]))]

# Convert Data to DataFrame
sales_df = pd.DataFrame({
    "Month": sales_data["Month"],
    "HL_Sales_Volume": sales_data["HL_Sales_Volume"],
    "SL_Sales_Volume": sales_data["SL_Sales_Volume"],
    "HL_Revenue": sales_data["HL_Revenue"],
    "SL_Revenue": sales_data["SL_Revenue"],
    "HL_STR": sales_data["HL_STR"],
    "SL_STR": sales_data["SL_STR"],
})

def get_sales_dashboard():
    return html.Div([
        html.H1("Sales Dashboard", style={'textAlign': 'center'}),

        # Monthly Sales Volume (HL vs SL)
        dcc.Graph(
            id='sales-volume',
            figure={
                'data': [
                    go.Scatter(x=sales_df["Month"], y=sales_df["HL_Sales_Volume"], mode='lines+markers', name='HL'),
                    go.Scatter(x=sales_df["Month"], y=sales_df["SL_Sales_Volume"], mode='lines+markers', name='SL'),
                ],
                'layout': go.Layout(
                    title="Monthly Sales Volume: HL vs. SL",
                    xaxis={'title': 'Month'},
                    yaxis={'title': 'Sales Volume'}
                )
            }
        ),

        # Sell-Through Rate (STR)
        dcc.Graph(
            id='sell-through-rate',
            figure={
                'data': [
                    go.Bar(name='HL STR', x=sales_df["Month"], y=sales_df["HL_STR"], marker_color='blue'),
                    go.Bar(name='SL STR', x=sales_df["Month"], y=sales_df["SL_STR"], marker_color='orange'),
                ],
                'layout': go.Layout(
                    title="Sell-Through Rate (STR): HL vs. SL",
                    barmode='stack',
                    xaxis={'title': 'Month'},
                    yaxis={'title': 'Sell-Through Rate (%)'}
                )
            }
        ),

        # Monthly Revenue Comparison
        dcc.Graph(
            id='revenue-comparison',
            figure={
                'data': [
                    go.Bar(name='HL Revenue', x=sales_df["Month"], y=sales_df["HL_Revenue"], marker_color='blue'),
                    go.Bar(name='SL Revenue', x=sales_df["Month"], y=sales_df["SL_Revenue"], marker_color='orange'),
                ],
                'layout': go.Layout(
                    title="Monthly Revenue Comparison: HL vs. SL",
                    barmode='group',
                    xaxis={'title': 'Month'},
                    yaxis={'title': 'Revenue ($)'}
                )
            }
        ),

        # Best-Selling Items
        html.Div([
            html.H3("Best-Selling Items by Category"),
            html.P(f"HL: {sales_data['Best_Selling_Items']['HL']}"),
            html.P(f"SL: {sales_data['Best_Selling_Items']['SL']}"),
        ], style={'textAlign': 'center', 'margin': '20px'}),

        # Revenue Growth Rate
        dcc.Graph(
            id='revenue-growth-rate',
            figure={
                'data': [
                    go.Bar(x=["HL", "SL"], y=[sales_data["Revenue_Growth_Rate"]["HL"], sales_data["Revenue_Growth_Rate"]["SL"]],
                           marker_color=['green', 'purple'])
                ],
                'layout': go.Layout(
                    title="Revenue Growth Rate (%)",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Growth Rate (%)'}
                )
            }
        ),

        # Average Revenue per Item
        dcc.Graph(
            id='avg-revenue-per-item',
            figure={
                'data': [
                    go.Bar(x=["HL", "SL"], y=[sales_data["Avg_Revenue_Per_Item"]["HL"], sales_data["Avg_Revenue_Per_Item"]["SL"]],
                           marker_color=['teal', 'pink'])
                ],
                'layout': go.Layout(
                    title="Average Revenue per Item",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Revenue per Item ($)'}
                )
            }
        ),

        # Gross Margin by Category
        dcc.Graph(
            id='gross-margin',
            figure={
                'data': [
                    go.Bar(x=["HL", "SL"], y=[sales_data["Gross_Margin"]["HL"], sales_data["Gross_Margin"]["SL"]],
                           marker_color=['blue', 'orange'])
                ],
                'layout': go.Layout(
                    title="Gross Margin by Category",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Gross Margin ($)'}
                )
            }
        ),

        # Average Transaction Value (ATV)
        dcc.Graph(
            id='avg-transaction-value',
            figure={
                'data': [
                    go.Bar(x=["HL", "SL"], y=[sales_data["ATV"]["HL"], sales_data["ATV"]["SL"]],
                           marker_color=['cyan', 'magenta'])
                ],
                'layout': go.Layout(
                    title="Average Transaction Value (ATV)",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'ATV ($)'}
                )
            }
        ),

        # Sales by Channel
        dcc.Graph(
            id='sales-by-channel',
            figure={
                'data': [
                    go.Pie(labels=["In-Store", "Online"], values=[sales_data["Channel_Revenue"]["In-Store"],
                                                                  sales_data["Channel_Revenue"]["Online"]],
                           hole=.4)
                ],
                'layout': go.Layout(
                    title="Sales by Channel"
                )
            }
        ),

        # Revenue Per Employee
        dcc.Graph(
            id='revenue-per-employee',
            figure={
                'data': [
                    go.Bar(x=["HL", "SL"], y=[sales_data["Revenue_Per_Employee"]["HL"], sales_data["Revenue_Per_Employee"]["SL"]],
                           marker_color=['gold', 'silver'])
                ],
                'layout': go.Layout(
                    title="Revenue Per Employee",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Revenue Per Employee ($)'}
                )
            }
        ),
    ])
