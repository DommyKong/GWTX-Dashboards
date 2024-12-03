import streamlit as st
from sales_dashboard import sales_dashboard
from operations_dashboard import operations_dashboard
from inventory_dashboard import inventory_dashboard

# Sidebar Navigation
st.sidebar.title("Navigation")
dashboard_selection = st.sidebar.radio(
    "Select Dashboard", 
    ["Home", "Sales Dashboard", "Operations Dashboard", "Inventory Dashboard"]
)

# Home Page
if dashboard_selection == "Home":
    st.title("Welcome to the Thrift Analytics Dashboard")
    st.write("""
        This application provides comprehensive insights into various aspects of the thrifting business:
        - **Sales Dashboard**: View metrics like sales volume, revenue, and growth rates.
        - **Operations Dashboard**: Monitor operational performance and efficiency.
        - **Inventory Dashboard**: Track stock levels, turnover rates, and shrinkage.
        
        Use the sidebar to navigate between dashboards.
    """)

# Sales Dashboard
elif dashboard_selection == "Sales Dashboard":
    sales_dashboard()

# Operations Dashboard
elif dashboard_selection == "Operations Dashboard":
    operations_dashboard()

# Inventory Dashboard
elif dashboard_selection == "Inventory Dashboard":
    inventory_dashboard()
