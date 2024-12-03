import streamlit as st
import warnings
import plotly.graph_objs as go

# Suppress Streamlit warnings
warnings.filterwarnings("ignore", category=UserWarning, module="streamlit")

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

def sales_dashboard():
    # Back to Home Button
    if st.button("Go to Home", key="home_from_sales"):
        st.experimental_set_query_params(page="home")

    # Mock Data for Sales Dashboard
    data = {
        "Metrics": {
            "Monthly Sales Volume": {"HL": 1200, "SL": 1100},
            "Monthly Revenue": {"HL": 6000, "SL": 5000},
            "Best-Selling Items": {"HL": "Kitchenware", "SL": "Winter Jackets"},
            "Revenue Growth Rate": {"HL": 5, "SL": 6},
            "Average Revenue Per Item": {"HL": 20, "SL": 25},
            "Gross Margin": {"HL": 3000, "SL": 2500},
            "Average Transaction Value": {"HL": 200, "SL": 150},
            "Sales by Channel": {"In-Store": 8000, "Online": 7000},
            "Revenue Per Employee": {"HL": 3000, "SL": 2800},
        }
    }

    # Title
    st.title("Sales Dashboard")

    # Widgets for Key Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Monthly Sales Volume (HL)", f"{data['Metrics']['Monthly Sales Volume']['HL']} items")
        st.metric("Revenue Growth Rate (HL)", f"{data['Metrics']['Revenue Growth Rate']['HL']}%", "+2% MoM")
        st.metric("Best-Selling Item (HL)", f"{data['Metrics']['Best-Selling Items']['HL']}")

    with col2:
        st.metric("Monthly Sales Volume (SL)", f"{data['Metrics']['Monthly Sales Volume']['SL']} items")
        st.metric("Revenue Growth Rate (SL)", f"{data['Metrics']['Revenue Growth Rate']['SL']}%", "+3% MoM")
        st.metric("Best-Selling Item (SL)", f"{data['Metrics']['Best-Selling Items']['SL']}")

    with col3:
        st.metric("Average Revenue/Item (HL)", f"${data['Metrics']['Average Revenue Per Item']['HL']}")
        st.metric("Average Revenue/Item (SL)", f"${data['Metrics']['Average Revenue Per Item']['SL']}")
        st.metric("Gross Margin (HL)", f"${data['Metrics']['Gross Margin']['HL']}")

    # Graphs
    # 1. Monthly Sales Volume
    st.subheader("Monthly Sales Volume (HL vs SL)")
    sales_fig = go.Figure()
    sales_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Monthly Sales Volume"]["HL"],
            data["Metrics"]["Monthly Sales Volume"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    sales_fig.update_layout(title="Monthly Sales Volume", xaxis_title="Category", yaxis_title="Items Sold")
    st.plotly_chart(sales_fig, use_container_width=True)

    # 2. Monthly Revenue
    st.subheader("Monthly Revenue (HL vs SL)")
    revenue_fig = go.Figure()
    revenue_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Monthly Revenue"]["HL"],
            data["Metrics"]["Monthly Revenue"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    revenue_fig.update_layout(title="Monthly Revenue", xaxis_title="Category", yaxis_title="Revenue ($)")
    st.plotly_chart(revenue_fig, use_container_width=True)

    # 3. Revenue Growth Rate
    st.subheader("Revenue Growth Rate (HL vs SL)")
    growth_fig = go.Figure()
    growth_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Revenue Growth Rate"]["HL"],
            data["Metrics"]["Revenue Growth Rate"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    growth_fig.update_layout(title="Revenue Growth Rate", xaxis_title="Category", yaxis_title="Growth (%)")
    st.plotly_chart(growth_fig, use_container_width=True)

    # 4. Average Revenue Per Item
    st.subheader("Average Revenue Per Item (HL vs SL)")
    avg_rev_fig = go.Figure()
    avg_rev_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Average Revenue Per Item"]["HL"],
            data["Metrics"]["Average Revenue Per Item"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    avg_rev_fig.update_layout(title="Average Revenue Per Item", xaxis_title="Category", yaxis_title="Revenue ($)")
    st.plotly_chart(avg_rev_fig, use_container_width=True)

    # 5. Gross Margin
    st.subheader("Gross Margin (HL vs SL)")
    margin_fig = go.Figure()
    margin_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Gross Margin"]["HL"],
            data["Metrics"]["Gross Margin"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    margin_fig.update_layout(title="Gross Margin", xaxis_title="Category", yaxis_title="Margin ($)")
    st.plotly_chart(margin_fig, use_container_width=True)

    # 6. Sales by Channel
    st.subheader("Sales by Channel (In-Store vs Online)")
    channel_fig = go.Figure()
    channel_fig.add_trace(go.Bar(
        x=["In-Store", "Online"],
        y=[
            data["Metrics"]["Sales by Channel"]["In-Store"],
            data["Metrics"]["Sales by Channel"]["Online"],
        ],
        marker_color=["blue", "orange"]
    ))
    channel_fig.update_layout(title="Sales by Channel", xaxis_title="Channel", yaxis_title="Revenue ($)")
    st.plotly_chart(channel_fig, use_container_width=True)

    # 7. Average Transaction Value
    st.subheader("Average Transaction Value (HL vs SL)")
    atv_fig = go.Figure()
    atv_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Average Transaction Value"]["HL"],
            data["Metrics"]["Average Transaction Value"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    atv_fig.update_layout(title="Average Transaction Value", xaxis_title="Category", yaxis_title="Transaction Value ($)")
    st.plotly_chart(atv_fig, use_container_width=True)

    # 8. Revenue Per Employee
    st.subheader("Revenue Per Employee (HL vs SL)")
    rev_per_emp_fig = go.Figure()
    rev_per_emp_fig.add_trace(go.Bar(
        x=["HL", "SL"],
        y=[
            data["Metrics"]["Revenue Per Employee"]["HL"],
            data["Metrics"]["Revenue Per Employee"]["SL"],
        ],
        marker_color=["blue", "orange"]
    ))
    rev_per_emp_fig.update_layout(title="Revenue Per Employee", xaxis_title="Category", yaxis_title="Revenue ($)")
    st.plotly_chart(rev_per_emp_fig, use_container_width=True)
