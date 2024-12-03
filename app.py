import streamlit as st
from operations_dashboard import operations_dashboard
from inventory_dashboard import inventory_dashboard
from sales_dashboard import sales_dashboard

# Custom CSS for larger dashboard titles and consistent styling
st.markdown(
    """
    <style>
    .dashboard-title {
        font-size: 24px !important; /* Larger font size for titles */
        font-weight: bold; /* Make the titles bold */
        margin-bottom: 15px; /* Add spacing below the titles */
    }
    [data-testid="metric-container"] {
        width: 40% !important; /* Consistent widget width across pages */
        margin: 0 auto 15px; /* Center widgets and add spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Home Page
def home_page():
    st.title("Thrift Analytics Dashboard")
    st.write("Use the buttons next to the section titles below to navigate to the respective dashboards.")

    # Operations Section
    st.markdown('<div class="dashboard-title">Operations Dashboard</div>', unsafe_allow_html=True)
    if st.button("Go to Operations", key="operations"):
        st.experimental_set_query_params(page="operations")

    # Operations Widgets
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

    # Inventory Section
    st.markdown('<div class="dashboard-title">Inventory Dashboard</div>', unsafe_allow_html=True)
    if st.button("Go to Inventory", key="inventory"):
        st.experimental_set_query_params(page="inventory")

    # Inventory Widgets
    col10, col11, col12 = st.columns(3)
    with col10:
        st.metric("Current Stock (HL)", "900 items")
    with col11:
        st.metric("Current Stock (SL)", "700 items")
    with col12:
        st.metric("Turnover Rate (HL)", "4.5%", "+1% MoM")

    col13, col14, col15 = st.columns(3)
    with col13:
        st.metric("Turnover Rate (SL)", "4.8%", "+1% MoM")
    with col14:
        st.metric("Unsold Items (HL)", "150 items", "-10% MoM")
    with col15:
        st.metric("Unsold Items (SL)", "120 items", "-10% MoM")

    col16, col17, col18 = st.columns(3)
    with col16:
        st.metric("Overstock Alerts (HL)", "120 items")
    with col17:
        st.metric("Overstock Alerts (SL)", "100 items")
    with col18:
        st.metric("Shrinkage Rate", "HL: 2%, SL: 1.8%")

    # Sales Section
    st.markdown('<div class="dashboard-title">Sales Dashboard</div>', unsafe_allow_html=True)
    if st.button("Go to Sales", key="sales"):
        st.experimental_set_query_params(page="sales")

    # Sales Widgets
    col19, col20, col21 = st.columns(3)
    with col19:
        st.metric("Monthly Sales Volume (HL)", "1200 items", "+5% MoM")
    with col20:
        st.metric("Monthly Sales Volume (SL)", "1100 items", "+3% MoM")
    with col21:
        st.metric("Revenue Growth Rate (HL)", "5%", "+2% MoM")

    col22, col23, col24 = st.columns(3)
    with col22:
        st.metric("Revenue Growth Rate (SL)", "6%", "+3% MoM")
    with col23:
        st.metric("Best-Selling Item (HL)", "Kitchenware")
    with col24:
        st.metric("Best-Selling Item (SL)", "Winter Jackets")

    col25, col26, col27 = st.columns(3)
    with col25:
        st.metric("Gross Margin (HL)", "$3000", "+4% MoM")
    with col26:
        st.metric("Gross Margin (SL)", "$2500", "+3% MoM")
    with col27:
        st.metric("Average Revenue Per Item (HL)", "$20", "+1% MoM")

# Main App
def main():
    # Get the current page from the query parameters
    query_params = st.experimental_get_query_params()
    current_page = query_params.get("page", ["home"])[0]

    if current_page == "home":
        home_page()
    elif current_page == "operations":
        operations_dashboard()
    elif current_page == "inventory":
        inventory_dashboard()
    elif current_page == "sales":
        sales_dashboard()

if __name__ == "__main__":
    main()
