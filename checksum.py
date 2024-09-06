import os
import hashlib
from prettytable import PrettyTable

def calculate_checksum(filename, algorithm='sha256'):
    """Calculate the checksum of a file using the specified algorithm."""
    with open(filename, 'rb') as f:
        data = f.read()
        hash_object = hashlib.new(algorithm)
        hash_object.update(data)
        return hash_object.hexdigest()

def get_all_files_in_directory(directory):
    """Recursively get all files in a directory, including nested directories."""
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def calculate_checksums_for_directory(directory, algorithm='sha256'):
    """Calculate checksums for all files in a directory and print in tabular form."""
    files = get_all_files_in_directory(directory)
    
    table = PrettyTable()
    table.field_names = ["File Path", f"{algorithm.upper()} Checksum"]
    
    for file in files:
        checksum = calculate_checksum(file, algorithm)
        table.add_row([file, checksum])
    
    print(table)

# Example usage
directory_path = "."  # Specify the directory path you want to scan
calculate_checksums_for_directory(directory_path, algorithm='sha256')

