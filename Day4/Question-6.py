import os
import datetime

class File:
    def __init__(self, path):
        self.path = path

    def getMaxSizeFile(self):
        files = []
        for root, _, filenames in os.walk(self.path):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                if os.path.isfile(filepath):
                    size = os.path.getsize(filepath)
                    files.append((filename, size))
        files.sort(key=lambda x: x[1], reverse=True)
        return files[:2]

    def getLatestFiles(self, date):
        latest_files = []
        for root, _, filenames in os.walk(self.path):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                if os.path.isfile(filepath):
                    file_mod_time = datetime.date.fromtimestamp(os.path.getmtime(filepath))
                    if file_mod_time > date:
                        latest_files.append((filename, file_mod_time))
        latest_files.sort(key=lambda x: x[1], reverse=True)
        return latest_files

if __name__ == '__main__':
    path = r"C:\Users\Praveen\Desktop\handson\files"
    fs = File(path)    
    max_files = fs.getMaxSizeFile()
    print("Largest files:", max_files)
    latest_files = fs.getLatestFiles(datetime.date(2018, 2, 1))
    print("Files modified after 1st Feb 2018:", latest_files)
