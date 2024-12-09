from utilities.csv_read_list import *
from utilities.print_with_color import *

def csv_show_table(filepath):
    data = csv_read_list(filepath)
        
    header = data[0]
    print("\n" + " | ".join(header))
    print("-" * (len(header) * 10))
    
    if not data:
        print_warning("No Data")

    for row in data[1:]:
        print(" | ".join(row))