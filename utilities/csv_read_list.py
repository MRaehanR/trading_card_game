import csv

def csv_read_list(filepath):
    with open(str(filepath), 'r') as File:
        csv_reader = csv.reader(File)
        return list(csv_reader)