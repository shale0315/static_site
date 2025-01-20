
from htmlnode import ParentNode
from inline_md import *

def markdown_to_blocks(markdown):
    blocks = []
    current_block = []
    lines = markdown.split("\n")
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            current_block.append(stripped_line)
        elif current_block:
            blocks.append("\n".join(current_block))
            current_block = []
    if current_block:
        blocks.append("\n".join(current_block))
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    elif block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered list"
    elif block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return "paragraph"
        return "unordered list"
    elif block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered list"
    else:
        return "paragraph"


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text in text_nodes:
        html_node = text_node_to_html_node(text)
        children.append(html_node)
    return children

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    elif block_type == "paragraph":
        return paragraph_to_html_node(block)
    elif block_type == "code":
        return code_to_html_node(block)
    elif block_type == "quote":
        return quote_to_html_node(block)
    elif block_type == "unordered list":
        return ul_to_html_node(block)
    elif block_type == "ordered list":
        return ol_to_html_node(block)
    
def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level > 6:
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ul_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

# Convert the markdown document into a single Parent HTMLNode.
# Parent HTML Node will contain children -- nested HTMLNode objects
def markdown_to_html_node(markdown):
    #Split MD into blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    #Loop over each block
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    #Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
    master_node = ParentNode("div", children)
    return master_node
    
