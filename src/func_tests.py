import unittest
from da_func import *

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


if __name__ == "__main__":
    unittest.main()