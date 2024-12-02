from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Example Data for Inventory
inventory_data = {
    "Category": ["HL", "SL"],
    "Current_Stock": [1200, 1000],  # Items currently in stock
    "Turnover_Rate": [5.0, 4.5],  # Times inventory is sold/replenished per month
    "Overstock_Alert": [200, 150],  # Overstock (threshold exceeded)
    "Unsold_Items_3_Weeks": [100, 120],  # Items unsold for 3 weeks
    "Inventory_Value": [6000, 5000],  # Total monetary value of inventory
    "Aging_Inventory_Value": [1200, 1000],  # Value of inventory unsold for 3 weeks
    "Shrinkage_Percentage": [2.0, 1.5],  # Percentage of inventory lost
    "Dead_Stock_Items": [50, 40],  # Items not sold within a specified timeframe
    "Total_Stock": [1250, 1040],  # Total inventory including dead stock
}

# Calculate Dead Stock Rate
inventory_data["Dead_Stock_Rate"] = [(inventory_data["Dead_Stock_Items"][i] / inventory_data["Total_Stock"][i]) * 100 for i in range(len(inventory_data["Category"]))]

# Convert Data to DataFrame
inventory_df = pd.DataFrame(inventory_data)

def get_inventory_dashboard():
    return html.Div([
        html.H1("Inventory Dashboard", style={'textAlign': 'center'}),

        # Current Stock Levels
        dcc.Graph(
            id='current-stock',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Current_Stock"], marker_color=['blue', 'orange'])
                ],
                'layout': go.Layout(
                    title="Current Stock Levels by Category",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Stock Levels'}
                )
            }
        ),

        # Turnover Rate
        dcc.Graph(
            id='turnover-rate',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Turnover_Rate"], marker_color=['green', 'purple'])
                ],
                'layout': go.Layout(
                    title="Turnover Rate (Times Per Month)",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Turnover Rate'}
                )
            }
        ),

        # Overstock/Understock Alerts
        dcc.Graph(
            id='overstock-alerts',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Overstock_Alert"], marker_color=['red', 'yellow'])
                ],
                'layout': go.Layout(
                    title="Overstock Alerts by Category",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Overstock Items'}
                )
            }
        ),

        # Items Unsold for 3 Weeks
        dcc.Graph(
            id='unsold-items',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Unsold_Items_3_Weeks"], marker_color=['purple', 'cyan'])
                ],
                'layout': go.Layout(
                    title="Items Unsold for 3 Weeks",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Unsold Items'}
                )
            }
        ),

        # Inventory Value by Category
        dcc.Graph(
            id='inventory-value',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Inventory_Value"], marker_color=['blue', 'orange'])
                ],
                'layout': go.Layout(
                    title="Inventory Value by Category",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Inventory Value ($)'}
                )
            }
        ),

        # Aging Inventory Value
        dcc.Graph(
            id='aging-inventory-value',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Aging_Inventory_Value"], marker_color=['green', 'purple'])
                ],
                'layout': go.Layout(
                    title="Aging Inventory Value (Unsold for 3 Weeks)",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Value ($)'}
                )
            }
        ),

        # Inventory Shrinkage
        dcc.Graph(
            id='shrinkage-percentage',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Shrinkage_Percentage"], marker_color=['red', 'yellow'])
                ],
                'layout': go.Layout(
                    title="Inventory Shrinkage Percentage",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Shrinkage (%)'}
                )
            }
        ),

        # Dead Stock Items
        dcc.Graph(
            id='dead-stock',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Dead_Stock_Items"], marker_color=['purple', 'cyan'])
                ],
                'layout': go.Layout(
                    title="Dead Stock Items",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Dead Stock (Items)'}
                )
            }
        ),

        # Dead Stock Rate
        dcc.Graph(
            id='dead-stock-rate',
            figure={
                'data': [
                    go.Bar(x=inventory_df["Category"], y=inventory_df["Dead_Stock_Rate"], marker_color=['blue', 'orange'])
                ],
                'layout': go.Layout(
                    title="Dead Stock Rate Compared to Overall Stock",
                    xaxis={'title': 'Category'},
                    yaxis={'title': 'Dead Stock Rate (%)'}
                )
            }
        ),
    ])
