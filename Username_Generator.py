#Script takes in a file with `FirstName and LastName` and generates all kinds of possible Usernames 
#output is stored in output.txt file 
#Example: python Username_Generator.py names.txt

import itertools
import sys

def generate_usernames(first_name, last_name):
    first = first_name.lower()
    last = last_name.lower()
    first_initial = first[0]
    last_initial = last[0]
    
    formats = [
        f"{first}{last}",  # elliotanderson
        f"{last}{first}",  # andersonelliot
        f"{first_initial}{last}",  # eanderson
        f"{last}{first_initial}",  # andersone
        f"{first}.{last}",  # elliot.anderson
        f"{last}.{first}",  # anderson.elliot
        f"{first}_{last}",  # elliot_anderson
        f"{last}_{first}",  # anderson_elliot
        f"{first_initial}.{last}",  # e.anderson
        f"{last}.{first_initial}",  # anderson.e
        f"{first_initial}_{last}",  # e_anderson
        f"{last}_{first_initial}",  # anderson_e
        f"{first_initial}{last_initial}",  # ea
        f"{first_initial}.{last_initial}",  # e.a
        f"{first_initial}_{last_initial}",  # e_a
        f"{first}{last_initial}",  # elliota
        f"{last}{first_initial}",  # andersone
    ]
    
    return set(formats) 

def read_names_from_file(filename):
    names = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                names.append((parts[0], parts[1]))
    return names

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    names = read_names_from_file(filename)
    
    with open("output.txt", "w") as output_file:
        for first, last in names:
            usernames = generate_usernames(first, last)
            for username in sorted(usernames):
                output_file.write(f"{username}\n")
