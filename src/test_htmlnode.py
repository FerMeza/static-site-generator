import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_repr(self):
        expected_value = "HTMLNode(a, my_link, None, {'href': 'http://www.example.com/', 'target': '_blank'})"
        node = HTMLNode("a", "my_link", props={"href": "http://www.example.com/", "target": "_blank"})
        self.assertEqual(str(node), expected_value)
    
    def test_eq_propts_to_html(self):
        expected_value = ' href="http://www.example.com/" target="_blank"'
        props = HTMLNode("a", "my_link", props={"href": "http://www.example.com/", "target": "_blank"}).props_to_html()
        self.assertEqual(props, expected_value)

    def test_eq_repr_nested(self):
        my_game_1 = HTMLNode("li", "portal")
        my_game_2 = HTMLNode("li", "portal 2")
        portal_games = HTMLNode("ul", None, list((my_game_1, my_game_2)))
        expected = "HTMLNode(ul, None, [HTMLNode(li, portal, None, None), HTMLNode(li, portal 2, None, None)], None)"
        self.assertEqual(str(portal_games), expected)

class TestLeafNode(unittest.TestCase):
    def test_eq_to_html(self):
        node = LeafNode("p", "Hello, world!", {"class": "test", "id": "dont-care"})
        self.assertEqual(node.to_html(), '<p class="test" id="dont-care">Hello, world!</p>')
    
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()