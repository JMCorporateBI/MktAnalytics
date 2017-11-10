import csv 

# open a file and return a double list
def open_with_csv(filename, d='\t'):
    uuids = []
    with open(filename, encoding='utf-8') as tsvin:
        tsvin = csv.reader(tsvin, delimiter=d)
        for row in tsvin:
            uuids.append(row)
    return uuids