import unittest

from textnode import TextNode, TextType
from textnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq_different_text_type(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    def test_none_property_on_url(self):
        node1 = TextNode("This is a link", TextType.LINK)
        self.assertIsNone(node1.url)
    def test_neq_different_text(self):
        node1 = TextNode("This is the text of node1", TextType.ITALIC)
        node2 = TextNode("This is the text of node2", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()

