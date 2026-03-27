# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    try:
        with open('names.txt', 'r') as file:
            names = file.readlines()
            name_count = len(names)
        
        print(f"The file contains {name_count} name(s).")

    except FileNotFoundError:
        print("Error: The file 'names.txt' was not found.")
    except IOError as e:
        print(f"Error reading file: {e}")
    ######################
    print('In the count_file_lines function')


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()