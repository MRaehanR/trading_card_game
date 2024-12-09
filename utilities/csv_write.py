import csv

def csv_write(row, file, method_write="row", file_handling="a") :
   with open(file, file_handling, newline="") as f :
      writer = csv.writer(f)
      writer.writerow(row) if method_write == "row" else writer.writerows(row)