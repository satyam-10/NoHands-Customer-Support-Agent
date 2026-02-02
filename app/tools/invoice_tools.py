from langchain_core.tools import tool
from app.db.chinook import db

@tool
def get_invoices_by_customer_sorted_by_date(customer_id: str):
    return db.run(f"SELECT * FROM Invoice WHERE CustomerId = {customer_id}")

invoice_tools = [get_invoices_by_customer_sorted_by_date]
