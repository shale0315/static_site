from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case (TextType.TEXT):
            return LeafNode(None, text_node.text,{})
        case (TextType.BOLD):
            return LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case (TextType.CODE):
            return LeafNode("code", text_node.text)
        case (TextType.LINK):
            return LeafNode("a", text_node.text, props={"href":text_node.url})
        #Needs modification below.
        case (TextType.IMAGE):
            return LeafNode("img","", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Invalid type")
        
        
# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     tuple_list = []
#     i = 0
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT:
#             return node
#         split_node = node.text.split(delimiter)
#         for string in split_node:
#             if i == 0 or i % 2 == 0:
#                 tuple_list.append(TextNode(string,TextType.TEXT))
#             else:
#                 tuple_list.append(TextNode(string,text_type))
#             i+=1
#     return tuple_list

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    img_md = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return img_md

def extract_markdown_links(text):
    link_md = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_md

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    old_node = [TextNode(text, TextType.TEXT)]
    new_node = split_nodes_delimiter(old_node, "**", TextType.BOLD)
    new_node = split_nodes_delimiter(new_node, "*", TextType.ITALIC)
    new_node = split_nodes_delimiter(new_node, "`",TextType.CODE)
    new_node = split_nodes_image(new_node)
    new_node = split_nodes_link(new_node)
    return new_node

# def markdown_to_blocks(markdown):
#     string_list = markdown.split("\n")
#     for i in range(len(string_list)):
#         new_string = string_list[i].strip()
#         string_list[i] = new_string
#     for string in string_list:
#         if len(string) == 0:
#             string_list.remove(string)
    
#     return string_list

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

def block_to_block(block):
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

## Loop through MD blocks 
def block_loop(block_list):
    for block in block_list:
        #Determine block type
        html_node = block_to_html_node(block)
    return block_type_list

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text in text_nodes:
        html_node = text_node_to_html_node(text)
        children.append(html_node)
    return children

def block_to_html_node(block):
    block_type = block_to_block(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    elif block_type == "paragraph":
        return paragraph_to_html_node(block)
    elif block_type == "code":
        return code_to_html_node(block)
    elif block_type == "quote":
        return "<quoteblock>"
    elif block_type == "unordered list":
        return "<ul>"
    elif block_type == "ordered list":
        return "<ol>"
    
def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in range(len(block)):
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
    text = block(4:-3)
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

# Convert the markdown document into a single Parent HTMLNode.
# Parent HTML Node will contain children -- nested HTMLNode objects
def markdown_to_html_node(markdown):
    #Split MD into blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    #Loop over each block
    block_loop(blocks)
    #Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
    master_node = ParentNode("<div>", None, children_list, None)
    return master_node
    pass
    
