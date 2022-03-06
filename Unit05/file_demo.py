
def read_file():
    # in_file = open("data\input.txt")                  # RELATIVE PATH
    with open("data\input2.txt") as in_file:
        print(type(in_file))
        # in_file = open("C:\\Users\\Karti\\GCIS123\\Unit05\\data\\input.txt")          # ABSOLUTE PATH
        #read
        for line in in_file:
            line = line.strip()                         # REMOVES ALL WHITSPACES (TABS, SPACES AND NEWLINES)
            print(line)                                 # FROM BEGINNING TO END OF THE LINE
        #data processing

def write_file():
    with open("data\output.txt", "a") as out_file:      # RELATIVE PATH
        out_file.write("Hello\n")
        out_file.write("World")
        out_file.write("\n")
        out_file.write("2022!")
        out_file.close()

def read_csv_file():
    print(" ")
    with open("data\grades.csv") as in_file:
        sum = 0
        count = 0
        next(in_file)                                   # SKIPPING THE HEADER LINE
        #read
        for line in in_file:
            count += 1
            line = line.strip()                         # REMOVES ALL WHITSPACES (TABS, SPACES AND NEWLINES)
            tokens = line.split(",")                    # FROM BEGINNING TO END OF THE LINE
            final = int(tokens[4])
            #data processing
            sum += final 
            print("The running total is: ", sum)
            #sum (426) and provide average (85.2) final exam mark
                
        print(" ")
        print("Count is: ", count)
        print("Final sum is: ", sum)
        average = sum/count
        print("Average is: ", average)
        print(" ")

def main():
    # read_file()
    # write_file()
    read_csv_file()

main()