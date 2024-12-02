from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Example Data for Operations
operations_data = {
    "Metric": ["SL", "HL"],
    "Processed_Items_Daily": [50, 40],
    "Processed_Items_Weekly": [350, 280],
    "Processed_Items_Monthly": [1400, 1120],
    "Processing_Time_Per_Item": [4, 6],  # Minutes
    "Employee_Tagging_Performance": {"Ryan": [180, 150], "Jessica": [120, 120]},  # Items tagged
    "Unsold_Inventory_Percentage": [30, 40],  # Percentage
    "Restocking_Rate": [2, 3],  # Days
    "Incoming_Donations_Daily": [80, 70],
    "Incoming_Donations_Weekly": [560, 490],
    "Incoming_Donations_Monthly": [2240, 1960],
    "Donation_Conversion_Percentage": [85, 80],  # Percentage
}

def get_operations_dashboard():
    return html.Div([
        html.H1("Operations Dashboard", style={'textAlign': 'center'}),

        # Total Items Processed (Daily/Weekly/Monthly)
        dcc.Graph(
            id='processed-items',
            figure={
                'data': [
                    go.Bar(name='Daily', x=operations_data["Metric"], y=operations_data["Processed_Items_Daily"]),
                    go.Bar(name='Weekly', x=operations_data["Metric"], y=operations_data["Processed_Items_Weekly"]),
                    go.Bar(name='Monthly', x=operations_data["Metric"], y=operations_data["Processed_Items_Monthly"]),
                ],
                'layout': go.Layout(
                    title="Total Items Processed (Daily/Weekly/Monthly)",
                    barmode='group',
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Items Processed'}
                )
            }
        ),

        # Processing Time Per Item
        dcc.Graph(
            id='processing-time',
            figure={
                'data': [
                    go.Bar(x=operations_data["Metric"], y=operations_data["Processing_Time_Per_Item"], marker_color=['blue', 'orange'])
                ],
                'layout': go.Layout(
                    title="Processing Time Per Item (Minutes)",
                )
            }
        ),

        # Employee Tagging Performance
        dcc.Graph(
            id='employee-performance',
            figure={
                'data': [
                    go.Bar(name='Ryan (SL)', x=["SL"], y=[operations_data["Employee_Tagging_Performance"]["Ryan"][0]], marker_color='green'),
                    go.Bar(name='Ryan (HL)', x=["HL"], y=[operations_data["Employee_Tagging_Performance"]["Ryan"][1]], marker_color='limegreen'),
                    go.Bar(name='Jessica (SL)', x=["SL"], y=[operations_data["Employee_Tagging_Performance"]["Jessica"][0]], marker_color='red'),
                    go.Bar(name='Jessica (HL)', x=["HL"], y=[operations_data["Employee_Tagging_Performance"]["Jessica"][1]], marker_color='salmon'),
                ],
                'layout': go.Layout(
                    title="Employee Tagging Performance (By Individual)",
                    barmode='group',
                )
            }
        ),

        # Unsold Inventory Percentage
        dcc.Graph(
            id='unsold-inventory',
            figure={
                'data': [
                    go.Bar(x=operations_data["Metric"], y=operations_data["Unsold_Inventory_Percentage"], marker_color=['purple', 'pink'])
                ],
                'layout': go.Layout(
                    title="Unsold Inventory Percentage (After 3 Weeks)",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Percentage'}
                )
            }
        ),

        # Restocking Rate
        dcc.Graph(
            id='restocking-rate',
            figure={
                'data': [
                    go.Bar(x=operations_data["Metric"], y=operations_data["Restocking_Rate"], marker_color=['teal', 'cyan'])
                ],
                'layout': go.Layout(
                    title="Restocking Rate (Days)",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Days'}
                )
            }
        ),

        # Incoming Donations (Daily/Weekly/Monthly)
        dcc.Graph(
            id='incoming-donations',
            figure={
                'data': [
                    go.Bar(name='Daily', x=operations_data["Metric"], y=operations_data["Incoming_Donations_Daily"], marker_color='gold'),
                    go.Bar(name='Weekly', x=operations_data["Metric"], y=operations_data["Incoming_Donations_Weekly"], marker_color='yellow'),
                    go.Bar(name='Monthly', x=operations_data["Metric"], y=operations_data["Incoming_Donations_Monthly"], marker_color='orange'),
                ],
                'layout': go.Layout(
                    title="Incoming Donations (Daily/Weekly/Monthly)",
                    barmode='group',
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Donations'}
                )
            }
        ),

        # Donation Conversion Percentage
        dcc.Graph(
            id='donation-conversion',
            figure={
                'data': [
                    go.Pie(
                        labels=operations_data["Metric"],
                        values=operations_data["Donation_Conversion_Percentage"],
                        hole=.4
                    )
                ],
                'layout': go.Layout(
                    title="Donation Conversion Percentage",
                )
            }
        ),
    ])
