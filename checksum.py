import os
import hashlib
import csv

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

def calculate_checksums_for_directory(directory, output_file, algorithm='sha256'):
    """Calculate checksums for all files in a directory and save them to a CSV file."""
    files = get_all_files_in_directory(directory)
    
    with open(output_file, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header
        csvwriter.writerow(["File Path", f"{algorithm.upper()} Checksum"])
        
        for file in files:
            checksum = calculate_checksum(file, algorithm)
            # Write file path and checksum to CSV
            csvwriter.writerow([file, checksum])

# Example usage
directory_path = "."  # Specify the directory path you want to scan
output_file = "checksums.csv"  # CSV file to save the results
calculate_checksums_for_directory(directory_path, output_file, algorithm='sha256')
