from block_md import *



def extract_title(markdown):
    block_md = markdown_to_blocks(markdown)
    for block in block_md:
        if block_to_block_type(block) == "heading":
            split_block = block.split("\n")
            for item in split_block:
                h1 = check_if_h1(item)
                if h1 == True:
                    item_sans_hash = item.strip("#")
                    return item_sans_hash.strip()
    if h1 == False:
        raise Exception("Missing <h1> heading")
        

def check_if_h1(block):
    heading_node = heading_to_html_node(block)
    if heading_node.tag == "h1":
        return True
    else:
        return False