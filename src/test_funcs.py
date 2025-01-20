import unittest
from block_md import *
from inline_md import *

class TestMarkdown(unittest.TestCase):
    def test_good_img(self):
        test_list = []
        text1 = "This is test 1 ![Test 1 here](http://test1.com/img1.img)"
        text2 = "This is test 2 ![X% Test 2 99](http://www.test2.com/img%?img2.img)"
        test_list.append(extract_markdown_images(text1))
        test_list.append(extract_markdown_images(text2))
        self.assertListEqual(
            [
                [("Test 1 here", "http://test1.com/img1.img")],
                [("X% Test 2 99", "http://www.test2.com/img%?img2.img")]
            ],
            test_list
        )

    def test_good_link(self):
        test_list = []
        text1 = "This is test 1 [Test 1 link here](http://test1.com/link.com)"
        text2 = "This is test 2 [Test 2 @%^*^](http://www.test2.com/img%?link2)"
        test_list.append(extract_markdown_links(text1))
        test_list.append(extract_markdown_links(text2))
        self.assertListEqual(
            [
                [("Test 1 link here", "http://test1.com/link.com")],
                [("Test 2 @%^*^", "http://www.test2.com/img%?link2")]
            ],
        test_list
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_ordered_text(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
            new_nodes
        )

    def test_reverse_order_text(self):
        text = "This is a [link](https://boot.dev) to an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg), followed by a `code block` then some *italics* and finally a **bold word**"
        new_node = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" to an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(", followed by a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" then some ", TextType.TEXT),
                TextNode("italics", TextType.ITALIC),
                TextNode(" and finally a ", TextType.TEXT),
                TextNode("bold word", TextType.BOLD),
            ],
            new_node
        )

    def test_whitespace(self):
        markdown_content = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item"""
        test = markdown_to_blocks(markdown_content)
        self.assertListEqual(
            ["# This is a heading",
             "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
             "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
             ],
             test
        )

    def test_extralines(self):
        markdown_content = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    
    * This is the first list item in a list block
    * This is a list item
    * This is another list item
    
    """
        test = markdown_to_blocks(markdown_content)
        self.assertListEqual(
            ["# This is a heading",
             "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
             "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
             ],
             test
        )

    def test_header_block(self):
        test_list = []
        header_wrong_format = "#Wrong header"
        header1 = "# Header 1"
        header6 = "###### Header 6"
        header7 = "####### Header 7 is wrong"
        code_right = "```\nThis is code\n```"
        code_wrong = "```This is wrong code```"
        quote_right = ">Quote1\n>Quote2\n>Quote3"
        quote_wrong = ">Quote2\n>Quote2\nQuote3"
        u_list_right_1 = "- item1\n- item 2\n- item3"
        u_list_right_2 = "* item1\n* item 2\n* item3"
        u_list_wrong = "item1\n-item2\n*item3"
        o_list_right = "1. item 1\n2. item 2\n3. item 3"
        o_list_wrong = "1.item1\n2.item2\n3.item3"


        test_list.append(block_to_block_type(header_wrong_format))
        test_list.append(block_to_block_type(header1))
        test_list.append(block_to_block_type(header6))
        test_list.append(block_to_block_type(header7))
        test_list.append(block_to_block_type(code_right))
        test_list.append(block_to_block_type(code_wrong))
        test_list.append(block_to_block_type(quote_right))
        test_list.append(block_to_block_type(quote_wrong))
        test_list.append(block_to_block_type(u_list_right_1))
        test_list.append(block_to_block_type(u_list_right_2))
        test_list.append(block_to_block_type(u_list_wrong))
        test_list.append(block_to_block_type(o_list_right))
        test_list.append(block_to_block_type(o_list_wrong))
        self.assertListEqual(
            [
                "paragraph",
                "heading",
                "heading",
                "paragraph",
                "code",
                "paragraph",
                "quote",
                "paragraph",
                "unordered list",
                "unordered list",
                "paragraph",
                "ordered list",
                "paragraph",
            ],
            test_list
        )


if __name__ == "__main__":
    unittest.main()