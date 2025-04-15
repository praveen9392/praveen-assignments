import datetime
from question_6 import File

path = r"C:\Users\Praveen\Desktop\handson\files"
fs = File(path)
max_files = fs.getMaxSizeFile()
print("Largest files:", max_files)
latest_files = fs.getLatestFiles(datetime.date(2018, 2, 1))
print("Files modified after 1st Feb 2018:", latest_files)
