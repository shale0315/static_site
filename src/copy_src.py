import os
import shutil

def deltree_and_copy():
    base_src_dir = "./static"
    base_dest_dir = "./public/"
    if os.path.isdir(base_dest_dir):
        shutil.rmtree(base_dest_dir)
        os.mkdir(base_dest_dir)
    else:
        os.mkdir(base_dest_dir)
    return copy_src(base_src_dir,base_dest_dir)
            
def copy_src(base_src_dir, base_dest_dir):
    for item in os.listdir(base_src_dir):
        current_file = os.path.join(base_src_dir,item)
        if os.path.isfile(current_file):
            shutil.copy(current_file,base_dest_dir)
        else:
            dest_path = os.path.join(base_dest_dir,item)
            src_path = os.path.join(base_src_dir,item)
            os.mkdir(dest_path)
            copy_src(src_path, dest_path)