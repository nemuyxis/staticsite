from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in TextType:
        raise Exception("Not a valid TextType")

    if text_node.text_type == TextType.TEXT:
        leaf = LeafNode(None, text_node.text)
        return leaf

    if text_node.text_type == TextType.BOLD:
        leaf = LeafNode("b", text_node.text)
        return leaf

    if text_node.text_type == TextType.ITALIC:
        leaf = LeafNode("i", text_node.text)
        return leaf

    if text_node.text_type == TextType.CODE:
        leaf = LeafNode("code", text_node.text)
        return leaf

    if text_node.text_type == TextType.IMAGE:
        leaf = LeafNode("img", "", {"src": "image source url", "alt": "alt text of image",})
        return leaf

    if text_node.text_type == TextType.LINK:
        leaf = LeafNode("a", text_node.text, {"href": text_node.url,})
        return leaf
