import csv
def read_csv_file(path):
    f = open(path)
    r = csv.reader(f)
    rows = []
    for row in r:
        rows.append(row)
    return rows
    
