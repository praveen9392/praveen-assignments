#Question-3

import os
def find_largest_file(folder):
    largest_file = None
    largest_size = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > largest_size:
                largest_size = file_size
                largest_file = file_path
    return largest_file, largest_size

target_folder = r"C:\Users\Praveen\Desktop\handson"
largest_file, largest_size = find_largest_file(target_folder)

if largest_size > 0:
    print(f"The largest file is: {largest_file}, Size: {largest_size} bytes")
else:
    print("No files found in the directory")