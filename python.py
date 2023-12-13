import sys

if len(sys.argv) == 3 and sys.argv[1] == '-f' and sys.argv[2] == 'abc.csv':
    # Your code for processing the provided filename goes here
    print("Processing abc.csv file...")
    # Example: Read the contents of abc.csv
    try:
        with open('abc.csv', 'r') as file:
            data = file.read()
            print(data)  # Just an example, you can perform any processing here
    except FileNotFoundError:
        print("File not found.")
else:
    print("Usage: python filename.py -f abc.csv")
