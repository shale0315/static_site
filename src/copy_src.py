import os

def main():
    # src_dir = "/home/ballerhino/Documents/bootdevprojects/static_site/static"
    # dest_dir = "/home/ballerhino/Documents/bootdevprojects/static_site/public"
    # print(check_dir(src_dir))
    # del_contents(dest_dir)
    print(copy_src())

def check_dir(src_dir):
    if not os.path.exists(src_dir):
        raise Exception("Path not found")
    else:
        return "Path is valid"

def del_contents():
    pass
# print(os.listdir("/home"))
def copy_src():
    src_dir = "/home/ballerhino/Documents/bootdevprojects/static_site/static"
    dest_dir = "/home/ballerhino/Documents/bootdevprojects/static_site/public"
    return os.listdir(src_dir)

main()