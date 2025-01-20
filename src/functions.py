### I don't think this file is incorporated into anything

# from textnode import TextType, TextNode
# from htmlnode import HTMLNode, LeafNode


# def text_node_to_html_node(text_node):
#     match(text_node.text_type):
#         case (TextType.TEXT):
#             return LeafNode(None, text_node.text,{})
#         case (TextType.BOLD):
#             return LeafNode("b", text_node.text)
#         case (TextType.ITALIC):
#             return LeafNode("i", text_node.text)
#         case (TextType.CODE):
#             return LeafNode("code", text_node.text)
#         case (TextType.LINKS):
#             return LeafNode("a", text_node.text, props={"href":text_node.url})
#         #Needs modification below.
#         case (TextType.IMAGES):
#             return LeafNode("img","", props={"src":text_node.url, "alt":text_node.text})
#         case _:
#             raise Exception("Invalid type")
        
### I think below was an attempt at this method        
# def splits_nodes_delimiter(old_nodes, delimiter, text_type):
#     string_list = []
#     if text_type != TextType.TEXT:
#         raise Exception("Finish this part")
#     for node in old_nodes:
#         if text_type == TextType.BOLD:
#             # string_list.extend(f'TextNode(node.split(delimiter)
#             string_list.extend(node.split(delimiter))
#     return string_list
            