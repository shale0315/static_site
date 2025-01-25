from textnode import TextNode,TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_md import *
from inline_md import *
from copy_src import *
from extract_html import extract_title
from gen_page import generate_page

def main():
    # test_text = TextNode("dummy text", TextType.BOLD, "www.dummy.test")
    # print(test_text)

    # test_html = HTMLNode("<p>", "dummy paragraph", None, {"href": "https://www.google.com"})
    # print(test_html)

    # converted = test_html.props_to_html()
    # print(converted)

    # props = {"src": "http://www.imgsrc.com","alt": "img description"}
    # test_img = LeafNode("img", "", {"src": "http://www.imgsrc.com","alt": "img description"})
    # print(test_img)
    # print(test_img.to_html())

    # test_leaf = LeafNode("a", "Click me", {"href": "https://boot.dev"})
    # print(test_leaf)
    # print(test_leaf.to_html())

#     test_parent = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )
#     print(test_parent.to_html())

    # pass

# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# print(split_nodes_link([node]))

# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
    # text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    # print(text_to_textnodes(text))

    # markdown_content = """# This is a heading

    # This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    # * This is the first list item in a list block
    # * This is a list item
    # * This is another list item"""
    # print(markdown_to_blocks(markdown_content))

    # l = ['    This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '   and this too ', ]
    # for i in range(len(l)):
    #     ns = l[i].strip()
    #     l[i] = ns
    # print(l)

    # content = markdown_to_blocks(markdown_content)
    # print(block_to_block(content))

#     deltree_and_copy()
#     print(extract_title("""
# # Heading 2

# paragraph of text

# > Quote block
# """)
#     )

    from_path = "./content/index.md"
    dest_path = "./public"
    template_path = "./template.html"
    deltree_and_copy()
    generate_page(from_path, template_path, dest_path)

main()