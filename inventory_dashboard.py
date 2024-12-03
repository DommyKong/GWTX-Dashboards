import streamlit as st
import plotly.graph_objs as go

def inventory_dashboard():
    # Back to Home Button
    if st.button("Go to Home", key="home_from_inventory"):
        st.experimental_set_query_params(page="home")

    # Custom CSS for consistent widget width
    st.markdown(
        """
        <style>
        [data-testid="metric-container"] {
            width: 40% !important; /* Ensure consistent widget width */
            margin: 0 auto 15px; /* Center widgets and add spacing */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Inventory Dashboard")

    # Widgets
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Stock (HL)", "900 items")
    with col2:
        st.metric("Current Stock (SL)", "700 items")
    with col3:
        st.metric("Turnover Rate (HL)", "3.2 times/month", "+0.5 MoM")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Turnover Rate (SL)", "2.8 times/month", "+0.4 MoM")
    with col5:
        st.metric("Unsold Items (HL)", "150 items", "-10% MoM")
    with col6:
        st.metric("Unsold Items (SL)", "120 items", "-10% MoM")

    col7, col8, col9 = st.columns(3)
    with col7:
        st.metric("Overstock Alerts (HL)", "120 items")
    with col8:
        st.metric("Overstock Alerts (SL)", "100 items")
    with col9:
        st.metric("Shrinkage Rate", "HL: 2%, SL: 1.8%")

    # Graph 1: Current Stock Levels
    st.subheader("Current Stock Levels by Category")
    stock_levels_fig = go.Figure()
    stock_levels_fig.add_trace(go.Bar(x=["HL", "SL"], y=[900, 700], marker_color=["blue", "orange"]))
    stock_levels_fig.update_layout(title="Current Stock Levels", xaxis_title="Category", yaxis_title="Stock (items)")
    st.plotly_chart(stock_levels_fig)

    # Graph 2: Turnover Rate
    st.subheader("Turnover Rate by Category (Times per Month)")
    turnover_rate_fig = go.Figure()
    turnover_rate_fig.add_trace(go.Bar(x=["HL", "SL"], y=[3.2, 2.8], marker_color=["blue", "orange"]))
    turnover_rate_fig.update_layout(title="Turnover Rate by Category", xaxis_title="Category", yaxis_title="Rate (times/month)")
    st.plotly_chart(turnover_rate_fig)

    # Graph 3: Unsold Items
    st.subheader("Unsold Items by Category")
    unsold_items_fig = go.Figure()
    unsold_items_fig.add_trace(go.Bar(x=["HL", "SL"], y=[150, 120], marker_color=["blue", "orange"]))
    unsold_items_fig.update_layout(title="Unsold Items", xaxis_title="Category", yaxis_title="Unsold Items")
    st.plotly_chart(unsold_items_fig)

    # Graph 4: Overstock Alerts
    st.subheader("Overstock Alerts by Category")
    overstock_alerts_fig = go.Figure()
    overstock_alerts_fig.add_trace(go.Bar(x=["HL", "SL"], y=[120, 100], marker_color=["blue", "orange"]))
    overstock_alerts_fig.update_layout(title="Overstock Alerts", xaxis_title="Category", yaxis_title="Items")
    st.plotly_chart(overstock_alerts_fig)

    # Graph 5: Shrinkage Rate
    st.subheader("Shrinkage Rate by Category")
    shrinkage_rate_fig = go.Figure()
    shrinkage_rate_fig.add_trace(go.Bar(x=["HL", "SL"], y=[2.1, 1.8], marker_color=["blue", "orange"]))
    shrinkage_rate_fig.update_layout(title="Shrinkage Rate", xaxis_title="Category", yaxis_title="Rate (%)")
    st.plotly_chart(shrinkage_rate_fig)

    # Graph 6: Aging Inventory Value
    st.subheader("Aging Inventory Value (Unsold for 3 Weeks)")
    aging_inventory_fig = go.Figure()
    aging_inventory_fig.add_trace(go.Bar(x=["HL", "SL"], y=[4500, 3800], marker_color=["blue", "orange"]))
    aging_inventory_fig.update_layout(title="Aging Inventory Value", xaxis_title="Category", yaxis_title="Value ($)")
    st.plotly_chart(aging_inventory_fig)

    # Graph 7: Dead Stock
    st.subheader("Dead Stock (Bale Items Not Sold)")
    dead_stock_fig = go.Figure()
    dead_stock_fig.add_trace(go.Bar(x=["HL", "SL"], y=[200, 150], marker_color=["blue", "orange"]))
    dead_stock_fig.update_layout(title="Dead Stock", xaxis_title="Category", yaxis_title="Items")
    st.plotly_chart(dead_stock_fig)

    # Graph 8: Dead Stock Rate
    st.subheader("Dead Stock Rate Compared to Overall Stock")
    dead_stock_rate_fig = go.Figure()
    dead_stock_rate_fig.add_trace(go.Bar(x=["HL", "SL"], y=[22, 18], marker_color=["blue", "orange"]))
    dead_stock_rate_fig.update_layout(title="Dead Stock Rate", xaxis_title="Category", yaxis_title="Rate (%)")
    st.plotly_chart(dead_stock_rate_fig)
