from langchain_core.tools import tool
from app.db.chinook import db

@tool
def get_invoices_by_customer_sorted_by_date(customer_id: str):
    """Get all invoices for a specific customer.
    
    Retrieve invoice records from the database for a given customer ID.
    
    Args:
        customer_id: The ID of the customer to get invoices for
    """
    return db.run(f"SELECT * FROM Invoice WHERE CustomerId = {customer_id}")

invoice_tools = [get_invoices_by_customer_sorted_by_date]