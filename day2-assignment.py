import os
def find_largest_file(folder):
    largest_file = None
    largest_size = 0

    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            if file_size > largest_size:
                largest_size = file_size
                largest_file = item_path
        elif os.path.isdir(item_path):
            sub_file, sub_size = find_largest_file(item_path)
            if sub_size > largest_size:
                largest_size = sub_size
                largest_file = sub_file
                
    return largest_file, largest_size

target_folder = r"C:\Users\Praveen\Desktop\handson"
largest_file, largest_size = find_largest_file(target_folder)

if largest_size>0:
    print(f"The largest file is: {largest_file}, Size: {largest_size} bytes")
else:
    print("No files found in the directory")