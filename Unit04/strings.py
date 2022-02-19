"""def test_strings():
    name = "Kartik\t\'Rajesh\'"
    print("My name is ", name)
    print("Wlcome!", end="\n")
    print("To GCIS-123!")

def main():
    test_strings()

main()"""

def extract_characters(name):
    length = len(name)
    i = 0
    while i < length:
        print(name[i])
        i += 1

def get_name():
    return input("Please enter your name: ")

def main():
    name = get_name()
    extract_characters(name)

main()