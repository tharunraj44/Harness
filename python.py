import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python filename.py -f <filename>")
    sys.exit(1)

# Extract the filename provided after the '-f' flag
if sys.argv[1] == '-f':
    filename = sys.argv[2]
    print(f"Filename provided: {filename}")

    # Now you can use the 'filename' variable in your script as needed
    # For instance, if you want to read the contents of the CSV file, you might do something like this:
    try:
        with open(filename, 'r') as file:
            # Process the CSV file here
            pass  # Placeholder for actual processing
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
else:
    print("Usage: python filename.py -f <filename>")
    sys.exit(1)
