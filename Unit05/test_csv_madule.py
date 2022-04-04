import csv 

def test_csv_reading():
    with open ('data\grades.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)                            # SKIP THE HEADER METADATA
        for row in csv_reader:
            # print(row)
            print(row[1])
            print(row[5])

def read_csv_file():
    print(" ")
    try:
        with open("data\grades.csv") as in_file:
            csv_reader = csv.reader(in_file, delimiter=",")
            sum = 0
            count = 0
            next(in_file)                                   # SKIPPING THE HEADER LINE
            #read
            for line in in_file:
                count += 1
                try:
                    final = int(line[4])
                except ValueError: 
                    print("A value error has occured in the file. Please review your input file")
                #data processing
                print(line[5])                            # ADDRESS (PART OF ADDRESS)
                sum += final 
                print("The running total is: ", sum)
                #sum (426) and provide average (85.2) final exam mark
                    
            print(" ")
            print("Count is: ", count)
            print("Final sum is: ", sum)
            average = sum/count
            print("Average is: ", average)
            print(" ")
    except FileNotFoundError:
        print("The input file name is invalid.")

def main():
    # print(" ")
    # test_csv_reading()
    # print(" ")
    read_csv_file()
    # test_csv_writing()
main()