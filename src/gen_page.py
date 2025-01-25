from block_md import markdown_to_html_node
from htmlnode import *
from extract_html import extract_title
import os



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        src_contents = f.read()
    with open(template_path, 'r') as f:
        template_contents = f.read()
    # print(type(template_contents))
    src_md = markdown_to_html_node(src_contents)
    src_md_to_html = src_md.to_html()
    title = extract_title(src_contents)
    # print(type(title))
    new_title = template_contents.replace("{{ Title }}", title)
    new_contents = new_title.replace("{{ Content }}", src_md_to_html)
    # print(new_contents)
    check_dest_path(dest_path)
    dest_file = os.path.join(dest_path,"index.html")
    with open(dest_file, 'w') as f:
        f.write(new_contents)
    return dest_file
    
def check_dest_path(dest_path):
    is_dir = os.path.isdir(dest_path)
    if is_dir == False:
        return os.mkdir(dest_path)