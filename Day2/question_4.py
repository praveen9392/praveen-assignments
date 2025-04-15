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