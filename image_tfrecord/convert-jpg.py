import os
def replace(folder_path, old, new):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if(old.lower() in name.lower()):
                file_path = os.path.join(path,name)
                new_name = os.path.join(path,name.lower().replace(old,new))
                os.rename(file_path, new_name)

replace('/mnt/nvme/images-backup/', '.*', '.JPEG')
