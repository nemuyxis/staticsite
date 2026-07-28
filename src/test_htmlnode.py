import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("a", "Test html")
        #node.to_html()


    def test_props_to_html(self):
        test_props = {}
        node = HTMLNode("a", "Test props", None, test_props)
        test_props = {"href": "https://www.google.com", "target": "_blank",}
        node2 = HTMLNode("a", "Test props2", None, test_props)
        node3 = HTMLNode("a", "Test props3")

        print("Node:")
        print(node.props_to_html())
        print("Node2:")
        print(node2.props_to_html())
        print("Node3:")
        print(node3.props_to_html())

    def test__repr__(self):
        test_props = {}
        node = HTMLNode("a", "Test repr", None, test_props)
        test_props = {"href": "https://www.google.com", "target": "_blank",}
        node2 = HTMLNode("a", "Test repr2", None, test_props)
        node3 = HTMLNode("a", "Test repr3")

        node.__repr__()
        node2.__repr__()
        node3.__repr__()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        test_props = {"href": "https://www.google.com", "target": "_blank",}
        node = LeafNode("a", "Click me!", test_props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello World!")
        self.assertEqual(node.to_html(), "<b>Hello World!</b>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode("", "Brute Text value")
        self.assertEqual(node.to_html(), "Brute Text value")




if __name__ == "__main__":
    unittest.main()