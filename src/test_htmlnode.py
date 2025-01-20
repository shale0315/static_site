import unittest
from inline_md import text_node_to_html_node
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "paragraph text", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("<p>", "paragraph text", None, {"href": "https://www.google.com"})
        self.assertEqual(node,node2)

    def test_default_initialization(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("p", "Hello")
        assert node.to_html() == "<p>Hello</p>"

    def test_leaf_node_with_props(self):
        node = LeafNode("a", "Click me", {"href": "https://boot.dev"})
        assert node.to_html() == '<a href="https://boot.dev">Click me</a>'

    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "Just text")
        assert node.to_html() == "Just text"

    # def test_leaf_node_no_value():
    #     # This should raise a ValueError
    #     node = LeafNode("p", None)
    #     with pytest.raises(ValueError):
    #         node.to_html()

    # def test_parent_node_in_parent_node(self):
    #     node = ParentNode(
    #         "content",
    #         [
    #             ParentNode(
    #                 "p",
    #                 [
    #                     LeafNode("b","Learn the basics of HTML, CSS, and JavaScript"),
    #                     ParentNode(
    #                         "properties",
    #                         [
    #                             LeafNode("a","Click me", {"href": "https://properties.com"}),
    #                             LeafNode("author","Bill Bill"),
    #                         ],
    #                     LeafNode("img","This is in italics",{"src": "http://imagesource.com"})
    #                     )
    #                 ],
    #             ),
    #         ])
    #     assert node.to_html() == '<content><p><b>Learn the basics of HTML, CSS, and JavaScript</b><properties><a href="https://properties.com">Click me</a><author>Bill Bill</author></properties><img src="http://imagesource.com">This is in italics</img></p></content>'


    def test_parent_node_to_html_basic(self):
        children = [
            LeafNode("b", "bold text"),
            LeafNode(None, " regular text")
        ]
        parent_node = ParentNode("p", children)
        expected_html = "<p><b>bold text</b> regular text</p>"
        assert parent_node.to_html() == expected_html

    def test_parent_node_no_children(self):
        try:
            node = ParentNode("div", [])
            node.to_html()
            assert False, "Expected ValueError for no children"
        except ValueError as e:
            assert str(e) == "No children"

    def test_parent_node_no_tag(self):
        try:
            node = ParentNode(None, [LeafNode("span", "content")])
            node.to_html()
            assert False, "Expected ValueError for missing tag"
        except ValueError as e:
            assert str(e) == "No tag"

## text_node_to_html_node Tests

    def test_text_node_to_html_node(self):
    # Test text type
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"
        assert html_node.props == {}

    # Add more test cases for other types...
    # def test_text_node_to_html_node(self):
    #     text_node = TextNode("Hello, world!", TextType.TEXT)
    #     html_node = text_node_to_html_node(text_node)
    #     print(f"Actual props: {html_node.props}")  # Add this line
    #     assert html_node.tag == None
    #     assert html_node.value == "Hello, world!"
    #     assert html_node.props == {}

if __name__ == "__main__":
    unittest.main()