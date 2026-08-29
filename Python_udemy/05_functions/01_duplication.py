#Reducing the duplication of code 
def print_order(name,chai_type):
    print(f"{name} ordered {chai_type} chai")

print_order("Aman","Masala")
print_order("Bob","Ginger")
print_order("Charlie","Tulsi")

#Splitting comples tasks
def fetch_sales():
    print("Fetching sales data")

def filter_valid_sales():
    print("Filtering valid sales")

def summarize_data():
    print("Summarizing data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")
    
generate_report()