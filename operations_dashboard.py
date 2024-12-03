import streamlit as st
import plotly.graph_objs as go

def operations_dashboard():
    # Back to Home Button
    if st.button("Go to Home", key="home_from_operations"):
        st.experimental_set_query_params(page="home")

    # Custom CSS for widget width
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

    st.title("Operations Dashboard")

    # Widgets
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Items Processed (Monthly)", "12000 items", "+5% MoM")
    with col2:
        st.metric("Processing Time (HL)", "3.2 mins", "-0.5% MoM")
    with col3:
        st.metric("Processing Time (SL)", "3.5 mins", "-0.5% MoM")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Unsold Inventory (HL)", "18%", "-2% MoM")
    with col5:
        st.metric("Unsold Inventory (SL)", "22%", "-2% MoM")
    with col6:
        st.metric("Donation Conversion Rate (HL)", "94%", "+3% MoM")

    col7, col8, col9 = st.columns(3)
    with col7:
        st.metric("Donation Conversion Rate (SL)", "89%", "+3% MoM")
    with col8:
        st.metric("Restocking Rate (HL)", "1.8 days", "-1% MoM")
    with col9:
        st.metric("Restocking Rate (SL)", "2.3 days", "-1% MoM")

    # Graph 1: Total Items Processed
    st.subheader("Total Items Processed")
    items_processed_fig = go.Figure()
    items_processed_fig.add_trace(go.Bar(x=["Daily", "Weekly", "Monthly"], y=[400, 2500, 12000], marker_color="blue"))
    items_processed_fig.update_layout(title="Total Items Processed", xaxis_title="Timeframe", yaxis_title="Items")
    st.plotly_chart(items_processed_fig)

    # Graph 2: Processing Time per Item
    st.subheader("Processing Time per Item")
    processing_time_fig = go.Figure()
    processing_time_fig.add_trace(go.Bar(x=["HL", "SL"], y=[3.2, 3.5], marker_color=["blue", "orange"]))
    processing_time_fig.update_layout(title="Processing Time per Item", xaxis_title="Category", yaxis_title="Time (mins)")
    st.plotly_chart(processing_time_fig)

    # Graph 3: Employee Tagging Performance
    st.subheader("Employee Tagging Performance")
    employee_performance_fig = go.Figure()
    employee_performance_fig.add_trace(go.Bar(x=["HL", "SL"], y=[300, 270], marker_color=["blue", "orange"]))
    employee_performance_fig.update_layout(title="Employee Tagging Performance", xaxis_title="Category", yaxis_title="Tagged Items")
    st.plotly_chart(employee_performance_fig)

    # Graph 4: Unsold Inventory Percentage
    st.subheader("Unsold Inventory Percentage After 3 Weeks")
    unsold_inventory_fig = go.Figure()
    unsold_inventory_fig.add_trace(go.Bar(x=["HL", "SL"], y=[18, 22], marker_color=["blue", "orange"]))
    unsold_inventory_fig.update_layout(title="Unsold Inventory Percentage", xaxis_title="Category", yaxis_title="Percentage (%)")
    st.plotly_chart(unsold_inventory_fig)

    # Graph 5: Restocking Rate
    st.subheader("Restocking Rate")
    restocking_rate_fig = go.Figure()
    restocking_rate_fig.add_trace(go.Bar(x=["HL", "SL"], y=[1.8, 2.3], marker_color=["blue", "orange"]))
    restocking_rate_fig.update_layout(title="Restocking Rate", xaxis_title="Category", yaxis_title="Days")
    st.plotly_chart(restocking_rate_fig)

    # Graph 6: Incoming Donations
    st.subheader("Incoming Donations")
    donations_fig = go.Figure()
    donations_fig.add_trace(go.Bar(x=["Daily", "Weekly", "Monthly"], y=[150, 1000, 4500], marker_color="blue"))
    donations_fig.update_layout(title="Incoming Donations by Timeframe", xaxis_title="Timeframe", yaxis_title="Donations")
    st.plotly_chart(donations_fig)

    # Graph 7: Donation Conversion Percentage
    st.subheader("Donation Conversion Percentage")
    conversion_rate_fig = go.Figure()
    conversion_rate_fig.add_trace(go.Bar(x=["HL", "SL"], y=[94, 89], marker_color=["blue", "orange"]))
    conversion_rate_fig.update_layout(title="Donation Conversion Rate", xaxis_title="Category", yaxis_title="Percentage (%)")
    st.plotly_chart(conversion_rate_fig)
