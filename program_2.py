# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def write_random_numbers():
    while True:
        num_count = input("How many random numbers do you want to write to the file? (up to 1000): ")
        
        try:
            num_count = int(num_count)
            if 1 <= num_count <= 1000:
                break
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Please enter a valid integer.")
    
    try:
        with open('random_numbers.txt', 'w') as file:
            for i in range(num_count):
                random_num = random.randint(1, 500)
                file.write(str(random_num) + '\n')
        
        print(f"Successfully wrote {num_count} random numbers to 'random_numbers.txt'")

    except IOError as e:
        print(f"Error writing to file: {e}")