import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node,node2)

    def test_eq_method_true(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD)

        equality1 = TextNode.__eq__(node,node2)
        equality2 = TextNode.__eq__(node3,node4)

        self.assertEqual(equality1,equality2)

    def test_eq_method_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.LINK)

        equality1 = TextNode.__eq__(node,node2)
        equality2 = TextNode.__eq__(node3,node4)

        self.assertNotEqual(equality1,equality2)

    def test_string_rep_method(self):
        node = TextNode("Hi mom!", TextType.TEXT, url='www.google.com')
        textRepresentation = TextNode.__repr__(node)
        self.assertTrue(isinstance(textRepresentation, str))
    
    def test_string_rep_method_contains_TextNode(self):
        node = TextNode("Hi mom!", TextType.TEXT, url='www.google.com')
        textRepresentation = TextNode.__repr__(node)
        self.assertTrue("TextNode" in textRepresentation)



    

if __name__ == "__main__":
    unittest.main()