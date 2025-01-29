from block_md import markdown_to_html_node
from htmlnode import *
from extract_html import extract_title
import os



def generate_page(from_path, template_path, dest_path):
    md_filename = os.path.basename(from_path)
    html_filename = convert_extension_to_html(md_filename)
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
    dest_file = os.path.join(dest_path, html_filename)
    with open(dest_file, 'w') as f:
        f.write(new_contents)
    return dest_file
    
def check_dest_path(dest_path):
    is_dir = os.path.isdir(dest_path)
    if is_dir == False:
        return os.mkdir(dest_path)
    
def convert_extension_to_html(filename):
    index = 0
    for char in filename:
        if char == ".":
            break
        else:
            index += 1
    sans_extension = filename[0:index]
    html_file = sans_extension + ".html"
    return html_file
    
def generate_pages_recursive(dir_path_content, template_path, dest_path_content):
    for item in os.listdir(dir_path_content):
        current_item_path = os.path.join(dir_path_content,item)
        dest_path = os.path.join(dest_path_content, item)
        if item[-3:] == ".md":
            is_file = os.path.isfile(current_item_path)
            if is_file:
                parent_dir = os.path.dirname(dest_path)
                generate_page(current_item_path, template_path, parent_dir)
        else:
            is_dir = os.path.isdir(current_item_path)
            if is_dir:
                if not os.path.isdir(dest_path):
                    os.mkdir(dest_path)
                generate_pages_recursive(current_item_path, template_path, dest_path)
                