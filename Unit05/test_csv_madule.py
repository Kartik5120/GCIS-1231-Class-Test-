import csv 

def test_csv_reading():
    with open ('C:\Users\Karti\GCIS123\Unit05\data\gardes.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)                    #Skip the header metadata
        for row in csv_reader:
            print(row[1])
            print(row[5])

def main():
    test_csv_reading()
    # test_csv_writing()
main()