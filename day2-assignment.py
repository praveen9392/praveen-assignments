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
  


  
#Question-4

import os
target_path = r"c:\Users\Praveen\Desktop\handson"
new_file = r"c:\Users\Praveen\Desktop\assignments\newfile.txt"

def dump_data(dir_path):
    with open(new_file, "a") as output_file:
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                if file_name.endswith(".txt"):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, "r") as input_file:
                        output_file.writelines(input_file)

dump_data(target_path)