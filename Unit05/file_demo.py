def read_file():
    # in_file = open("data\input.txt")                  # relative path 
    with open("data\input.txt") as in_file:
        print(type(in_file))
        # in_file = open("C:\\Users\\Karti\\GCIS123\\Unit05\\data\\input.txt")          # absolute path
        #read
        for line in in_file:
            line = line.strip()                         # removes all whitespace (tabs, spaces and newlines)
            print(line)                                 # from beginning to end of line
        #data processing

def write_file():
    with open("data\output.txt", "a") as out_file:      # relative path 
        out_file.write("Hello\n")
        out_file.write("World")
        out_file.write("\n")
        out_file.write("2022!")
        out_file.close()

def read_csv_file():
    with open("data\grades.csv") as in_file:
        next(in_file)                                   # SKIPPING THE HEADER LINE
        #read
        for line in in_file:
            line = line.strip()                         # REMOVES ALL WHITSPACES (TABS, SPACES AND NEWLINES)
            tokens = line.split(",")                    # FORM BEGINNING TO END OF THE LINE
            final = int(tokens[4])
            print(type(final))
        #data processing

def main():
    # read_file()
    # write_file()
    read_csv_file()

main()