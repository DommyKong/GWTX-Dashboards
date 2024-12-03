import streamlit as st
import plotly.graph_objs as go

def sales_dashboard():
    # Back to Home Button
    if st.button("Go to Home", key="home_from_sales"):
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

    st.title("Sales Dashboard")

    # Widgets
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Monthly Sales Volume (HL)", "1200 items", "+5% MoM")
    with col2:
        st.metric("Monthly Sales Volume (SL)", "1100 items", "+3% MoM")
    with col3:
        st.metric("Revenue Growth Rate (HL)", "5%", "+2% MoM")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Revenue Growth Rate (SL)", "6%", "+3% MoM")
    with col5:
        st.metric("Best-Selling Item (HL)", "Kitchenware")
    with col6:
        st.metric("Best-Selling Item (SL)", "Winter Jackets")

    col7, col8, col9 = st.columns(3)
    with col7:
        st.metric("Gross Margin (HL)", "$3000", "+4% MoM")
    with col8:
        st.metric("Gross Margin (SL)", "$2500", "+3% MoM")
    with col9:
        st.metric("Monthly Sell-Through Rate", "HL: 80%, SL: 85%", "+5% MoM")

    # Graph 1: Monthly Sales Volume
    st.subheader("Monthly Sales Volume by Category")
    sales_volume_fig = go.Figure()
    sales_volume_fig.add_trace(go.Scatter(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[1200, 1300, 1250, 1400, 1500, 1600], mode="lines+markers", name="HL", line_color="blue"))
    sales_volume_fig.add_trace(go.Scatter(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[1100, 1200, 1150, 1300, 1400, 1450], mode="lines+markers", name="SL", line_color="orange"))
    sales_volume_fig.update_layout(title="Monthly Sales Volume", xaxis_title="Month", yaxis_title="Items Sold")
    st.plotly_chart(sales_volume_fig)

    # Graph 2: Monthly Revenue Comparison
    st.subheader("Monthly Revenue Comparison by Category")
    revenue_fig = go.Figure()
    revenue_fig.add_trace(go.Bar(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[12000, 13000, 12500, 14000, 15000, 16000], name="HL", marker_color="blue"))
    revenue_fig.add_trace(go.Bar(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[11000, 12000, 11500, 13000, 14000, 14500], name="SL", marker_color="orange"))
    revenue_fig.update_layout(title="Monthly Revenue Comparison", xaxis_title="Month", yaxis_title="Revenue ($)", barmode="group")
    st.plotly_chart(revenue_fig)

    # Graph 3: Best-Selling Items by Category
    st.subheader("Best-Selling Items by Category")
    best_selling_fig = go.Figure()
    best_selling_fig.add_trace(go.Bar(x=["Kitchenware", "Winter Jackets", "Electronics", "Books"], y=[500, 450, 300, 200], marker_color="blue"))
    best_selling_fig.update_layout(title="Best-Selling Items (HL and SL)", xaxis_title="Item Category", yaxis_title="Units Sold")
    st.plotly_chart(best_selling_fig)

    # Graph 4: Revenue Growth Rate
    st.subheader("Revenue Growth Rate by Category")
    revenue_growth_fig = go.Figure()
    revenue_growth_fig.add_trace(go.Bar(x=["HL", "SL"], y=[5, 6], marker_color=["blue", "orange"]))
    revenue_growth_fig.update_layout(title="Revenue Growth Rate", xaxis_title="Category", yaxis_title="Growth Rate (%)")
    st.plotly_chart(revenue_growth_fig)

    # Graph 5: Average Revenue Per Item
    st.subheader("Average Revenue Per Item by Category")
    avg_revenue_fig = go.Figure()
    avg_revenue_fig.add_trace(go.Bar(x=["HL", "SL"], y=[20, 18], marker_color=["blue", "orange"]))
    avg_revenue_fig.update_layout(title="Average Revenue Per Item", xaxis_title="Category", yaxis_title="Revenue Per Item ($)")
    st.plotly_chart(avg_revenue_fig)

    # Graph 6: Gross Margin by Category
    st.subheader("Gross Margin by Category")
    gross_margin_fig = go.Figure()
    gross_margin_fig.add_trace(go.Bar(x=["HL", "SL"], y=[3000, 2500], marker_color=["blue", "orange"]))
    gross_margin_fig.update_layout(title="Gross Margin by Category", xaxis_title="Category", yaxis_title="Gross Margin ($)")
    st.plotly_chart(gross_margin_fig)

    # Graph 7: Monthly Sell-Through Rate
    st.subheader("Monthly Sell-Through Rate (STR) by Category")
    sell_through_fig = go.Figure()
    sell_through_fig.add_trace(go.Bar(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[75, 78, 80, 82, 85, 87], name="HL STR", marker_color="blue"))
    sell_through_fig.add_trace(go.Bar(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[70, 72, 75, 78, 80, 85], name="SL STR", marker_color="orange"))
    sell_through_fig.update_layout(title="Monthly Sell-Through Rate (STR)", xaxis_title="Month", yaxis_title="Sell-Through Rate (%)", barmode="group")
    st.plotly_chart(sell_through_fig)

    # Graph 8: Revenue Per Employee
    st.subheader("Revenue Per Employee")
    revenue_per_employee_fig = go.Figure()
    revenue_per_employee_fig.add_trace(go.Bar(x=["HL", "SL"], y=[3000, 2800], marker_color=["blue", "orange"]))
    revenue_per_employee_fig.update_layout(title="Revenue Per Employee", xaxis_title="Category", yaxis_title="Revenue ($)")
    st.plotly_chart(revenue_per_employee_fig)
