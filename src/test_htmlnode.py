import unittest

from htmlnode import HTMLNode

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




if __name__ == "__main__":
    unittest.main()