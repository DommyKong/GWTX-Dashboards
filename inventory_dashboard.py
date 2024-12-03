import streamlit as st
import plotly.graph_objs as go

# Adjust sidebar and widget font size
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        min-width: 200px; /* Reduce sidebar width */
        max-width: 200px;
    }
    [data-testid="stMetricValue"] {
        font-size: 18px; /* Reduce widget font size */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def inventory_dashboard():
    # Mock Data for Inventory Dashboard
    data = {
        "Metrics": {
            "Current Stock Levels": {"HL": 900, "SL": 700},
            "Turnover Rate": {"HL": 4.5, "SL": 4.8},
            "Overstock Alerts": {"HL": 120, "SL": 100},
            "Unsold Items (3 Weeks)": {"HL": 150, "SL": 120},
            "Inventory Shrinkage Rate": {"HL": 2.1, "SL": 1.8},
            "Dead Stock": {"HL": 30, "SL": 25},
            "Dead Stock Rate": {"HL": 5, "SL": 4.5},
            "Aging Inventory Value": {"HL": 1800, "SL": 1600},
            "Inventory Value by Category": {"HL": 5000, "SL": 4000},
        }
    }

    # Title
    st.title("Inventory Dashboard")

    # Widgets for Key Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Current Stock (HL)", f"{data['Metrics']['Current Stock Levels']['HL']} items")
        st.metric("Turnover Rate (HL)", f"{data['Metrics']['Turnover Rate']['HL']}%", "+1% MoM")
        st.metric("Overstock Alerts (HL)", f"{data['Metrics']['Overstock Alerts']['HL']} items")

    with col2:
        st.metric("Current Stock (SL)", f"{data['Metrics']['Current Stock Levels']['SL']} items")
        st.metric("Turnover Rate (SL)", f"{data['Metrics']['Turnover Rate']['SL']}%", "+1% MoM")
        st.metric("Overstock Alerts (SL)", f"{data['Metrics']['Overstock Alerts']['SL']} items")

    with col3:
        st.metric("Unsold Items (HL)", f"{data['Metrics']['Unsold Items (3 Weeks)']['HL']} items", "-10% MoM")
        st.metric("Unsold Items (SL)", f"{data['Metrics']['Unsold Items (3 Weeks)']['SL']} items", "-10% MoM")
        st.metric("Shrinkage Rate", f"HL: {data['Metrics']['Inventory Shrinkage Rate']['HL']}%, SL: {data['Metrics']['Inventory Shrinkage Rate']['SL']}%")

    # Graphs
    # 1. Current Stock Levels (HL vs SL)
    st.subheader("Current Stock Levels (HL vs SL)")
    stock_fig = go.Figure()
    stock_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Current Stock Levels"]["HL"],
            data["Metrics"]["Current Stock Levels"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    stock_fig.update_layout(title="Current Stock Levels", xaxis_title="Category", yaxis_title="Items")
    st.plotly_chart(stock_fig, use_container_width=True)

    # 2. Turnover Rate
    st.subheader("Turnover Rate (HL vs SL)")
    turnover_fig = go.Figure()
    turnover_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Turnover Rate"]["HL"],
            data["Metrics"]["Turnover Rate"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    turnover_fig.update_layout(title="Turnover Rate", xaxis_title="Category", yaxis_title="Rate (%)")
    st.plotly_chart(turnover_fig, use_container_width=True)

    # 3. Overstock Alerts
    st.subheader("Overstock Alerts (HL vs SL)")
    overstock_fig = go.Figure()
    overstock_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Overstock Alerts"]["HL"],
            data["Metrics"]["Overstock Alerts"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    overstock_fig.update_layout(title="Overstock Alerts", xaxis_title="Category", yaxis_title="Alerts")
    st.plotly_chart(overstock_fig, use_container_width=True)

    # 4. Unsold Items
    st.subheader("Unsold Items After 3 Weeks (HL vs SL)")
    unsold_fig = go.Figure()
    unsold_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Unsold Items (3 Weeks)"]["HL"],
            data["Metrics"]["Unsold Items (3 Weeks)"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    unsold_fig.update_layout(title="Unsold Items", xaxis_title="Category", yaxis_title="Items")
    st.plotly_chart(unsold_fig, use_container_width=True)

    # 5. Inventory Shrinkage Rate
    st.subheader("Inventory Shrinkage Rate (HL vs SL)")
    shrinkage_fig = go.Figure()
    shrinkage_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Inventory Shrinkage Rate"]["HL"],
            data["Metrics"]["Inventory Shrinkage Rate"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    shrinkage_fig.update_layout(title="Shrinkage Rate", xaxis_title="Category", yaxis_title="Rate (%)")
    st.plotly_chart(shrinkage_fig, use_container_width=True)

    # 6. Dead Stock
    st.subheader("Dead Stock (HL vs SL)")
    dead_stock_fig = go.Figure()
    dead_stock_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Dead Stock"]["HL"],
            data["Metrics"]["Dead Stock"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    dead_stock_fig.update_layout(title="Dead Stock", xaxis_title="Category", yaxis_title="Items")
    st.plotly_chart(dead_stock_fig, use_container_width=True)

    # 7. Dead Stock Rate
    st.subheader("Dead Stock Rate (HL vs SL)")
    dead_rate_fig = go.Figure()
    dead_rate_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Dead Stock Rate"]["HL"],
            data["Metrics"]["Dead Stock Rate"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    dead_rate_fig.update_layout(title="Dead Stock Rate", xaxis_title="Category", yaxis_title="Rate (%)")
    st.plotly_chart(dead_rate_fig, use_container_width=True)

    # 8. Aging Inventory Value
    st.subheader("Aging Inventory Value (HL vs SL)")
    aging_fig = go.Figure()
    aging_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Aging Inventory Value"]["HL"],
            data["Metrics"]["Aging Inventory Value"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    aging_fig.update_layout(title="Aging Inventory Value", xaxis_title="Category", yaxis_title="Value ($)")
    st.plotly_chart(aging_fig, use_container_width=True)

    # 9. Inventory Value by Category
    st.subheader("Inventory Value by Category")
    inventory_value_fig = go.Figure()
    inventory_value_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Inventory Value by Category"]["HL"],
            data["Metrics"]["Inventory Value by Category"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    inventory_value_fig.update_layout(title="Inventory Value by Category", xaxis_title="Category", yaxis_title="Value ($)")
    st.plotly_chart(inventory_value_fig, use_container_width=True)
