import csv, sys
import numpy as np

def CSVread(csvpath):
    filename = csvpath
    properties = np.zeros((20))
    count = 0
    with open(filename) as f:
        reader = csv.reader(f)
        try:
            print("File read begins:")
            for row in reader:
                print(row[0],"is set:", row[1])
                properties[count] = row[1]
                count += 1
        except csv.Error as e:
            sys.exit('##ERROR## file {}, line {}: {}'.format(filename, reader.line_num, e))
    print("File read success!")
    return properties

