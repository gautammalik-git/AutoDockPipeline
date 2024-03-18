import os
import shutil

old_path = os.getcwd()
#print(old_path)
list = []
energy_file = "Energy.txt"
with open(energy_file) as f:
    data = f.readlines()

for lines in data:
    dir = lines[:13]
    dir_split = dir.split(":")
    full_dir = dir_split[0]

    list.append(full_dir)
result = list
#print(result)
if os.path.exists(old_path + "/" + "full_dir"):
    for item in result:
        path = old_path+"/"+item
        #print(path)
        if os.path.exists(path):
            #print(item)
            new = old_path+"/full_dir"
            os.chdir(new)
            shutil.move(path, new)
else:
    os.mkdir("full_dir")
    for item in result:
        path = old_path + "/" + item
        #print(path)
        if os.path.exists(path):
            #print(item)
            new = old_path + "/full_dir"
            os.chdir(new)
            shutil.move(path, new)











