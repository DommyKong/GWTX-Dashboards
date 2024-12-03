import streamlit as st
import plotly.graph_objs as go
import pandas as pd

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

def operations_dashboard():
     # Back to Home Button
    if st.button("Go to Home", key="home_from_operations"):
        st.experimental_set_query_params(page="home")

    # Mock Data for Operations Dashboard
    data = {
        "Metrics": {
            "Total Items Processed": {
                "Daily": 500,
                "Weekly": 3000,
                "Monthly": 12000,
            },
            "Processing Time Per Item": {"HL": 3.2, "SL": 3.5},
            "Employee Tagging Performance": {"HL": 310, "SL": 295},
            "Unsold Inventory % (3 Weeks)": {"HL": 18, "SL": 22},
            "Restocking Rate (Days)": {"HL": 1.8, "SL": 2.3},
            "Incoming Donations": {
                "Daily": {"HL": 60, "SL": 55},
                "Weekly": {"HL": 400, "SL": 370},
                "Monthly": {"HL": 1500, "SL": 1400},
            },
            "Donation Conversion Rate": {"HL": 94, "SL": 89},
        }
    }

    # Title
    st.title("Operations Dashboard")

    # Widgets for Key Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Items Processed (Monthly)", f"{data['Metrics']['Total Items Processed']['Monthly']} items", "+5% MoM")
        st.metric("Processing Time (HL)", f"{data['Metrics']['Processing Time Per Item']['HL']} mins", "-0.5% MoM")
        st.metric("Processing Time (SL)", f"{data['Metrics']['Processing Time Per Item']['SL']} mins", "-0.5% MoM")

    with col2:
        st.metric("Unsold Inventory % (HL)", f"{data['Metrics']['Unsold Inventory % (3 Weeks)']['HL']}%", "-2% MoM")
        st.metric("Unsold Inventory % (SL)", f"{data['Metrics']['Unsold Inventory % (3 Weeks)']['SL']}%", "-2% MoM")
        st.metric("Restocking Rate (HL)", f"{data['Metrics']['Restocking Rate (Days)']['HL']} days", "-1% MoM")

    with col3:
        st.metric("Restocking Rate (SL)", f"{data['Metrics']['Restocking Rate (Days)']['SL']} days", "-1% MoM")
        st.metric("Donation Conversion Rate (HL)", f"{data['Metrics']['Donation Conversion Rate']['HL']}%", "+3% MoM")
        st.metric("Donation Conversion Rate (SL)", f"{data['Metrics']['Donation Conversion Rate']['SL']}%", "+3% MoM")

    # Graphs
    # 1. Total Items Processed (Daily/Weekly/Monthly)
    st.subheader("Total Items Processed (Daily/Weekly/Monthly)")
    processed_fig = go.Figure()
    processed_fig.add_trace(go.Bar(
        x=["Daily", "Weekly", "Monthly"],
        y=[
            data["Metrics"]["Total Items Processed"]["Daily"],
            data["Metrics"]["Total Items Processed"]["Weekly"],
            data["Metrics"]["Total Items Processed"]["Monthly"],
        ],
        marker_color=["blue", "orange", "cyan"]
    ))
    processed_fig.update_layout(title="Total Items Processed", xaxis_title="Timeframe", yaxis_title="Items Processed")
    st.plotly_chart(processed_fig, use_container_width=True)

    # 2. Processing Time Per Item (HL vs SL)
    st.subheader("Processing Time Per Item (HL vs SL)")
    time_fig = go.Figure()
    time_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Processing Time Per Item"]["HL"],
            data["Metrics"]["Processing Time Per Item"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    time_fig.update_layout(title="Processing Time Per Item", xaxis_title="Category", yaxis_title="Time (mins)")
    st.plotly_chart(time_fig, use_container_width=True)

    # 3. Employee Tagging Performance (HL vs SL)
    st.subheader("Employee Tagging Performance (HL vs SL)")
    tagging_fig = go.Figure()
    tagging_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Employee Tagging Performance"]["HL"],
            data["Metrics"]["Employee Tagging Performance"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    tagging_fig.update_layout(title="Employee Tagging Performance", xaxis_title="Category", yaxis_title="Items Tagged")
    st.plotly_chart(tagging_fig, use_container_width=True)

    # 4. Unsold Inventory % (HL vs SL)
    st.subheader("Unsold Inventory % After 3 Weeks (HL vs SL)")
    unsold_fig = go.Figure()
    unsold_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Unsold Inventory % (3 Weeks)"]["HL"],
            data["Metrics"]["Unsold Inventory % (3 Weeks)"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    unsold_fig.update_layout(title="Unsold Inventory %", xaxis_title="Category", yaxis_title="Percentage (%)")
    st.plotly_chart(unsold_fig, use_container_width=True)

    # 5. Restocking Rate (HL vs SL)
    st.subheader("Restocking Rate (HL vs SL)")
    restocking_fig = go.Figure()
    restocking_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Restocking Rate (Days)"]["HL"],
            data["Metrics"]["Restocking Rate (Days)"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    restocking_fig.update_layout(title="Restocking Rate", xaxis_title="Category", yaxis_title="Time (Days)")
    st.plotly_chart(restocking_fig, use_container_width=True)

    # 6. Incoming Donations (Monthly HL/SL)
    st.subheader("Incoming Donations (Monthly by HL vs SL)")
    donations_fig = go.Figure()
    donations_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Incoming Donations"]["Monthly"]["HL"],
            data["Metrics"]["Incoming Donations"]["Monthly"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    donations_fig.update_layout(title="Incoming Donations", xaxis_title="Category", yaxis_title="Donations")
    st.plotly_chart(donations_fig, use_container_width=True)

    # 7. Donation Conversion Rate (HL vs SL)
    st.subheader("Donation Conversion Rate (HL vs SL)")
    conversion_fig = go.Figure()
    conversion_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Donation Conversion Rate"]["HL"],
            data["Metrics"]["Donation Conversion Rate"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    conversion_fig.update_layout(title="Donation Conversion Rate", xaxis_title="Category", yaxis_title="Percentage (%)")
    st.plotly_chart(conversion_fig, use_container_width=True)
