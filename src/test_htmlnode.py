import unittest

from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_method(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        props_as_html = HTMLNode.props_to_html(props)
        self.assertTrue(isinstance(props_as_html, str))

    def test_contains_htmlnode(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        props_as_html = HTMLNode.props_to_html(props)

        node = HTMLNode("a", None, None, props_as_html)
        textRepresentation = HTMLNode.__repr__(node)
        self.assertTrue("HTMLNode" in textRepresentation)

    def test_to_html_method(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        
        props_as_html = HTMLNode.props_to_html(props)

        node = HTMLNode("a", None, None, props_as_html)
    
        with self.assertRaisesRegex(Exception, "NotImplementedError"):
            HTMLNode.to_html(node)

    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("Hello, world!", "a", props)
        self.assertEqual(node.to_html(), "<a href='https://www.google.com' target='_blank'>Hello, world!</a>")

    def test_parent_to_html(self):
       node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        node.to_html()
    )