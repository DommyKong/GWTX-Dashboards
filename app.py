import streamlit as st
from operations_dashboard import operations_dashboard
from inventory_dashboard import inventory_dashboard
from sales_dashboard import sales_dashboard

# Custom CSS to style buttons and align them inline with titles
st.markdown(
    """
    <style>
    .header-button-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    .header-title {
        font-size: 20px;
        font-weight: bold;
        margin: 0;
    }
    .header-button button {
        padding: 8px 20px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Home Page
def home_page():
    st.title("Business Analytics Dashboard")
    st.write("Welcome! Use the buttons next to the section titles below to navigate to the respective dashboards.")

    # Operations Section
    st.markdown('<div class="header-button-container"><p class="header-title">Operations Dashboard</p><div class="header-button">', unsafe_allow_html=True)
    if st.button("Go to Operations", key="operations"):
        st.experimental_set_query_params(page="operations")
    st.markdown("</div></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Items Processed (Monthly)", "12000 items", "+5% MoM")
        st.metric("Processing Time (HL)", "3.2 mins", "-0.5% MoM")
        st.metric("Processing Time (SL)", "3.5 mins", "-0.5% MoM")
    with col2:
        st.metric("Unsold Inventory (HL)", "18%", "-2% MoM")
        st.metric("Unsold Inventory (SL)", "22%", "-2% MoM")
        st.metric("Restocking Rate (HL)", "1.8 days", "-1% MoM")
    with col3:
        st.metric("Restocking Rate (SL)", "2.3 days", "-1% MoM")
        st.metric("Donation Conversion Rate (HL)", "94%", "+3% MoM")
        st.metric("Donation Conversion Rate (SL)", "89%", "+3% MoM")

    # Inventory Section
    st.markdown('<div class="header-button-container"><p class="header-title">Inventory Dashboard</p><div class="header-button">', unsafe_allow_html=True)
    if st.button("Go to Inventory", key="inventory"):
        st.experimental_set_query_params(page="inventory")
    st.markdown("</div></div>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Current Stock (HL)", "900 items")
        st.metric("Turnover Rate (HL)", "4.5%", "+1% MoM")
        st.metric("Overstock Alerts (HL)", "120 items")
    with col5:
        st.metric("Current Stock (SL)", "700 items")
        st.metric("Turnover Rate (SL)", "4.8%", "+1% MoM")
        st.metric("Overstock Alerts (SL)", "100 items")
    with col6:
        st.metric("Unsold Items (HL)", "150 items", "-10% MoM")
        st.metric("Unsold Items (SL)", "120 items", "-10% MoM")
        st.metric("Shrinkage Rate", "HL: 2.1%, SL: 1.8%")

    # Sales Section
    st.markdown('<div class="header-button-container"><p class="header-title">Sales Dashboard</p><div class="header-button">', unsafe_allow_html=True)
    if st.button("Go to Sales", key="sales"):
        st.experimental_set_query_params(page="sales")
    st.markdown("</div></div>", unsafe_allow_html=True)

    col7, col8, col9 = st.columns(3)
    with col7:
        st.metric("Monthly Sales Volume (HL)", "1200 items")
        st.metric("Revenue Growth Rate (HL)", "5%", "+2% MoM")
        st.metric("Best-Selling Item (HL)", "Kitchenware")
    with col8:
        st.metric("Monthly Sales Volume (SL)", "1100 items")
        st.metric("Revenue Growth Rate (SL)", "6%", "+3% MoM")
        st.metric("Best-Selling Item (SL)", "Winter Jackets")
    with col9:
        st.metric("Average Revenue/Item (HL)", "$20")
        st.metric("Average Revenue/Item (SL)", "$25")
        st.metric("Gross Margin (HL)", "$3000")

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
