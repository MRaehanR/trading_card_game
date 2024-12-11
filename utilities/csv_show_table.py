from utilities.csv_read_list import *
from utilities.print_with_color import *
from tabulate import tabulate

def csv_show_table(filepath):
    data = csv_read_list(filepath)
        
    header = data[0]
    print("\n" + " | ".join(header))
    print("-" * (len(header) * 10))
    
    if not data:
        print_warning("No Data")

    for row in data[1:]:
        print(" | ".join(row))
        
def csv_show_table_tabulate(filepath):
    data = csv_read_list(filepath)
    header = data[0]
    
    data.pop(0)
    
    print(tabulate(data, headers=header, tablefmt="grid"))