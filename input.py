import os
file_details = os.path.splitext((input("filename ")))
print(file_details[1][1:])