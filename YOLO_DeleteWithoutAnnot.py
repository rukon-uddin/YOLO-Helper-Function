import os

file_path = "test_images"
txt_files = [i for i in os.listdir(file_path) if i.endswith(".txt")]
delete_files_counter = 0
for i in txt_files:
    lines = open(f"{file_path}/{i}")
    lines = lines.read()
    if len(lines) == 0:
        img_file_name = i.split(".txt")[0]+".jpg"
        os.remove(f"{file_path}/{i}") # Deleting text file
        os.remove(f"{file_path}/{img_file_name}")  # Deleting image
        delete_files_counter+=1

print(delete_files_counter)