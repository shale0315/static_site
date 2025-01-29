from textnode import TextType,TextNode
from htmlnode import HTMLNode, LeafNode
import os

# print(TextType.__members__)

# dict = {"cow":"heifer", "chicken":"hen", "goose":"gander"}

# listed_dict = list(dict)
# converted = ""
# for item in listed_dict:
#     converted += f' {item}="{dict[item]}"'
#     # for value in dict[item]:
#     #     converted += f" {value}"
# print(listed_dict)
# print(converted)

###Recursive Parent
#Take tag, add to string
#For each item in child-item list:
##If item has children, perform ParentNode to_html
##Perform LeafNode to_html
#Add end tag

# "content"
#     "p"Learn the basics of HTML, CSS, and JavaScript</p>
#     <list type="unordered">
#       <item>HTML for structure</item>
#       <item>CSS for styling</item>
#       <item>JavaScript for interactivity</item>
#     </list>
#   </content>

# def text_node_to_html_node(text_node):
#     types = ["text", "bold", "italic", "code", "link"]
#     text.node
#     if text_node.TextType not in types:
#         raise Exception("Invalid type")
#     if text_node.text_type == "text":
#         return LeafNode(None, text_node.text)
#     elif text_node.text_type == "bold":
#         return LeafNode("b", text_node.text)
#     elif text_node.text_type ==  "italic":
#         return LeafNode("i", text_node.text)
#     elif text_node.text_type == "code":
#         return LeafNode("code", text_node.text)
#     elif text_node.text_type == "link":
#         return LeafNode("a", text_node.text, props={"href":text_node.url})
#     #Add image later
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

# node = TextNode("dummy text", TextType.IMAGES, "www.dummy.test")
# print(text_node_to_html_node(node))

# s = "This is text with a **bold text** word"
# s2 = (s.split("**"))
# print(s2)
# # print(len(s2))
# for i in len(s2):
    
    
# "# This is a heading"  -> <h1>This is a heading</h1>
# HTMLNode("<h>", "This is a heading")

# "## This is a heading"  -> <h2>This is a heading</h2>

# * This is the first list item in a list block
# * This is a list item
# * This is another list item

# ->

# <ul>
#     <li>This is the first list item in a list block</li>
#     <li>This is a list item</li>
#     <li>This is another list item</li>
# </ul>

item = "wundercop.xls"
index = 0
for char in item:
    if char == ".":
        break
    else:
        index += 1
sans_extension = item[0:index]
html_file = sans_extension + ".html"
print(html_file)